from .serializers import MovieSerializer, TokenSerializer
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .PushNotification import sendNotification


class RefreshMovieList(APIView):
    def get(self, request, format=None):
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MovieSerializer(data=request)
        try:
            Movie.objects.get(title=request['title'])
        except:
            movie = 'empty'
        else:
            movie = Movie.objects.get(title=request['title'])

        if request['title'] != movie.title:
            sendNotification(request['title'],
                             request['url'],
                             request['image'],)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetNewestMovie(APIView):
    def get(self, request):
        try:
            Movie.objects.latest('id')
        except:
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            movie = Movie.objects.latest('id')
            data = MovieSerializer(movie)
            return Response(data.data)


class GetThumbnailMovie(APIView):
    def get(self, request):
        movie = Movie.objects.all().order_by('-id')[:5]
        serializer = MovieSerializer(movie, many=True)
        return Response(serializer.data)


class GetToken(APIView):
    def get(self, request):
        token = Token.objects.all()
        serializer = TokenSerializer(token, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TokenSerializer(data=request.data)

        try:
            Token.objects.get(token=request.data['token'])
        except:
            token = 'empty'
        else:
            token = Token.objects.get(title=request.data['token'])

        if request.data['token'] != token.title:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
