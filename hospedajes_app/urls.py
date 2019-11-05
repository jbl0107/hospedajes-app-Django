from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from hospedajes_app import views

app_name = 'hospedajes_app'

urlpatterns = [
    path('', views.index, name='index'),
    # url(r'^alta_salon/$', login_required(ingresar_salon), name='altaSalon'),
    path('new_property/', views.property_form, name='propertyForm'),
    path('property/<int:property_id>', views.view_property, name='property'),
    path('new_city', views.city_form, name='cityForm'),


    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#  static nos va a permitir generar una nueva url en base a nuestro media url y media root.