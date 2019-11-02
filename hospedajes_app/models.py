from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Host(User):
    pass

    class Meta:
        verbose_name_plural = 'Users'


class City(models.Model):
    name = models.CharField(max_length=25, null=True)
    country = models.CharField(max_length=25, null=True)

    def __str__(self):
        return self.name + ", " + self.country

    class Meta:
        verbose_name_plural = 'Cities'


class Booking(models.Model):
    name = models.CharField(max_length=25, null=True)
    surname = models.CharField(max_length=25, null=True)
    email = models.EmailField(null=True)
    dni = models.IntegerField(null=True)
    total = models.FloatField(default=0, null=True)

    def __str__(self):
        return self.name + ", " + self.surname + ", " + self.email + ", " + self.dni + "."

    class Meta:
        verbose_name_plural = 'Bookings'


class Property(models.Model):
    pax = models.IntegerField(null=True)
    title = models.CharField(max_length=25, null=True)
    description = models.CharField(max_length=25, null=True)
    image = models.ImageField(null=True, default=0)
    daily_import = models.FloatField(null=True)
    #  fk_user = models.ForeignKey(Host, null=True, on_delete=models.DO_NOTHING)  # models.SET_NULL
    #  fk_city = models.ForeignKey(City, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title + ", " + self.description + ", " + self.pax + ", " + self.daily_import + "."

    class Meta:
        verbose_name_plural = 'Properties'


class RentalDate(models.Model):
    fk_property = models.ForeignKey(Property, null=True, on_delete=models.DO_NOTHING)
    fk_booking = models.ForeignKey(Booking, null=True, blank=True, on_delete=models.DO_NOTHING)
    date = models.DateField(null=True)

    def __str__(self):
        return self.date + "."

    class Meta:
        verbose_name_plural = 'RentalDates'
