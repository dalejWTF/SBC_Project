from django.db import models
from qwikidata.entity import WikidataItem
from qwikidata.linked_data_interface import get_entity_dict_from_api
from qwikidata.sparql  import return_sparql_query_results
from datetime import datetime

# Create your models here.

class Enterprise(models.Model):
    code = models.CharField(max_length=500, verbose_name="Codigo empresa")
    name = models.CharField(max_length=3000,  verbose_name="nombre de la empresa",null=True,blank=True)
    country = models.CharField(max_length=500, verbose_name="Ciudad",null=True,blank=True)
    imagen = models.URLField(max_length = 2000,null=True,blank=True)
    logo = models.URLField(max_length = 2000,null=True,blank=True)
    detail = models.CharField(max_length=500, verbose_name="Detalle",null=True,blank=True)
    product = models.CharField(max_length=5000, verbose_name="Productos",null=True,blank=True)
    haspart = models.CharField(max_length=5000, verbose_name="Parte de",null=True,blank=True)
    created = models.CharField(max_length=5000, verbose_name="Fecha de creacion",null=True,blank=True)
    json_original = models.TextField(max_length=500000, verbose_name="JSON original",null=True,blank=True)

    class Meta:
        verbose_name="Empresa"
        verbose_name_plural="Empresas"

    def __str__(self):
        return f"{str(self.name)} {str(self.code)}"

    def save(self, *args, **kwargs):
        query = """
        SELECT ?WDid ?countryLabel ?logo ?managerLabel ?imagen 
        ?productLabel ?subsidiaryLabel ?haspartLabel ?createdLabel
        WHERE {
            ?WDid wdt:P279* wd:"""+self.code+""" .
                   OPTIONAL{?WDid wdt:P17 ?country}.
                   OPTIONAL{?WDid wdt:P154 ?logo}.
                   OPTIONAL{?WDid wdt:P18 ?imagen}.
                   OPTIONAL{?WDid wdt:P1056 ?product}.   
                   OPTIONAL{?WDid wdt:P361 ?haspart}.   
                   OPTIONAL{?WDid wdt:P571 ?created}.   
        SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
        }
        """
        # obtiene todo el JSON
        res = return_sparql_query_results(query)
        data = res.get("results").get("bindings")
        product = list()
        subsidiary = list()
        haspart = list()
        for data in data:
            try:
                product.append(data.get("productLabel").get("value"))
            except Exception as e:
                print(e)
                pass
            try:
                haspart.append(data.get("haspartLabel").get("value"))
            except Exception as e:
                print(e)
                pass
        self.product = list(dict.fromkeys(product))
        self.haspart = list(dict.fromkeys(haspart))
        # guardo la code de wikidata
        try:
            self.country = res.get("results").get("bindings")[0].get("country").get("value")
        except Exception as e:
            print(e)
            pass
        try:
            self.imagen = res.get("results").get("bindings")[0].get("imagen").get("value")
        except Exception as e:
            print(e)
            pass
        try:
            self.country = res.get("results").get("bindings")[0].get("countryLabel").get("value")
        except Exception as e:
            print(e)
            pass
        try:
            self.logo = res.get("results").get("bindings")[0].get("logo").get("value")
        except Exception as e:
            print(e)
            pass
        try:
            self.created = res.get("results").get("bindings")[0].get("createdLabel").get("value")
        except Exception as e:
            print(e)
            pass

        q42_dict = get_entity_dict_from_api(self.code)
        # guardo el JSON
        self.json_original=q42_dict
        # guardo el nombre de wikidata
        self.name=q42_dict.get("labels").get("es").get("value")
        try:
            # guardo el detalle de wikidata
            self.detail=q42_dict.get("descriptions").get("es").get("value")
        except Exception as e:
            print(e)
        super(Enterprise, self).save(*args, **kwargs)
