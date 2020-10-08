"""Django Database model."""
from django.db import models


class Jugador(models.Model):
    """Tabla en BD de Jugador."""

    name = models.CharField("Nombre", max_length=40)
    surname = models.CharField("Apellidos", max_length=40)
    age = models.IntegerField("Edad", blank=False, null=False)

    class Meta:
        """Metadatos del la clase."""

        ordering = ["name"]
        verbose_name_plural = "Jugadores Verbose"
        verbose_name = "Jugador Verbose"

    def __str__(self):
        """Muestra objeto como nombre y apellido."""
        return self.name + " " + self.surname


class JugadorHabilidades(models.Model):
    """Tabla en BD con las habilidades de los jugadores."""

    class Habilidades(models.IntegerChoices):
        """Clase auxiliar para creación de lista de opciones."""

        MALO = 1
        PESIMO = 2
        REGULAR = 3
        SOBRESALIENTE = 4
        EXCELENTE = 5

    jugador = models.OneToOneField(Jugador, on_delete=models.CASCADE)
    forma = models.IntegerField(
        "Forma", choices=Habilidades.choices, default=Habilidades.REGULAR
    )
    experience = models.IntegerField(
        "Experiencia", choices=Habilidades.choices, default=Habilidades.REGULAR
    )
    discipline = models.IntegerField(
        "Disciplina", choices=Habilidades.choices, default=Habilidades.REGULAR
    )
    stamina = models.IntegerField(
        "Condición", choices=Habilidades.choices, default=Habilidades.REGULAR
    )
    pace = models.IntegerField(
        "Rápidez", choices=Habilidades.choices, default=Habilidades.REGULAR
    )
    technique = models.IntegerField(
        "Técnica", choices=Habilidades.choices, default=Habilidades.REGULAR
    )
    keeper = models.IntegerField(
        "Guardameta", choices=Habilidades.choices, default=Habilidades.REGULAR
    )
    defending = models.IntegerField(
        "Defensa", choices=Habilidades.choices, default=Habilidades.REGULAR
    )
    passing = models.IntegerField(
        "Pases", choices=Habilidades.choices, default=Habilidades.REGULAR
    )
    playmaking = models.IntegerField(
        "Creación", choices=Habilidades.choices, default=Habilidades.REGULAR
    )
    scoring = models.IntegerField(
        "Anotación", choices=Habilidades.choices, default=Habilidades.REGULAR
    )

    def __str__(self) -> str:
        """Muestra objeto según su ID."""
        return str(self.id)
