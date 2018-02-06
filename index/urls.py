from django.urls import path

from . import views


app_name = 'index'
urlpatterns = [
   
    path('', views.IndexView.as_view(), name='index'),
    path('formular/', views.FormView.as_view(), name='formular'),

]

