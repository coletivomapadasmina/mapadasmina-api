from django.db import models


class Candidate(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    electionName = models.TextField()
    slug = models.TextField()
    number = models.PositiveIntegerField()
    bio = models.TextField()
    instagram = models.TextField()
    latitude = models.DecimalField(decimal_places = 4,max_digits = 10)
    longitude = models.DecimalField(decimal_places = 4,max_digits = 10)
    facebookUrl = models.URLField()
    campaignUrl = models.URLField()
    supportUrl = models.URLField()
    age = models.PositiveIntegerField()
    electedBefore = models.BooleanField(default=False)
    previousRole = models.ForeignKey('Role', on_delete=models.CASCADE, related_name='previous_role', null=True)
    role = models.ForeignKey('Role', on_delete=models.CASCADE)
    ethnicity = models.ForeignKey('Ethnicity', on_delete=models.CASCADE, null=True)
    genderIdentity = models.ForeignKey('GenderIdentity', on_delete=models.CASCADE, null=True)
    causes = models.ManyToManyField('Cause')
    party = models.ForeignKey('Party', on_delete=models.CASCADE)
    picture = models.OneToOneField(Picture, on_delete=models.CASCADE)

class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()

class Party(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    number = models.IntegerField()

class Cause(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(unique=True)
    description = models.TextField()

class GenderIdentity(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()

class Ethnicity(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()

class Picture(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.TextField()