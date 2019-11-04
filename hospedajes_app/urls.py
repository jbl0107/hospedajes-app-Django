from django.urls import include, path

from hospedajes_app import views
from hospedajes_app.views import property_form, ficha_property, city_form

urlpatterns = [
    path('', views.index, name='index'),

    # url(r'^alta_salon/$', login_required(ingresar_salon), name='altaSalon'),
    path('new_property/', property_form, name='propertyForm'),
    path('property/<int:property_id>', ficha_property, name='property'),
    path('new_city', city_form, name='cityForm'),


    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

]
