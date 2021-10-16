from django.db import models
from django import forms

class Musician(models.Model):

    First_Name = models.CharField(max_length=128)
    Last_Name = models.CharField(max_length=128)
    Instrument = models.CharField(max_length=256)

    def __str__(self):

        return self.First_Name + " " + self.Last_Name

class Album(models.Model):

    Artist = models.ForeignKey(Musician,on_delete = models.CASCADE)
    Name = models.CharField(max_length=256)
    Release_Date = models.DateField()

    level = (
                (1,'Worst'),
                (2,'Average'),
                (3,'Good'),
                (4,'Best'),
                (5,'Great')
    )

    Rating = models.IntegerField(choices=level)

    def __str__(self):

        return self.Name
