from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)

    def get_no_of_rating(self):
        ratings = Rating.objects.filter(movie=self)
        return len(ratings)

    def get_avg_rating(self):
        sum = 0
        ratings = Rating.objects.filter(movie=self)
        for rating in ratings:
            sum += rating.stars
        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ])

    class Meta:
        unique_together = [('user', 'movie'), ]
        index_together = [('user', 'movie'), ]
