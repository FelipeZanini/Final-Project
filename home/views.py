from django.shortcuts import render
from .models import ContactUs


def home(request):
    """ Function to render the landpage"""
    return render(request, 'home/home.html')



def contact_us(request):
    """ Function to render the contact us page"""
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
    return render(request, 'home/contact_us.html')


# custom 404 view
def error_404(request, exception):
    return render(request, 'home/404.html')
