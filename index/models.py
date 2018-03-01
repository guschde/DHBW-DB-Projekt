from django.db import models
from datetime import datetime
from datetime import date
from django.urls import reverse

class Personal(models.Model):
    Vorname = models.CharField(max_length=50)
    Name = models.CharField(max_length=50)
    Führungsqualifikation = models.CharField(max_length=50)
    Bereitschaft = models.CharField(max_length=20)
    Qualifikation = models.CharField(max_length=20)

#mehr als das muss in der models.py nicht geändert werden
    def get_absolute_url(self):
        if self == self:
            return ('/personal/')
#mehr is es echt nicht xD
    def __str__(self):
        return self.Vorname+' '+self.Name

class Einsatz(models.Model):
    Personal_ID = models.ForeignKey(Personal, on_delete=models.CASCADE)
    Einsatzdatum = models.DateField('Einsatzdatum', default=date.today)
    Einsatzinfo = models.CharField('Einsatzinfo', max_length=254, default='Einsatzinfo')    
    
    def get_absolute_url(self):
        if self == self:
            return ('/einsatz/')

    def __str__(self):
        return self.Einsatzinfo


class Dienst(models.Model):
    Dienstdatum = models.DateField('Dienstdatum', default=date.today)
    Personal_ID = models.ForeignKey(Personal, default="Gruppenführer", on_delete=models.DO_NOTHING)
    Einsatz_ID = models.ForeignKey(Einsatz, default="Einsatz", on_delete=models.DO_NOTHING)
    Einsatzbeginnzeit = models.TimeField('Einsatzbeginn')
    Telefonnummer = models.CharField(max_length=20)
    Einsatzendezeit = models.TimeField('Einsatzende',  blank=True, null=True)
    
    def get_absolute_url(self):
        if self == self:
            return ('/dienst/')

    def __str__(self):
        return str(self.Personal_ID)


class Ansprechpartner(models.Model):
    sex = (('w', 'W'), ('m', 'M'))
    Einsatz_ID = models.ForeignKey(Einsatz, default='Einsatz', on_delete=models.CASCADE)
    Datum = models.DateField('Datum')
    Telefonnummer = models.CharField(max_length=20)
    Geschlecht = models.CharField(max_length=1, choices=sex, default='W')
    Vorname = models.CharField(max_length=20)
    Name = models.CharField(max_length=20)
    Infotext = models.CharField(max_length=100)

    def get_absolute_url(self):
        if self == self:
            return ('/ansprechpartner/')

    def __str__(self):
        return self.Vorname+' '+self.Name

class Rettungsmittel(models.Model):
    Bezeichnung = models.CharField(max_length=30)
   
    def get_absolute_url(self):
        if self == self:
            return ('/rettungsmittel/')

    def __str__(self):
        return self.Bezeichnung

class Patient(models.Model):
    sex = (('w', 'W'), ('m', 'M'))
    Vorname = models.CharField(max_length=20, default='Patientin')
    Name = models.CharField(max_length=20, default='Musterfrau')
    Alter = models.IntegerField(default='1')
    Geschlecht = models.CharField(max_length=1, choices=sex, default='W')
    def __str__(self):
        return self.Vorname+' '+self.Name
    
    
    def get_absolute_url(self):
        if self == self:
            return ('/patient/')



class Vorfall(models.Model):
    triag = (('leichte Verletzungen', 'LEICHTE VERLETZUNGEN'),
        ('mittlere Verletzungen', 'MITTLERE VERLETZUNGEN'),
        ('schwere Verletzungen', 'SCHWERE VERLETZUNGEN'),
    )
    Einsatz = models.ForeignKey(Einsatz, default='1', on_delete=models.CASCADE)
    Einsatzdatum = models.DateField('Einsatzdatum', default=date.today)
    Einsatzort = models.CharField(max_length=50, default='Heidenheim', editable=True)
    Einsatzbeginn = models.TimeField('Einsatzbeginn', default=datetime.now)
    Einsatzende = models.TimeField('Einsatzende', blank=True, null=True)
    Triagekategorie = models.CharField('Triagekategorie', max_length=21, default='LEICHTE VERLETZUNGEN', choices=triag)
    Dienst = models.ManyToManyField(Dienst)
    Retter = models.ManyToManyField(Rettungsmittel)
    Patient = models.ManyToManyField(Patient, blank=True, null=True)

    def __str__(self):
        return self.Einsatzort

    def get_absolute_url(self):
        if self == self:
            return ('/vorfall/')







