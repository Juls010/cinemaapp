from django.db import models
from django.forms import ValidationError

#Método que verifica que el año es mayor o igual a 1900
def verf_year (value):
    if value < 1900:
        raise "The year of release must not be earlier than 1900"


#Método que verifica si la duración está entre 1 y 500
def verf_duration (value):
    if value < 1 or value > 500:
        raise "The duration must be between 1 and 500 minutes"

#Método que verifica si el rating está entre 0.0 y 10.0
def verf_rating (value):
    if value < 0.0 or value > 10.0:
        raise "The average rating must be between 0,0 and 10,0"

# modelo de la clase Movie, con sus campos y validadores correspondientes
class Movie (models.Model):
    title = models.CharField(max_length=100)
    synopsis = models.CharField(max_length=1000)
    genre = models.CharField(max_length=20)
    director = models.CharField(max_length=100)
    release_year = models.IntegerField(validators=[verf_year])
    duration = models.IntegerField(validators=[verf_duration])
    release_date = models.DateField()
    announcement_date = models.DateField()
    has_subtitles = models.BooleanField()
    subtitles_language = models.CharField()
    imdb = models.URLField(blank=True)
    rating = models.DecimalField(blank=True ,max_digits=3, decimal_places=1, validators=[verf_rating])

    #Método que coge datos del propio modelo (self)
    #Verifica si release_date es anterior a release_year
    #Verifica si has_subtitles es true, tiene que meter un lenguaje
    def clean(self):
        super().clean()
        if self.release_date and self.release_date < self.release_year:
            raise ValidationError("The announcement date must be before the release date")
        if self.has_subtitles:
            raise ValidationError("Please specify a languag")
