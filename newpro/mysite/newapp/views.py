from django.shortcuts import render
from .models import MovieData
from django.core.paginator import Paginator
# Create your views here.

def movie_list(request):
    movie_objects = MovieData.objects.all()
    paginator = Paginator(movie_objects,4)
    page = request.GET.get('page')
    movie_objects = paginator.get_page(page)
    return render(request,'newapp/movie_objects.html',{'movie_objects':movie_objects})
