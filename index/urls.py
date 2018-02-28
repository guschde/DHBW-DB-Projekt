from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'index'
urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),
    path('einsatz/', views.EinsatzView.as_view(), name='einsatz'),
    path('einsatz/add', views.EinsatzCreate.as_view(), name='einsatz-create'),
    path('einsatz/upd/<int:pk>/', views.EinsatzUpdate.as_view(), name='einsatz-update'),
    path('einsatz/del/<int:pk>/', views.EinsatzDelete.as_view(), name='einsatz-delete'),
    path('dienst/', views.DienstView.as_view(), name='dienst'),
    path('dienst/add', views.DienstCreate.as_view(), name='dienst-create'),
    path('dienst/upd/<int:pk>/', views.DienstUpdate.as_view(), name='dienst-update'),
    path('dienst/del/<int:pk>/', views.DienstDelete.as_view(), name='dienst-delete'),
    path('rettungsmittel/', views.RettungsmittelView.as_view(), name='rettungsmittel'),
    path('rettungsmittel/add', views.RettungsmittelCreate.as_view(), name='rettungsmittel-create'),
    path('rettungsmittel/upd/<int:pk>/', views.RettungsmittelUpdate.as_view(), name='rettungsmittel-update'),
    path('rettungsmittel/del/<int:pk>/', views.RettungsmittelDelete.as_view(), name='rettungsmittel-delete'),
    path('patient/', views.PatientView.as_view(), name='patient'),
    path('patient/add', views.PatientCreate.as_view(), name='patient-create'),
    path('patient/upd/<int:pk>/', views.PatientUpdate.as_view(), name='patient-update'),
    path('patient/del/<int:pk>/', views.PatientDelete.as_view(), name='patient-delete'),
    path('vorfall/', views.VorfallView.as_view(), name='vorfall'),
    path('vorfall/add', views.VorfallCreate.as_view(), name='vorfall-create'),
    path('vorfall/upd/<int:pk>/', views.VorfallUpdate.as_view(), name='vorfall-update'),
    path('vorfall/del/<int:pk>/', views.VorfallDelete.as_view(), name='vorfall-delete'),
    path('personal/', views.PersonalView.as_view(), name='personal'),
    path('personal/add', views.PersonalCreate.as_view(), name='personal-create'),
    path('personal/upd/<int:pk>/', views.PersonalUpdate.as_view(), name='personal-update'),
    path('personal/del/<int:pk>/', views.PersonalDelete.as_view(), name='personal-delete'),
    path('ansprechpartner/add', views.AnsprechpartnerCreate.as_view(), name='ansprechpartner-create'),
    path('ansprechpartner/upd/<int:pk>/', views.AnsprechpartnerUpdate.as_view(), name='ansprechpartner-update'),
    path('ansprechpartner/del/<int:pk>/', views.AnsprechpartnerDelete.as_view(), name='ansprechpartner-delete'),
    path('ansprechpartner/', views.AnsprechpartnerView.as_view(), name='ansprechpartner'),
]

