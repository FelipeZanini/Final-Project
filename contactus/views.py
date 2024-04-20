from django.shortcuts import render
from contactus.models import ContactUs
from django.contrib import messages

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
