from datetime import timezone

from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from hospedajes_app.forms import CityForm, PropertyForm, FeatureForm, ComfortForm
from hospedajes_app.models import Property, City, RentalDate, Feature, Comfort, ComfortXProperty, Booking, Profile


def index(request):
    properties = Property.objects.all()
    return render(request, 'hospedajes_app/index.html', {'properties': properties})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return redirect('../')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {
        'form': form
    })


@login_required
@permission_required('hospedajes_app.propertyForm', login_url='login')
def property_form(request):
    cities = City.objects.all()

    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            new_property = form.save()
            # return HttpResponseRedirect(reverse('hospedajes_app:propertyForm'))
    else:
        form = PropertyForm()

    return render(request, 'hospedajes_app/forms/property_form.html', {'cities': cities, 'form': form})


@login_required
@permission_required('hospedajes_app.propertyForm', login_url='login')
def city_form(request):
    cities = City.objects.all()

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            new_city = form.save()
            # return HttpResponseRedirect(reverse('hospedajes_app:cityForm'))
    else:
        form = CityForm()

    return render(request, 'hospedajes_app/forms/city_form.html', {'cities': cities, 'form': form})


@login_required
@permission_required('hospedajes_app.propertyForm', login_url='login')
def feature_form(request):
    features = Feature.objects.all()

    if request.method == 'POST':
        form = FeatureForm(request.POST)
        if form.is_valid():
            new_feature = form.save()
            # return HttpResponseRedirect(reverse('hospedajes_app:featureForm'))
    else:
        form = FeatureForm()

    return render(request, 'hospedajes_app/forms/feature_form.html', {'features': features, 'form': form})


@login_required
@permission_required('hospedajes_app.propertyForm', login_url='login')
def comfort_form(request):
    comforts = Comfort.objects.all()

    if request.method == 'POST':
        form = ComfortForm(request.POST)
        if form.is_valid():
            new_comfort = form.save()
            # return HttpResponseRedirect(reverse('hospedajes_app:comfortForm'))
    else:
        form = ComfortForm()

    return render(request, 'hospedajes_app/forms/comfort_form.html', {'comforts': comforts, 'form': form})


def view_property(request, property_id):
    error = ''
    dateList = ''
    property = Property.objects.get(id=property_id)
    rentalDates = RentalDate.objects.filter(property_id=property_id, booking_id=None)
    comforts = ComfortXProperty.objects.filter(property_id=property_id)
    features = Feature.objects.filter(property__pk=property_id)

    for d in rentalDates:
        dateList += str(d.date)

    if request.method == 'POST':
        datesSelected = request.POST['dates']
        total = request.POST['total']
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        dni = request.POST['dni']

        if datesSelected and name and surname and email and dni:
            datesSelected = datesSelected.split(", ")
            total = total[1:]

            try:
                profile = Profile.objects.get(dni=dni)
            except Profile.DoesNotExist:
                profile = Profile(name=name, surname=surname, email=email, dni=dni)
                profile.save()

            booking = Booking(profile=profile, total=total)
            booking.save()

            for d in rentalDates:
                if str(d.date) in datesSelected:
                    d.booking = booking
                    d.save(update_fields=['booking'])

            return HttpResponseRedirect(reverse('hospedajes_app:myBookings'))
        else:
            error = 'Debe completar todos los campos para confirmar la reserva!'

    return render(request, 'hospedajes_app/view_property.html', {'property': property, 'comforts': comforts, 'features': features, 'dateList': dateList})


@login_required
def my_bookings(request):
    return render(request, 'hospedajes_app/my_bookings.html')


# class SecretPage(LoginRequiredMixin, TemplateView):
#    template_name = 'hospedajes_app/secret_page.html'

