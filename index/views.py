# Create your views here.
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse


#def index(request):
#    return HttpResponse("huhu i bims der index")
    
class IndexView(generic.ListView):    
    template_name = 'index/index.html'
    context_object_name = 'liste'

    def get_queryset(self):
         liste = ['huhu', 'haha', 'es wird langsam', 'wärmer', 'wärmer', 'heisser', 'Jackpot', 'ignore ist bestes gnore']
         return liste


class FormView(generic.ListView):    
    template_name = 'index/formular.html'
    context_object_name = 'liste'

    def get_queryset(self):
         liste = ['huhu', 'haha', 'es wird langsam', 'wärmer', 'wärmer', 'heisser', 'Jackpot']
         return liste

class Einsatz(generic.ListView):
    template_name = 'index/einsatz.html'
    context_object_name = 'liste'

    def get_queryset(self):
         liste = ['huhu', 'haha', 'es wird langsam', 'wärmer', 'wärmer', 'heisser', 'Jackpot']
         return liste

class Helfer(generic.ListView):
    template_name = 'index/helfer.html'
    context_object_name = 'liste'

    def get_queryset(self):
         liste = ['huhu', 'haha', 'es wird langsam', 'wärmer', 'wärmer', 'heisser', 'Jackpot']
         return liste


class Vorfall(generic.ListView):
    template_name = 'index/vorfall.html'
    context_object_name = 'liste'

    def get_queryset(self):
         liste = ['huhu', 'haha', 'es wird langsam', 'wärmer', 'wärmer', 'heisser', 'Jackpot']
         return liste

class Ansprechpartner(generic.ListView):
    template_name = 'index/ansprechpartner.html'
    context_object_name = 'liste'

    def get_queryset(self):
         liste = ['huhu', 'haha', 'es wird langsam', 'wärmer', 'wärmer', 'heisser', 'Jackpot']
         return liste