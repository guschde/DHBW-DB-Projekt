from django.contrib import admin
from .models import Personal, Einsatz,  Dienst, Ansprechpartner, Vorfall, Rettungsmittel, Patient
# Register your models here.

class PersonalAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['Vorname']}),
        (None, {'fields': ['Name']}),
        (None, {'fields': ['Führungsqualifikation']}),
        (None, {'fields': ['Bereitschaft']}),
        (None, {'fields': ['Qualifikation']}),
    ]
admin.site.register(Personal, PersonalAdmin)


class RettungsmittelAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['Bezeichnung']}),
    ]
admin.site.register(Rettungsmittel, RettungsmittelAdmin)

class PatientAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['Vorname']}),
        (None, {'fields': ['Name']}),
        (None, {'fields': ['Alter']}),
        (None, {'fields': ['Geschlecht']}),
    ]
admin.site.register(Patient, PatientAdmin)


class EinsatzAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['Personal_ID']}),
        (None, {'fields': ['Einsatzdatum']}),
        (None, {'fields': ['Einsatzinfo']}),

    ]
admin.site.register(Einsatz, EinsatzAdmin)


class AnsprechpartnerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['Einsatz_ID']}),
        (None, {'fields': ['Telefonnummer']}),
        (None, {'fields': ['Geschlecht']}),
        (None, {'fields': ['Vorname']}),
        (None, {'fields': ['Name']}),
        (None, {'fields': ['Infotext']}),

    ]

admin.site.register(Ansprechpartner, AnsprechpartnerAdmin)


class VorfallAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['Einsatz']}),
        (None, {'fields': ['Dienst']}),
        (None, {'fields': ['Patient']}),
        (None, {'fields': ['Einsatzort']}),
        (None, {'fields': ['Einsatzbeginn']}),
        (None, {'fields': ['Einsatzende']}),
        (None, {'fields': ['Retter']}),
    ]
admin.site.register(Vorfall, VorfallAdmin)




class DienstAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['Personal_ID']}),
        (None, {'fields': ['Einsatz_ID']}),
        (None, {'fields': ['Einsatzbeginnzeit']}),
        (None, {'fields': ['Einsatzendezeit']}),
        (None, {'fields': ['Funkrufname']}),
    ]
admin.site.register(Dienst, DienstAdmin)