from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import MovieData
# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieSerializer

class LoveViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genre='feel good love')
    serializer_class = MovieSerializer

class AnimationViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genre = 'animation')
    serializer_class = MovieSerializer