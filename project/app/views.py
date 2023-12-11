from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm, UserForm2

def index(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            return HttpResponse(f'Name: {name}')
        else:
            return HttpResponse('Данные не валидны')
    else:
        form = UserForm
        return render(request, 'app/index.html', context={'form': form})

