from django.contrib import admin
from .models import Movie, Rating


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass


@admin.register(Rating)
class MovieAdmin(admin.ModelAdmin):
    pass
