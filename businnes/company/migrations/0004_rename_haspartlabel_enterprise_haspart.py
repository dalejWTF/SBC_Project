# Generated by Django 4.0.6 on 2022-08-01 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_alter_enterprise_haspartlabel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enterprise',
            old_name='haspartLabel',
            new_name='haspart',
        ),
    ]