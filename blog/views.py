from django.shortcuts import render
from django.views import generic
from .models import Author, Blog


class AuthorDetailView(generic.DetailView):
    model = Author


class BlogDetailView(generic.DetailView):
    model = Blog
