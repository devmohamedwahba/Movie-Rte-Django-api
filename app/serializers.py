from rest_framework import serializers
from .models import Movie, Rating
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=500, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'token']
        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
        }
        # read_only_fields = ('token',)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        token = Token.objects.create(user=user)
        user.token = token
        return user


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'get_no_of_rating', 'get_avg_rating']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'stars', 'movie', 'user']
