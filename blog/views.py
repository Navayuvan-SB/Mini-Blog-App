from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from .models import Author, Blog


def index(request):

    total_number_of_blogs = Blog.objects.count()
    total_number_of_authors = Author.objects.count()

    context = {
        'total_number_of_blogs': total_number_of_blogs,
        'total_number_of_authors': total_number_of_authors
    }

    return render(request, 'index.html', context)


class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 5


class AuthorDetailView(generic.DetailView):
    model = Author


class BlogDetailView(generic.DetailView):
    model = Blog
