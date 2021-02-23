from django.db import models


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



