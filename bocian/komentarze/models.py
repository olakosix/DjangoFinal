from django.db import models

# Create your models here.
class Polakomenatarze (models.Model):

    nick = models.CharField(max_length=200)
    email = models.EmailField()
    tytul = models.CharField(max_length=200)
    tresc = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    wpis = models.ForeignKey(Wpis, on_delete=models.CASCADE)
