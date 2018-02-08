from django.db import models
from datetime import datetime
from datetime import date

class Personal(models.Model):
	Vorname = models.CharField(max_length=50)
	Name = models.CharField(max_length=50)
	Führungsqualifikation = models.CharField(max_length=50)
	Bereitschaft = models.CharField(max_length=20)
	Qualifikation = models.CharField(max_length=20)
	def __str__(self):
		return self.Vorname

class Einsatz(models.Model):
    Personal_ID = models.ForeignKey(Personal, on_delete=models.CASCADE)
    Einsatzdatum = models.DateField('Einsatzdatum', default=date.today)
    Einsatzinfo = models.CharField('Einsatzinfo', max_length=254, default='Einsatzinfo')
    def __str__(self):
        return self.Einsatzinfo

class Dienst(models.Model):
    Dienstdatum = models.DateField('Dienstdatum', default=date.today)
    Personal_ID = models.ForeignKey(Personal, default="Gruppenführer", on_delete=models.DO_NOTHING)
    Einsatz_ID = models.ForeignKey(Einsatz, default="Einsatzleitung", on_delete=models.DO_NOTHING)
    Einsatzbeginnzeit = models.TimeField('Einsatzbeginn')
    Telefonnummer = models.CharField(max_length=20)
    Einsatzendezeit = models.TimeField('Einsatzende')

class Ansprechpartner(models.Model):
	Einsatz_ID = models.ForeignKey(Einsatz, on_delete=models.CASCADE)
	Datum = models.DateField('Datum')
	Telefonnummer = models.CharField(max_length=20)
	Geschlecht = models.CharField(max_length=1)
	Vorname = models.CharField(max_length=20)
	Name = models.CharField(max_length=20)
	Infotext = models.CharField(max_length=100)
	def __str__(self):
		return self.Name

class Rettungsmittel(models.Model):
	Bezeichnung = models.CharField(max_length=30)
	def __str__(self):
		return self.Bezeichnung

class Patient(models.Model):
	Vorname = models.CharField(max_length=20, default='Herbert')
	Name = models.CharField(max_length=20, default='Meier')
	Alter = models.IntegerField()
	Geschlecht = models.CharField(max_length=1)
	Triagekategorie = models.IntegerField()
	Diagnose = models.CharField(max_length=200)
	Patient_Einsatzdatum = models.DateField('Behandlungsdatum')
	def __str__(self):
		return self.Vorname+' '+self.Name

class Vorfall(models.Model):
	Einsatz = models.ForeignKey(Einsatz, default='1', on_delete=models.CASCADE)
	Einsatzdatum = models.DateField('Einsatzdatum', default=date.today)
	Einsatzort = models.CharField(max_length = 50, default='Heidenheim', editable=True)
	Einsatzbeginn = models.TimeField('Einsatzbeginn', default=datetime.now)
	Einsatzende = models.TimeField('Einsatzende')
	Dienst = models.ManyToManyField(Dienst)
	Patienten = models.ManyToManyField(Patient)
	Retter = models.ManyToManyField(Rettungsmittel)
	def __str__(self):
		return self.Einsatzort








