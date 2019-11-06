from django import forms
from .models import Property, City


class PostForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ('title', 'description', 'pax', 'daily_import', 'image',)


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ('name',)
