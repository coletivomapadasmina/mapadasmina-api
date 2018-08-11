from django.db import models

class Party(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.TextField()
    number=models.IntegerField()

class Candidate(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.TextField()
    slug=models.TextField()
    number=models.PositiveIntegerField()
    bio=models.TextField()
    instagram=models.TextField()
    latitude=models.DecimalField(decimal_places=4,max_digits=10)
    longitude=models.DecimalField(decimal_places=4,max_digits=10)
    facebookURL=models.URLField()
    campaignUrl=models.URLField()
    supportUrl=models.URLField()
    age=models.PositiveIntegerField()    
    electedBefore=models.BooleanField(default=False)
    role=models.ForeignKey('Role', on_delete=models.CASCADE)
    party=models.ForeignKey('Party',on_delete=models.CASCADE)
    picture=models.ForeignKey('Picture',on_delete=models.CASCADE)

class Role(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.TextField()

class Picture(models.Model):
    id=models.IntegerField(primary_key=True)
    url=models.TextField()