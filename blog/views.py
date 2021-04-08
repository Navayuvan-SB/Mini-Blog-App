from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.urls import reverse
from .models import Author, Blog, Comment
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

import datetime


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


class AuthorListView(generic.ListView):
    model = Author


class AuthorDetailView(generic.DetailView):
    model = Author


class BlogDetailView(generic.DetailView):
    model = Blog


class AddCommentView(LoginRequiredMixin, CreateView):

    model = Comment
    fields = ['text']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_blog = Blog.objects.get(pk=self.kwargs['blog_id'])
        context["blog"] = current_blog
        return context

    def form_valid(self, form):
        current_date = datetime.date.today()
        form.instance.user = self.request.user
        form.instance.comment_date = current_date

        current_blog = Blog.objects.get(pk=self.kwargs['blog_id'])
        form.instance.blog = current_blog

        return super(AddCommentView, self).form_valid(form)

    def get_success_url(self):
        return reverse('blog-detail', kwargs={'pk': self.kwargs['blog_id']})


class EditCommentView(LoginRequiredMixin, UpdateView):

    model = Comment
    fields = ['text']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_blog = Blog.objects.get(pk=self.kwargs['blog_id'])
        context["blog"] = current_blog
        return context

    def form_valid(self, form):
        current_date = datetime.date.today()
        form.instance.user = self.request.user
        form.instance.comment_date = current_date

        current_blog = Blog.objects.get(pk=self.kwargs['blog_id'])
        form.instance.blog = current_blog

        return super(EditCommentView, self).form_valid(form)

    def get_success_url(self):
        return reverse('blog-detail', kwargs={'pk': self.kwargs['blog_id']})


class DeleteCommentView(LoginRequiredMixin, DeleteView):
    model = Comment

    def get_success_url(self):
        return reverse('blog-detail', kwargs={'pk': self.kwargs['blog_id']})
