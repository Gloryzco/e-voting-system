from django.db import models

# Create your models here.

class Position(models.Model):
    name = models.CharField(max_length=100)
    no_of_contestant = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Contestant(models.Model):
    surname = models.CharField(max_length=32)
    firstname = models.CharField(max_length=32)
    image = models.ImageField(upload_to='gallery', blank=True)
    department = models.CharField(max_length=100)
    no_of_votes = models.IntegerField(default=0)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstname

class User(models.Model):
    surname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=32)
    email = models.EmailField(max_length=100)
    department = models.CharField(max_length=100)
    voted = models.BooleanField(default=False)

    def __str__(self):
        return self.firstname