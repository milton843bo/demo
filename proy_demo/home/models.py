from django.db import models
from django.contrib.auth.models import User

class Citas(models.Model):
    titulo = models.CharField(max_length=140)
    texto = models.TextField()
    fecha = models.DateTimeField()
    usuario = models.ForeignKey(User)

    def __unicode__(self):
    	return self.titulo
