from django.db import models


class Picture(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.TextField()

    def __str__(self):
        return f"{self.url}"

    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'

class Candidate(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    electionName = models.TextField()
    slug = models.TextField()
    number = models.PositiveIntegerField()
    bio = models.TextField()
    instagram = models.TextField(blank=True)
    latitude = models.DecimalField(decimal_places = 4,max_digits = 10)
    longitude = models.DecimalField(decimal_places = 4,max_digits = 10)
    facebookUrl = models.URLField(blank=True)
    campaignUrl = models.URLField(blank=True)
    supportUrl = models.URLField(blank=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    electedBefore = models.BooleanField(default=False)
    previousRole = models.ForeignKey('Role', on_delete=models.CASCADE, related_name='previous_role', null=True, blank=True)
    role = models.ForeignKey('Role', on_delete=models.CASCADE)
    ethnicity = models.ForeignKey('Ethnicity', on_delete=models.CASCADE, null=True)
    genderIdentity = models.ForeignKey('GenderIdentity', on_delete=models.CASCADE, null=True)
    causes = models.ManyToManyField('Cause')
    party = models.ForeignKey('Party', on_delete=models.CASCADE)
    picture = models.OneToOneField(Picture, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.electionName}"

    class Meta:
        verbose_name = 'Candidata'
        verbose_name_plural = 'Candidatas'

class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

class Party(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    number = models.IntegerField()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Partido'
        verbose_name_plural = 'Partidos'

class Cause(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(unique=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = 'Causa'
        verbose_name_plural = 'Causas'

class GenderIdentity(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Identidade de Gênero'
        verbose_name_plural = 'Identidades de Gênero'

class Ethnicity(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Etnia'
        verbose_name_plural = 'Etnias'