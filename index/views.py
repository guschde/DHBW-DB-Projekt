# Create your views here.
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse
from .models import Personal, Einsatz, Ansprechpartner, Vorfall, Dienst, Rettungsmittel, Patient


class IndexView(generic.ListView):
    template_name = 'index/index.html'
    context_object_name = 'listoflists'

    def get_queryset(self):
        listoflists=[]
        patientlist = Patient.objects.all()
        listoflists.append(patientlist)

        retterlist = Rettungsmittel.objects.all()
        listoflists.append(retterlist)

        vorfalllist = Vorfall.objects.all()
        listoflists.append(vorfalllist)

        einsatzlist = Einsatz.objects.all()
        listoflists.append(einsatzlist)

        dienstlist = Dienst.objects.all()
        listoflists.append(dienstlist)

        personallist=Personal.objects.all()
        listoflists.append(personallist)

        ansprechparterlist = Ansprechpartner.objects.all()
        listoflists.append(ansprechparterlist)

        return listoflists


class EinsatzView(generic.ListView):
    template_name = 'index/einsatz.html'
    context_object_name = 'liste'
    def get_queryset(self):
        return Einsatz.objects.all()

class DienstView(generic.ListView):
    template_name = 'index/dienst.html'
    context_object_name = 'liste'
    def get_queryset(self):
        return Dienst.objects.all()

class RettungsmittelView(generic.ListView):
    template_name = 'index/rettungsmittel.html'
    context_object_name = 'liste'
    def get_queryset(self):
        return Rettungsmittel.objects.all()

class PatientView(generic.ListView):
    template_name = 'index/patient.html'
    context_object_name = 'liste'
    def get_queryset(self):
        return Patient.objects.all()

class PersonalView(generic.ListView):
    template_name = 'index/personal.html'
    context_object_name = 'liste'
    def get_queryset(self):
        return Personal.objects.all()


class VorfallView(generic.ListView):
    template_name = 'index/vorfall.html'
    context_object_name = 'liste'
    def get_queryset(self):
        return Vorfall.objects.all()


class AnsprechpartnerView(generic.ListView):
    template_name = 'index/ansprechpartner.html'
    context_object_name = 'liste'
    def get_queryset(self):
        return Ansprechpartner.objects.all()
