from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from hospedajes_app import views

app_name = 'hospedajes_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('new_property/', views.property_form, name='propertyForm'),
    path('new_tipoAula/', views.tipoAula_form, name='tipoAulaForm'),
    path('new_caracteristica/', views.caracteristica_form, name='caracteristicaForm'),
    path('new_capacidad/', views.capacidad_form, name='capacidadForm'),
    path('property/<int:property_id>/', views.view_property, name='property'),
    path('my_bookings/<int:property_id>/', views.bookingByProperty, name='bookingByProperty'),
    path('my_bookings/', views.my_bookings, name='myBookings'),

    # path('secret2/', views.SecretPage.as_view(), name='secret2'),

    # url(r'^alta_salon/$', login_required(ingresar_salon), name='altaSalon'),

]