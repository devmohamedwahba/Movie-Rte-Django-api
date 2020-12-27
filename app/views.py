from django.shortcuts import render
from .serializers import MovieSerializer, RatingSerializer
from rest_framework import viewsets
from .models import Movie, Rating


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
