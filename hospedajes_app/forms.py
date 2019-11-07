from django import forms
from .models import Property, City


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ('title', 'description', 'pax', 'daily_import', 'image', 'city')


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ('name',)


