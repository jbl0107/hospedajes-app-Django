from django.db import models
from django.forms import forms

# Create your models here.
class User(models.Model):
    username: models.CharField(null=False)
    password: models.CharField(max_length=100)
    email: models.EmailField(null=False)
    name: models.CharField(null=False)
    surname: models.CharField(null=False)

    def __init__(self, username, password, email, name, surname):
        self.username = username
        self.password = password
        self.email = email
        self.name = name
        self.surname = surname

    def __str__(self):
        return self.name + " " + self.surname


class City(models.Model):
    name: models.CharField(null=False)
    country: models.CharField(null=False)

    def __init__(self, name, country):
        self.name = name
        self.country = country
    
    def __str__(self):
        return self.name + ", " + self.country


class Booking(models.Model):
    name: models.CharField(null=False)
    surname: models.CharField(null=False)
    email: models.EmailField(null=False)
    dni: models.IntegerField(max_length=8, null=False)
    total: models.FloatField(default = 0,null=False)


    def __init__(self, name, surname, email, dni):
        self.name = name
        self.surname = surname
        self.email = email
        self.dni = dni

    def __str__(self):
        return self.name + ", " + self.surname + ", " + self.email + ", " + self.dni + "."



class Property(models.Model):
    pax: models.IntegerField(null=False)
    title: models.CharField(null=False)
    description: models.CharField(null=False)
    image: models.ImageField(null=False)
    daily_import: models.FloatField(null=False)
    fk_user: models.ForeignKey(User, null=False, on_delete=models.DO_NOTHING)
    fk_city: models.ForeignKey(City, null=False, on_delete=models.DO_NOTHING)
    
    def __init__(self, title, description, pax, daily_import, image, fk_user, fk_city):
        self.title = title
        self.description = description
        self.pax = pax
        self.daily_import = daily_import
        self.image = image
        self.fk_user = fk_user
        self.fk_city = fk_city

    def __str__(self):
        return self.title + ", " + self.description + ", " + self.pax + ", " + self.daily_import + "."

class Rental_Date(models.Model):
    fk_property: models.ForeignKey(Property,null=False, on_delete=models.DO_NOTHING)
    fk_booking: models.ForeignKey(Booking,null=True, blank=True, on_delete=models.DO_NOTHING)
    date: models.DateField(null=False)

    def __init__(self,fk_property, fk_booking, date):
        self.fk_property = fk_property
        self.fk_booking = fk_booking
        self.date = date