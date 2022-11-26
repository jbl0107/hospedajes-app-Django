from django import forms
from .models import Property, TipoAula, RentalDate, Caracteristica, Comfort, Profile


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ('title', 'description', 'pax', 'daily_import', 'image', 'tipoAula', 'caracteristicas', 'user',)


class TipoAulaForm(forms.ModelForm):
    class Meta:
        model = TipoAula
        fields = ('name',)


class CaracteristicaForm(forms.ModelForm):
    class Meta:
        model = Caracteristica
        fields = ('name',)


class ComfortForm(forms.ModelForm):
    class Meta:
        model = Comfort
        fields = ('name', 'className',)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'surname', 'email',)