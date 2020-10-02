from django.db import models

# Create your models here.
class Jugador(models.Model):
    name = models.CharField("Nombre", max_length=40)
    surname = models.CharField("Apellidos", max_length=40)
    age = models.IntegerField("Edad", blank=False, null=False)

    def __str__(self):
        return self.name + " " + self.surname


class JugadorHabilidades(models.Model):
    class Habilidades(models.IntegerChoices):
        MALO = 1
        PESIMO = 2
        REGULAR = 3
        SOBRESALIENTE = 4
        EXCELENTE = 5

    jugador = models.OneToOneField(Jugador, on_delete=models.CASCADE)
    form = models.IntegerChoices("Forma", max_length=20)
    experience = models.CharField("Experiencia", max_length=20)
    discipline = models.CharField("Disciplina", max_length=20)
    stamina = models.CharField("Condición", max_length=20)
    pace = models.CharField("Rápidez", max_length=20)
    technique = models.CharField("Técnica", max_length=20)
    keeper = models.CharField("Guardameta", max_length=20)
    defending = models.CharField("Defensa", max_length=20)
    passing = models.CharField("Pases", max_length=20)
    playmaking = models.CharField("Creación", max_length=20)
    scoring = models.CharField("Anotación", max_length=20)

    def __str__(self) -> str:
        return self.id