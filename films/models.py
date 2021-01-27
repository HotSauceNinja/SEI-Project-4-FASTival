from django.db import models
from django.core.validators import MinValueValidator

# Film model
class Film(models.Model):
    title = models.CharField(max_length=50, unique=True)
    director = models.CharField(max_length=100, unique=True)
    year_released = models.PositiveIntegerField(validators=[MinValueValidator(1900)])
    country = models.CharField(max_length=50)
    run_time = models.DurationField()
    plot = models.CharField(max_length=600)
    genre = models.CharField(max_length=50)
    poster = models.CharField(max_length=500)
    distributor = models.CharField(max_length=50)
    film_format = models.CharField(max_length=50)
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.director}"