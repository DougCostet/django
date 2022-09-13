from django.db import models

class Pessoa(models.Model):
    name = models.CharField(max_length=200)
    idade = models.IntegerField()

pessoa = Pessoa.objects.get(nome='Douglas')
# Create your models here.
