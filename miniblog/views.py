from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import CustomSignupForm

from blog.models import Author


def sign_up_user(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))

    if request.method == 'POST':

        form = CustomSignupForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            date_of_birth = form.cleaned_data['date_of_birth']
            bio = form.cleaned_data['bio']

            new_user = User.objects.create_user(
                username=username, password=password, first_name=first_name, last_name=last_name)

            new_author = Author.objects.create(
                name=new_user.get_full_name(),
                date_of_birth=date_of_birth, bio=bio)

            new_author.save()

            return HttpResponseRedirect(reverse('login'))

    else:
        form = CustomSignupForm()

    context = {
        'form': form
    }

    return render(request, 'registration/sign_up_user.html', context)
