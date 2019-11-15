from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models


class Host(User):
    pass

    class Meta:
        verbose_name_plural = 'Hosts'


class Profile(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    dni = models.IntegerField(unique=True)

    def __str__(self):
        return self.name + ", " + self.surname + "."

    class Meta:
        verbose_name_plural = "Profiles"


class City(models.Model):
    name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cities'


class Feature(models.Model):
    name = models.CharField(max_length=25, unique=True)
    className = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Features'


class Comfort(models.Model):
    name = models.CharField(max_length=25, unique=True)
    className = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Comforts'


class Booking(models.Model):  # Reserva
    profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    total = models.FloatField(default=0)

    def __str__(self):
        return self.profile.name + ", " + self.profile.surname + "."

    class Meta:
        verbose_name_plural = 'Bookings'


class Property(models.Model):
    pax = models.IntegerField()
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=100, null=True)
    image = models.ImageField(null=True, blank=True)
    daily_import = models.FloatField()
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    features = models.ManyToManyField(Feature, blank=True)
    user = models.ForeignKey(Host, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title + ", " + self.description + "."

    class Meta:
        verbose_name_plural = 'Properties'


class ComfortXProperty(models.Model):
    comfort = models.ForeignKey(Comfort, on_delete=models.DO_NOTHING)
    property = models.ForeignKey(Property, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()

    def __str__(self):
        return "ComfortXProperty"

    class Meta:
        verbose_name_plural = 'ComfortsXProperty'


class RentalDate(models.Model):
    property = models.ForeignKey(Property, on_delete=models.DO_NOTHING)
    booking = models.ForeignKey(Booking, null=True, blank=True, on_delete=models.DO_NOTHING)
    date = models.DateField()

    def __str__(self):
        return "RentalDate"

    class Meta:
        verbose_name_plural = 'RentalDates'
