from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from hospedajes_app import views

app_name = 'hospedajes_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('new_property/', views.property_form, name='propertyForm'),
    path('new_city/', views.city_form, name='cityForm'),
    path('new_feature/', views.feature_form, name='featureForm'),
    path('new_comfort/', views.comfort_form, name='comfortForm'),
    path('property/<int:property_id>/', views.view_property, name='property'),
    path('secret/', views.secret_page, name='secret'),
    path('secret2/', views.SecretPage.as_view(), name='secret2'),

    # url(r'^alta_salon/$', login_required(ingresar_salon), name='altaSalon'),

]