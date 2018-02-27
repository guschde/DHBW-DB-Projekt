from django.db import models
from datetime import datetime
from datetime import date

class Personal(models.Model):
	Personal_ID = models.CharField(max_length=10, primary_key=True)
	Vorname = models.CharField(max_length=50)
	Name = models.CharField(max_length=50)
	Führungsqualifikation = models.CharField(max_length=50)
	Bereitschaft = models.CharField(max_length=20)
	Qualifikation = models.CharField(max_length=20)
	def __str__(self):
		return self.Vorname

class Einsatz(models.Model):
    Personal_ID = models.ForeignKey(Personal, on_delete=models.CASCADE)
    Einsatzdatum = models.DateField('Einsatzdatum', default=date.today, primary_key=True)
    Einsatzinfo = models.CharField('Einsatzinfo', max_length=254, default='Einsatzinfo')
    def __str__(self):
        return str(self.id)

class Dienst(models.Model):
    Dienstdatum = models.DateField('Dienstdatum', default=date.today, primary_key=True)
    Personal_ID = models.ForeignKey(Personal, default="Gruppenführer", on_delete=models.DO_NOTHING)
    Einsatz_ID = models.ForeignKey(Einsatz, default="Einsatz", on_delete=models.DO_NOTHING)
    Einsatzbeginnzeit = models.TimeField('Einsatzbeginn')
    Telefonnummer = models.CharField(max_length=20)
    Einsatzendezeit = models.TimeField('Einsatzende')

class Ansprechpartner(models.Model):
	ID-Ansprechpartner = models.CharField(max_length=10, primary_key=True)
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
	Funkrufname = models.CharField(max_length=20, primary_key=True)
	Bezeichnung = models.CharField(max_length=30)
	def __str__(self):
		return self.Bezeichnung

class Patient(models.Model):
	ID_Patient = models.CharField(max_length=10, primary_key=True)
	Vorname = models.CharField(max_length=20, default='Herbert')
	Name = models.CharField(max_length=20, default='Meier')
	Alter = models.IntegerField()
	Geschlecht = models.CharField(max_length=1)
	def __str__(self):
		return self.Vorname+' '+self.Name

class Vorfall(models.Model):
	Vorfall_ID = models.CharField(max_length=10, primary_key=True)
	Einsatz = models.ForeignKey(Einsatz, default='1', on_delete=models.CASCADE)
	Einsatzdatum = models.DateField('Einsatzdatum', default=date.today)
	Einsatzort = models.CharField(max_length = 50, default='Heidenheim', editable=True)
	Einsatzbeginn = models.TimeField('Einsatzbeginn', default=datetime.now)
	Einsatzende = models.TimeField('Einsatzende')
	Dienst = models.ManyToManyField(Dienst)
	Retter = models.ManyToManyField(Rettungsmittel)
	def __str__(self):
		return self.Einsatzort

class Behandlung(models.Model):
	Vorfall = models.ForeignKey(Vorfall, on_delete=models.DO_NOTHING)
	Patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
	Triagekategorie = models.IntegerField(default='1')
	Diagnose = models.CharField(max_length=200, default='Krank')






