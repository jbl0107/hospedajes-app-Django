# Generated by Django 4.1.1 on 2022-11-26 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospedajes_app', '0047_rename_city_tipoaula_alter_tipoaula_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Feature',
            new_name='Caracteristica',
        ),
        migrations.AlterModelOptions(
            name='caracteristica',
            options={'verbose_name_plural': 'Caracteristicas'},
        ),
        migrations.RenameField(
            model_name='property',
            old_name='features',
            new_name='caracteristicas',
        ),
    ]
