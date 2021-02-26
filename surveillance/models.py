from django.db import models
from django.utils import timezone


# Create your models here.
class Surveillant(models.Model):
    GENRE_CHOICES = (
        ('masculin', 'Masculin'),
        ('feminin', 'Feminin'),
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    #phone = models.CharField(max_length=10)
    genre = models.CharField(max_length=10,
                                choices=GENRE_CHOICES,
                                default='masculin'
                            )


class Salle(models.Model):
    code = models.CharField(max_length=10)
    libelle = models.CharField(max_length=255)
    localisation = models.CharField(max_length=255)


class Filiere(models.Model):
    name = models.CharField(max_length=255)


class Niveau(models.Model):
    NIVEAU_CHOICES = (
        (1, 'I'),
        (2, 'II'),
        (3, 'III'),
        (4, 'IV'),
    )
    level = models.CharField(max_length=10,
                              choices=NIVEAU_CHOICES,
                              default='1'
                            )
    nbr_student = models.IntegerField()
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)


class Ue(models.Model):
    code = models.CharField(max_length=255)
    intitule = models.CharField(max_length=255)
    duration = models.IntegerField()
    level = models.ForeignKey(Niveau, on_delete=models.CASCADE)


class Exam(models.Model):
    day = models.DateField(auto_now=False, auto_now_add=False)
    begin = models.TimeField(auto_now=False, auto_now_add=False)
    end = models.TimeField(auto_now=False, auto_now_add=False)
    ue = models.ForeignKey(Ue, on_delete=models.CASCADE)
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)


class Present(models.Model):
    examen = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="present")
    #surveillant = models.ForeignKey(Surveillant, on_delete=models.CASCADE)
    is_present = models.BooleanField(default = False)