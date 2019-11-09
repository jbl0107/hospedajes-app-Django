from django import forms
from .models import Property, City, RentalDate, Feature, Comfort


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ('title', 'description', 'pax', 'daily_import', 'image', 'city', 'features', )


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ('name',)


class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ('name',)


class ComfortForm(forms.ModelForm):
    class Meta:
        model = Comfort
        fields = ('name', 'className',)
