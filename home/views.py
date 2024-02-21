from django.shortcuts import render
from django.contrib import messages
from .models import ContactUs


def home(request):
    """ Function to render the landpage"""
    return render(request, 'home/home.html')


def newsletter_signup(request):
    """ Function to render the newsletter signup page"""
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email-address']
        message = request.POST['message']
        contact = ContactUs(
            name=name,
            email=email,
            message=message
        )
        contact.save()
        messages.info(request, "Your form was successfully submitted")
    return render(request, 'home/newsletter_signup.html')


def error_404(request, exception):
    """ Function to render the 404 page"""
    return render(request, 'home/404.html')
