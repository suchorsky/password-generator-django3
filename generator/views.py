from django.shortcuts import render
from django.http import HttpResponse
import string
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    length = int(request.GET.get('length', 12))
    characters = string.ascii_lowercase

    if request.GET.get('uppercase'):
        characters += string.ascii_uppercase
    if request.GET.get('special'):
        characters += '!@#$%^&*()'
    if request.GET.get('number'):
        characters += '1234567890'

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')
