from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect


def sign_up_user(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            User.objects.create_user(username=username, password=password)

            return HttpResponseRedirect(reverse('login'))

    else:
        form = UserCreationForm()

    context = {
        'form': form
    }

    return render(request, 'registration/sign_up_user.html', context)
