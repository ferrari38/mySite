from django.db import models

# Create your models here.

class PersonTmp(models.Model):

    # 名前
    f_name = models.CharField(max_length=16)
    l_name = models.CharField(max_length=16)
    age = models.IntegerField()

class Worker(models.Model):
    # 名前
    name = models.CharField(max_length=16)
    age = models.IntegerField()

class Log(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    tmp = models.IntegerField()
