from datetime import timezone

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from hospedaje.settings import MEDIA_ROOT
from hospedajes_app.forms import CityForm, PropertyForm
from hospedajes_app.models import Property, City


def index(request):
    properties = Property.objects.all()
    return render(request, 'hospedajes_app/index.html', {'properties': properties})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
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
            return HttpResponseRedirect(reverse('hospedajes_app:propertyForm'))
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
        return HttpResponseRedirect(reverse('hospedajes_app:cityForm'))
    else:
        form = CityForm()

    return render(request, 'hospedajes_app/forms/city_form.html', {'cities': cities, 'form': form})


def view_property(request, property_id):
    property = Property.objects.get(id=property_id)
    return render(request, 'hospedajes_app/view_property.html', {'property': property})


@login_required
def secret_page(request):
    return render(request, 'hospedajes_app/secret_page.html')


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'hospedajes_app/secret_page.html'


"""
@login_required
@permission_required('hospedajes_app.propertyForm', login_url='login')
def property_form(request):
    error = ''
    cities = City.objects.all()
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        pax = request.POST['pax']
        daily_import = request.POST['daily']
        image = request.FILES['propertyImage']
        fk_city = request.POST['city']
        # fk_user = request.POST['fk_user']

        city = City.objects.get(id=fk_city)

        if title is not None:
            property = Property(title=title, pax=pax, description=description, daily_import=daily_import, city=city,
                                image=image, )
            property.save()
        else:
            error = 'La propiedad debe tener nombre'

    return render(request, 'hospedajes_app/forms/property_form.html', {'error': error, 'cities': cities})


def save_file(file, path=''):
    filename = file._get_name()
    fd = open('%s/%s' % (MEDIA_ROOT, str(path) + str(filename)), 'wb')
    for chunk in file.chunks():
        fd.write(chunk)
    fd.close()
"""

"""
@login_required
@permission_required('hospedajes_app.propertyForm', login_url='login')
def city_form(request):
    error = ''
    cities = City.objects.all()

    if request.method == 'POST':
        name = request.POST['name']

        if name is not None:
            city = City(name=name)
            city.save()
        else:
            error = 'La ciudad debe tener nombre'

    return render(request, 'hospedajes_app/forms/city_form.html', {'cities': cities, 'error': error})
"""