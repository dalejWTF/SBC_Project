# Generated by Django 4.0.6 on 2022-08-01 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=500, verbose_name='Codigo empresa')),
                ('name', models.CharField(blank=True, max_length=3000, null=True, verbose_name='nombre de la empresa')),
                ('country', models.CharField(blank=True, max_length=500, null=True, verbose_name='Ciudad')),
                ('imagen', models.URLField(blank=True, max_length=2000, null=True)),
                ('logo', models.URLField(blank=True, max_length=2000, null=True)),
                ('detail', models.CharField(blank=True, max_length=500, null=True, verbose_name='Detalle')),
                ('product', models.CharField(blank=True, max_length=5000, null=True, verbose_name='Productos')),
                ('json_original', models.TextField(blank=True, max_length=500000, null=True, verbose_name='JSON original')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
    ]
