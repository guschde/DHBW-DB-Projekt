from django import forms
from datetime import datetime
from datetime import date
from . import models

#   pro Model eine Klasse in forms , bei fields keine Primary Keys ausser wenn wir sie selber definieren
class CreatePersonal (forms.ModelForm):
    class Meta:
        model = models.Personal
        fields = ['Vorname', 'Name', 'Führungsqualifikation', 'Bereitschaft', 'Qualifikation']

class CreateAnsprechpartner (forms.ModelForm):
    class Meta:
        model = models.Ansprechpartner
        fields = ['Einsatz_ID', 'Vorname', 'Name', 'Geschlecht', 'Datum', 'Infotext', 'Telefonnummer']
        
class CreateEinsatz (forms.ModelForm):
    class Meta:
        model = models.Einsatz
        fields = ['Personal_ID', 'Einsatzdatum', 'Einsatzinfo']
        
class CreateDienst (forms.ModelForm):
    class Meta:
        model = models.Dienst
        fields = ['Einsatz_ID', 'Personal_ID', 'Dienstdatum', 'Einsatzbeginnzeit', 'Einsatzendezeit', 'Funkrufname']
        
class CreateRettungsmittel (forms.ModelForm):
    class Meta:
        model = models.Rettungsmittel
        fields = ['Bezeichnung']
        
class CreatePatient (forms.ModelForm):
    class Meta:
        model = models.Patient
        fields = ['Vorname', 'Name', 'Alter', 'Geschlecht']
        
class CreateVorfall (forms.ModelForm):
    class Meta:
        model = models.Vorfall
        fields = ['Einsatz', 'Einsatzdatum', 'Einsatzort', 'Einsatzbeginn',
                  'Einsatzende', 'Triagekategorie', 'Retter', 'Dienst', 'Patient']

