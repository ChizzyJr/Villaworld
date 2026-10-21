from django.shortcuts import render
from .models import Manufacturer

# Create your views here.
def index(request):
    return render (request, 'Apps/index.html')


def about(request):
    return render (request, 'Apps/about.html')


def contact(request):
    if request.method == 'POST':
        print(request.POST)

    return render(request, 'Apps/contact.html')

def rides(request):
    vehicles = Manufacturer.objects.all()
    return render(request, 'Apps/rides.html', {'vehicles': vehicles})

def termsofuse(request):
    return render (request, 'Apps/termsofuse.html')

def delivery(request):
    return render (request, 'Apps/delivery.html')