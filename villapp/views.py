from django.shortcuts import render, redirect
from .models import Manufacturer
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage

# Create your views here.
def index(request):
    return render (request, 'Apps/index.html')


def about(request):
    return render (request, 'Apps/about.html')



def contact(request):
    if request.method == 'POST':
        name = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        message = request.POST.get('message', '').strip()

        if not all([name, email, message]):
            messages.error(
                request,
                'Please provide your name, email address, and message.'
            )
            return redirect('contact')

        subject = f'New website enquiry from {name}'
        email_message = (
            f'Name: {name}\n'
            f'Customer email: {email}\n'
            f'Phone: {phone or "Not provided"}\n\n'
            f'Message:\n{message}'
        )

        
        try:
            email = EmailMessage(
                subject=subject,
                body=email_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.CONTACT_EMAIL],
                reply_to=[email],
            )
            email.send(fail_silently=False)

            messages.success(
                request,
                'Thank you! Your enquiry has been sent successfully.'
            )
        except Exception as e:
            print("EMAIL SENDING ERROR:", repr(e))
            messages.error(
                request,
                'Sorry, we could not send your enquiry right now. '
                'Please try again later or contact us by phone.'
            )


        return redirect('contact')

    return render(request, 'Apps/contact.html')


def rides(request):
    vehicles = Manufacturer.objects.all()
    return render(request, 'Apps/rides.html', {'vehicles': vehicles})

def termsofuse(request):
    return render (request, 'Apps/termsofuse.html')

def delivery(request):
    return render (request, 'Apps/delivery.html')