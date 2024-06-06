from django.db import models


class Tag(models.Model):
    nome = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.id} - {self.nome}"


class Receita(models.Model):
    titulo = models.CharField(max_length=255, unique=True)
    descricao = models.TextField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.id} - {self.nome}"
