from django.db import models

# Create your models here.

class Pratos(models.Model):

    class Meta:
        db_table = 'prato'

    name = models.CharField(max_length=100)
    value = models.FloatField()
    imagem = models.ImageField(upload_to='imagens')

    
    def __str__(self):
        return self.name


class Produtos(models.Model):


    class Meta:
        db_table = 'produto'


    categoria = models.CharField(max_length=50)
    pratos = models.ManyToManyField(Pratos, related_name='pratos')