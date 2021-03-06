from .models import Movie, Token
from rest_framework import serializers


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    def create(self, validated_data):
        return Movie.objects.create(
            title=validated_data['title'],
            year=validated_data['year'],
            url=validated_data['url'],
            image=validated_data['image'],
            star=validated_data['star'],
            duration=validated_data['duration'],
            genre=validated_data['genre'],
            imdb=validated_data['imdb'],
            video_url=validated_data['video_url']
        )


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'

    def create(self, validated_data):
        return Token.objects.create(
            token=validated_data['token']
        )