from django.db import models

class Personal(models.Model):
	Vorname = models.CharField(max_length=50)
	Name = models.CharField(max_length=50)
	Führungsqualifikation = models.CharField(max_length=50)
	Bereitschaft = models.CharField(max_length=20)
	Qualifikation = models.CharField(max_length=20)

class Einsatz(models.Model):
	Personal_ID = models.ForeignKey(Personal, on_delete=models.CASCADE)
	
class Dienst(models.Model):
	Dienstdatum = models.DateTimeField('date published')
	Personal_ID = models.ForeignKey(Personal, on_delete=models.CASCADE)
	Einsatzdatum = models.ForeignKey(Einsatz, on_delete=models.CASCADE)
	Einsatzbeginnzeit = models.DateTimeField('time published')
	Telefonnummer = models.CharField(max_length=20)
	Einsatzendezeit = models.DateTimeField('time published')
	

	
class Ansprechpartner(models.Model):
	Einsatz_ID = models.ForeignKey(Einsatz, on_delete=models.CASCADE)
	Datum = models.DateTimeField('date published')
	Telefonnummer = models.CharField(max_length=20)
	Geschlecht = models.CharField(max_length=1)
	Vorname = models.CharField(max_length=20)
	Name = models.CharField(max_length=20)
	Infotext = models.CharField(max_length=100)
	
class Rettungsmittel(models.Model):
	Bezeichnung = models.CharField(max_length=30)
	
class Vorfall(models.Model):
	Einsatzdatum = models.ForeignKey(Einsatz, on_delete=models.CASCADE)
	Einsatzort = models.CharField(max_length = 20)
	Einsatzbeginn = models.DateTimeField('time published')
	Einsatzende = models.DateTimeField('time published')
	
class Patient(models.Model):
	Vorname = models.CharField(max_length=20)
	Name = models.CharField(max_length=20)
	Alter = models.IntegerField()
	Geschlecht = models.CharField(max_length=1)
	Triagekategorie = models.IntegerField()
	Diagnose = models.CharField(max_length=200)
	Patient_Einsatzdatum = models.DateTimeField('date published')
	
class Hilfstabelle1(models.Model):
	Funkrufname = models.ForeignKey(Rettungsmittel, on_delete=models.CASCADE)
	Vorfall_ID = models.ForeignKey(Vorfall, on_delete=models.CASCADE)
	
class Hilfstabelle3(models.Model):
	Vorfall_ID = models.ForeignKey(Vorfall, on_delete=models.CASCADE)
	Patient_ID = models.ForeignKey(Patient, on_delete=models.CASCADE)

class Hilfstabelle2(models.Model):
	Hilfs_ID1 = models.ForeignKey(Hilfstabelle1, on_delete=models.CASCADE)
	Hilfs_ID3 = models.ForeignKey(Hilfstabelle3, on_delete=models.CASCADE)
	



