from django.db import models

<<<<<<< HEAD
class Personal(models.Model):
	Vorname = models.CharField(max_length=50)
	Name = models.CharField(max_length=50)
	Führungsqualifikation = models.CharField(max_length=50)
	Bereitschaft = models.CharField(max_length=20)
	Qualifikation = models.CharField(max_length=20)
	
class Dienst(models.Model):
	Dienstdatum = models.DateTimeField('date published')
	Personal-ID = models.ForeignKey(Personal, on_delete=models.CASCADE)
	Einsatzdatum = models.ForeignKey(Einsatz, on_delete=models.CASCADE)
	Einsatzbeginnzeit = models.DateTimeField('time published')
	Telefonnummer = models.CharField(max_length=20)
	Einsatzendezeit = models.DateTimeField('time published')
	
class Einsatz(models.Model):
	Personal-ID = models.ForeignKey(Personal, on_delete=models.CASCADE)
	
class Ansprechpartner(models.Model):
	Einsatz-ID = models.ForeignKey(Einsatz, on_delete=models.CASCADE)
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
	Geschlecht = = models.CharField(max_length=1)
	Triagekategorie = models.IntegerField()
	Diagnose = models.CharField(max_length=200)
	Patient-Einsatzdatum = models.DateTimeField('date published')
	
class Hilfstabelle1(models.Model):
	Funkrufname = models.ForeignKey(Rettungsmittel, on_delete=models.CASCADE)
	Vorfall-ID = models.ForeignKey(Vorfall, on_delete=models.CASCADE)
	
class Hilfstabelle2(models.Model):
	Hilfs-ID1 = models.ForeignKey(Hilfstabelle1, on_delete=models.CASCADE)
	Hilfs-ID3 = models.ForeignKey(Hilfstabelle3, on_delete=models.CASCADE)
	
class Hilfstabelle3(models.Model):
	Vorfall-ID = models.ForeignKey(Vorfall, on_delete=models.CASCADE)
	Patient-ID = models.ForeignKey(Patient, on_delete=models.CASCADE)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=1)
    def __str__(self):
        return self.choice_text

=======
#class Einsatz
>>>>>>> cf35e8f22044424357fd867b162cfdd682c7c578


