from django.db import models

class Candidate(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.TextField()
    slug=models.TextField()
    party=models.TextField()
    number=models.TextField()
    latitude=models.TextField()
    longitude=models.TextField()
    # party=models.ForeignKey(Party,related_name='candidates')

""" class Party(models.Model)
    id=models.IntegerField(primary_key=True)
    name=models.TextField()
    number=models.IntegerField()

class Picture(models.Model)
    id=models.IntegerField(primary_key=True)
    url=models.TextField() """


class Party(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.TextField()
    number=models.IntegerField()