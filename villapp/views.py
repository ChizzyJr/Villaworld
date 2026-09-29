from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render (request, 'Apps/index.html')


def about(request):
    return render (request, 'Apps/about.html')


def contact(request):
    return render (request, 'Apps/contact.html')

def rides(request):
    return render (request, 'Apps/rides.html')

def termsofuse(request):
    return render (request, 'Apps/termsofuse.html')

def delivery(request):
    return render (request, 'Apps/delivery.html')