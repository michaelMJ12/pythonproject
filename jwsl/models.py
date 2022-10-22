from django.db import models

class Activites(models.Model):
     title= models.CharField(max_length=3, null=True)
     body = models.CharField(max_length=300, null=True)

class Review(models.Model):
     name = models.CharField(max_length=50, null=True)
     proffession = models.CharField(max_length=50, null=True)
     text = models.TextField(max_length=500, null=True)

class Directors(models.Model):
     name = models.CharField(max_length=50, null=True)
     position = models.CharField(max_length=50, null=True)
     img = models.ImageField(upload_to='pictures', null=True)

class Experience(models.Model):
     years = models.IntegerField(null=True)
     clients = models.IntegerField(null=True)
     projects = models.IntegerField(null=True)
     skill = models.IntegerField(null=True)
