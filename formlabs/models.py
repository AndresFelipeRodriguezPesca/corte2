from django.db import models



class Cliente(models.Model):

    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    correo=models.CharField(max_length=200)
    telefono=models.IntegerField()
    industria=models.CharField(max_length=200)
    trabajo=models.CharField(max_length=200)
    empresa=models.CharField(max_length=200)

    class Meta:
        db_table="cliente"

