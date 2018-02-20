from django.urls import path
from . import views


app_name = 'index'
urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),
    path('einsatz/', views.EinsatzView.as_view(), name='einsatz'),
    path('dienst/', views.DienstView.as_view(), name='dienst'),
    path('rettungsmittel/', views.RettungsmittelView.as_view(), name='rettungsmittel'),
    path('patient/', views.PatientView.as_view(), name='patient'),
    path('vorfall/', views.VorfallView.as_view(), name='vorfall'),
    path('personal/', views.PersonalView.as_view(), name='personal'),
    path('ansprechpartner/', views.AnsprechpartnerView.as_view(), name='ansprechpartner'),

]

