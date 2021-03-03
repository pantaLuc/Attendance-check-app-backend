from django.db import models
from django.utils import timezone
from users.models import User


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


class Plage(models.Model):
    begin = models.TimeField(auto_now=False, auto_now_add=False)
    end = models.TimeField(auto_now=False, auto_now_add=False)


class Semestre(models.Model):
    num_semestre = models.IntegerField()
    year = models.IntegerField()

class Exam(models.Model):
    day = models.DateField(auto_now=False, auto_now_add=False)
    plage = models.ForeignKey(Plage, on_delete=models.CASCADE)
    ue = models.ForeignKey(Ue, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE)



class Controler(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_control")
    surveillant = models.ForeignKey(Surveillant, on_delete=models.CASCADE, related_name="surv_control")
    examen = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="exam_control")
    is_present = models.BooleanField(default = False)
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE, related_name="salle_control")