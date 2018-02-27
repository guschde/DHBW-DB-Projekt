from django.urls import path
from django.conf.urls import url
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
    path('personal/add', views.PersonalCreate.as_view(), name='personal-create'),
    path('personal/upd/<int:pk>/', views.PersonalUpdate.as_view(), name='personal-update'),
    path('personal/del/<int:pk>/', views.PersonalDelete.as_view(), name='personal-delete'),
    path('ansprechpartner/', views.AnsprechpartnerView.as_view(), name='ansprechpartner'),
    path('ansprechpartner/add', views.AnsprechpartnerCreate.as_view(), name='ansprechpartner-create'),
    path('ansprechpartner/upd/<int:pk>/', views.AnsprechpartnerUpdate.as_view(), name='ansprechpartner-update'),
    path('ansprechpartner/del/<int:pk>/', views.AnsprechpartnerDelete.as_view(), name='ansprechpartner-delete'),

]

