from django.shortcuts import render
from django.views import generic
from .models import Author


class AuthorDetailView(generic.DetailView):
    model = Author
