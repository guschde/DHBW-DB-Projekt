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

