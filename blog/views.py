from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from .models import Author, Blog


def index(request):
    return HttpResponse('Index Page of Blog App')


class AuthorDetailView(generic.DetailView):
    model = Author


class BlogDetailView(generic.DetailView):
    model = Blog
