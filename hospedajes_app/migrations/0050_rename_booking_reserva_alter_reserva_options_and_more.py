# Generated by Django 4.1.1 on 2022-11-26 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospedajes_app', '0049_rename_comfort_capacidad_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Booking',
            new_name='Reserva',
        ),
        migrations.AlterModelOptions(
            name='reserva',
            options={'verbose_name_plural': 'Reservas'},
        ),
        migrations.RenameField(
            model_name='rentaldate',
            old_name='booking',
            new_name='reserva',
        ),
    ]
