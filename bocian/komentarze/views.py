from django.shortcuts import render

from blog import models


def dodaj(request):
    nick = request.POST['nick']
    email = request.POST['email']
    tytul = request.POST['tytul']
    tresc = request.POST['tresc']
    wpis = models.ForeignKey()

    auto.save()

    return Httpresponse ('Komentarz został dodany')

class Httpresponse(object):
    pass


