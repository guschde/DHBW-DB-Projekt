from django.test import TestCase

# Create your tests here.
liste = ['huhu', 'huhi', 1]

def listerer(liste):
    for x in liste:
        print(type(str(x)))
        print(type(x))

listerer(liste)