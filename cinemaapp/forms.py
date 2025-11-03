
from django import forms

from cinemaapp.models import Movie

# Forms de nuestra web
class MovieForm (forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'      #queremos todos los datos
        labels = {  #Damos nombres bonitos a los campos
            "title" : "Title of the movie",
            "synopsis" : "Short plot summary",
            "genre" : "Movie genre",
            "director" : "Director’s full name",
            "release_year" : "Year of release",
            "duration" : "Duration (in minutes)",
            "release_date" : "Release date",
            "announcement_date" : " Announcement date",
            "has_subtitles" : "Has subtitles",
            "subtitles_language" : "Subtitles language",
            "imdb" : "IMDB URL",
            "rating" : "Average rating (0-10)"
        }
        # aquí mostramos en este caso el calendario a los campos date
        widgets = {
            "release_date" :  forms.DateInput(attrs={"type":"date"}),
            "announcement_date": forms.DateInput(attrs={"type": "date"}),
            "actors" : forms.CheckboxSelectMultiple()
        }

        # Manejo de mensajes de errores para cada campo y cada error en especifico
        error_message = {
            "title" : {
                "max_length" : "The title of the movie must not be more than 100 characters long",
                "required" : "The title of the movie is required"
            },
            "genre" : {
                "required" : "The genre of the movie is required"
            },
            "release_date" : {
                "required" : "The release date is required"
            }
        }