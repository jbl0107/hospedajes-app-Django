from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Host(User):
    pass

    class Meta:
        verbose_name_plural = 'Users'


class User(models.Model):
    name = models.CharField(max_length=25, null=True)
    surname = models.CharField(max_length=25, null=True)
    email = models.EmailField(null=True)
    dni = models.IntegerField(null=True)

    def __str__(self):
        return self.name + ", " + self.surname + "."

    class Meta:
        verbose_name_plural = "Users"


class City(models.Model):
    name = models.CharField(max_length=25, null=True, unique=True)

    def __str__(self):
        return self.name + '.'

    class Meta:
        verbose_name_plural = 'Cities'


class Booking(models.Model):  # Reserva
    user = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
    total = models.FloatField(default=0, null=True)

    def __str__(self):
        return self.name + "."

    class Meta:
        verbose_name_plural = 'Bookings'


class Property(models.Model):
    pax = models.IntegerField(null=True)
    title = models.CharField(max_length=25, null=True)
    description = models.CharField(max_length=100, null=True)
    image = models.ImageField(null=True, blank=True)
    daily_import = models.FloatField(null=True)
    # user = models.ForeignKey(Host, null=True, on_delete=models.DO_NOTHING)  # models.SET_NULL
    city = models.ForeignKey(City, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title + ", " + self.description + "."

    class Meta:
        verbose_name_plural = 'Properties'


class RentalDate(models.Model):
    fk_property = models.ForeignKey(Property, null=True, on_delete=models.DO_NOTHING)
    fk_booking = models.ForeignKey(Booking, null=True, blank=True, on_delete=models.DO_NOTHING)
    date = models.DateField(null=True)

    def __str__(self):
        return "Fecha"

    class Meta:
        verbose_name_plural = 'RentalDates'
