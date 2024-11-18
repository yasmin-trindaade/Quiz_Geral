from django.db import models

class Ranking(models.Model):
    nome = models.CharField(max_length=100)
    pontos = models.IntegerField()

    def __str__(self):
        return f"{self.nome} - {self.pontos} pontos"
