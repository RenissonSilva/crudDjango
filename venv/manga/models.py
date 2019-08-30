from django.db import models


class Manga(models.Model):
    nome = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    ano = models.IntegerField()

    # price = models.DecimalField(max_digits=9, decimal_places=2)
    # quantity = models.IntegerField()

    def __str__(self):
        return self.description
