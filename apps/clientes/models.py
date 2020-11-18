from django.db import models

# Create your models here.

class Cliente(models.Model):

    class Meta:
        db_table = 'cliente'

    name = models.CharField(max_length=80)
    image = models.ImageField(upload_to='imagens')
    selecionado = models.BooleanField(default=False)