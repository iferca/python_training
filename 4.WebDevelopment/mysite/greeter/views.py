from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User
from .forms import RegistrationForm


def index(request):
    users = User.objects.order_by('-name')[:50]
    context = {
        'users': users
    }
    return render(request, 'greeter/index.html', context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            title = form.cleaned_data['title']
            new_user = User(name=name)
            if title:
                new_user.title = title
            new_user.save()
            return HttpResponseRedirect(reverse('greet', args=(new_user.id,)))
    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'greeter/register.html', context)


def greet(request, user_id):
    u = User.objects.get(pk=user_id)
    return render(request, 'greeter/greet.html', {'user': u})
