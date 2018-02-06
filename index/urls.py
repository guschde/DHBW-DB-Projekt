from django.urls import path

from . import views


app_name = 'index'
urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),
    path('einsatz/', views.Einsatz.as_view(), name='einsatz'),
    path('vorfall/', views.Vorfall.as_view(), name='vorfall'),
    path('helfer/', views.Helfer.as_view(), name='helfer'),
    path('ansprechpartner/', views.Ansprechpartner.as_view(), name='ansprechpartner'),

]

