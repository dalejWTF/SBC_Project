from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.template import loader

from .models import Enterprise


def index(request):
    template = loader.get_template('../templates/index.html')
    context = {
        # 'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def get_company(request):
    get_company = Enterprise.objects.all()
    template = loader.get_template('../templates/company_list.html')
    context = {
        'get_company': get_company,
    }
    return HttpResponse(template.render(context, request))

def detail_company(request,pk):
    get_company = get_object_or_404(Enterprise, pk=pk)
    template = loader.get_template('../templates/company_detail.html')
    context = {
        'get_company': get_company,
        'url_node':f'https://query.wikidata.org/embed.html#%23defaultView%3AGraph%0ASELECT%20%3Fi%20%3FiLabel%20%3Fipicture%20%3Fp%20%3FpLabel%20%3Fppicture%20%3Fo%20%3FoLabel%20%3Fopicture%20WHERE%20%7B%0A%20%20BIND(wd%3A{get_company.code}%20AS%20%3Findustry)%0A%20%20%3Findustry%20(p%3AP361%2Fps%3AP361)%20%3Fp.%0A%20%20%3Fp%20wdt%3AP17%20%3Fo.%0A%20%20OPTIONAL%7B%0A%20%20%20%20%3Fp%20wdt%3AP154%20%3Fppicture.%20%20%0A%20%20%20%20%7D%0A%20%20%0A%20%20%3Fo%20wdt%3AP18%20%3Fopicture.%0A%20%20BIND(wd%3A{get_company.code}%20AS%20%3Fi)%0A%20%20%3Fi%20(p%3AP361%2Fps%3AP361)%20%3Fp.%0A%20%20%3Fi%20wdt%3AP17%20%3Fo.%0A%20%20%3Fi%20wdt%3AP18%20%3Fipicture.%0A%20%20%3Fo%20wdt%3AP18%20%3Fopicture.%0A%20%20%0A%20%20%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22%5BAUTO_LANGUAGE%5D%2Cen%22.%20%7D%0A%7D'
    }
    return HttpResponse(template.render(context, request))
