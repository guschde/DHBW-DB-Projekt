# Create your views here.
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.utils import timezone
from django.http import HttpResponse
from .models import Personal, Einsatz, Ansprechpartner, Vorfall, Dienst, Rettungsmittel, Patient
from django.urls import reverse_lazy
from . import forms


class IndexView(generic.ListView):
    template_name = 'index/index.html'
    context_object_name = 'listoflists'

    def get_queryset(self):
        listoflists = []
        patientlist = list(Patient.objects.all())
        patientlist.reverse()
        listoflists.append(patientlist[:5])

        retterlist = list(Rettungsmittel.objects.all())
        retterlist.reverse()
        listoflists.append(retterlist[:5])

        vorfalllist = list(Vorfall.objects.all())
        vorfalllist.reverse()
        listoflists.append(vorfalllist[:5])

        einsatzlist = list(Einsatz.objects.all())
        einsatzlist.reverse()
        listoflists.append(einsatzlist[:5])

        dienstlist = list(Dienst.objects.all())
        dienstlist.reverse()
        listoflists.append(dienstlist[:5])

        personallist = list(Personal.objects.all())
        personallist.reverse()
        listoflists.append(personallist[:5])

        ansprechparterlist = list(Ansprechpartner.objects.all())
        ansprechparterlist.reverse()
        listoflists.append(ansprechparterlist[:5])


        return listoflists


class EinsatzView(generic.ListView):
    template_name = 'index/einsatz.html'
    context_object_name = 'liste'
    def get_queryset(self):
        liste = list(Einsatz.objects.all())
        liste.reverse()
        return liste
    

class EinsatzCreate(generic.CreateView):
    template_name = 'index/einsatz_add.html'
    context_object_name = 'form'
    model = Einsatz
    fields = ['Personal_ID', 'Einsatzdatum', 'Einsatzinfo']


class EinsatzUpdate(generic.UpdateView):
    model = Einsatz
    fields = ['Personal_ID', 'Einsatzdatum', 'Einsatzinfo']
    template_name_suffix = '_update'


class EinsatzDelete(generic.DeleteView):
    model = Einsatz
    success_url = ('/einsatz/')
    

class DienstView(generic.ListView):
    template_name = 'index/dienst.html'
    context_object_name = 'liste'

    def get_queryset(self):
        liste = list(Dienst.objects.all())
        liste.reverse()
        return liste


class DienstCreate(generic.CreateView):
    template_name = 'index/dienst_add.html'
    context_object_name = 'form'
    model = Dienst
    fields = ['Personal_ID', 'Einsatz_ID', 'Einsatzbeginnzeit', 'Einsatzendezeit',  'Funkrufname']


class DienstUpdate(generic.UpdateView):
    model = Dienst
    fields = ['Personal_ID', 'Einsatz_ID', 'Einsatzbeginnzeit', 'Einsatzendezeit', 'Funkrufname']
    template_name_suffix = '_update'


class DienstDelete(generic.DeleteView):
    model = Dienst
    success_url = ('/dienst/')
    

class RettungsmittelView(generic.ListView):
    template_name = 'index/rettungsmittel.html'
    context_object_name = 'liste'

    def get_queryset(self):
        liste = list(Rettungsmittel.objects.all())
        liste.reverse()
        return liste
    

class RettungsmittelCreate(generic.CreateView):
    template_name = 'index/rettungsmittel_add.html'
    context_object_name = 'form'
    model = Rettungsmittel
    fields = ['Bezeichnung']


class RettungsmittelUpdate(generic.UpdateView):
    model = Rettungsmittel
    fields = ['Bezeichnung']
    template_name_suffix = '_update'


class RettungsmittelDelete(generic.DeleteView):
    model = Rettungsmittel
    success_url = ('/rettungsmittel/')


class PatientView(generic.ListView):
    template_name = 'index/patient.html'
    context_object_name = 'liste'
    def get_queryset(self):
        liste = list(Patient.objects.all())
        liste.reverse()
        return liste


class PatientCreate(generic.CreateView):
    template_name = 'index/patient_add.html'
    context_object_name = 'form'
    model = Patient
    fields = ['Vorname', 'Name', 'Alter', 'Geschlecht']

class PatientUpdate(generic.UpdateView):
    model = Patient
    fields = ['Vorname', 'Name', 'Alter', 'Geschlecht']
    template_name_suffix = '_update'

class PatientDelete(generic.DeleteView):
    model = Patient
    success_url = ('/patient/')
    

class PersonalView(generic.ListView):
    template_name = 'index/personal.html'
    context_object_name = 'liste'

    def get_queryset(self):
        liste = list(Personal.objects.all())
        liste.reverse()
        return liste

#Neu Objekt erstellen ändern und löschen
class PersonalCreate(generic.CreateView):
    template_name = 'index/personal_add.html'
    context_object_name = 'form'
    model = Personal
    fields = ['Vorname', 'Name', 'Führungsqualifikation', 'Bereitschaft', 'Qualifikation']

class PersonalUpdate(generic.UpdateView):
    model = Personal
    fields = ['Vorname', 'Name', 'Führungsqualifikation', 'Bereitschaft', 'Qualifikation']
    template_name_suffix = '_update'

class PersonalDelete(generic.DeleteView):
    model = Personal
    success_url = ('/personal/')
#das wars auch schon noch zu ändern (forms.py, urls.py, templates erstellen und anpassen)



class VorfallView(generic.ListView):
    template_name = 'index/vorfall.html'
    context_object_name = 'liste'

    def get_queryset(self):
        liste = list(Vorfall.objects.all())
        liste.reverse()
        return liste


class VorfallDetailView(generic.DetailView):

    model = Vorfall

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class VorfallCreate(generic.CreateView):
    template_name = 'index/vorfall_add.html'
    context_object_name = 'form'
    model = Vorfall
    fields = ['Einsatz', 'Einsatzort', 'Einsatzbeginn',
                  'Einsatzende', 'Triagekategorie', 'Retter', 'Dienst', 'Patient']


class VorfallUpdate(generic.UpdateView):
    model = Vorfall
    fields = ['Einsatz', 'Einsatzort', 'Einsatzbeginn',
                  'Einsatzende', 'Triagekategorie', 'Retter', 'Dienst', 'Patient']
    template_name_suffix = '_update'

class VorfallDelete(generic.DeleteView):
    model = Vorfall
    success_url = ('/vorfall/')


#    Ansprechpartner Block
class AnsprechpartnerView(generic.ListView):
    template_name = 'index/ansprechpartner.html'
    context_object_name = 'liste'

    def get_queryset(self):
        liste = list(Ansprechpartner.objects.all())
        liste.reverse()
        return liste

#Neu Objekt erstellen ändern und löschen
class AnsprechpartnerCreate(generic.CreateView):
    template_name = 'index/ansprechpartner_add.html'
    context_object_name = 'form'
    model = Ansprechpartner
    fields = ['Einsatz_ID', 'Vorname', 'Name', 'Geschlecht', 'Infotext', 'Telefonnummer']

class AnsprechpartnerUpdate(generic.UpdateView):
    model = Ansprechpartner
    fields = ['Einsatz_ID', 'Vorname', 'Name', 'Geschlecht', 'Infotext', 'Telefonnummer']
    template_name_suffix = '_update'

class AnsprechpartnerDelete(generic.DeleteView):
    model = Ansprechpartner
    success_url = ('/ansprechpartner/')
#das wars auch schon noch zu ändern (forms.py, urls.py, templates erstellen und anpassen)