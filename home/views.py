from django.shortcuts import render
from django.contrib import messages



def home(request):
    """ Function to render the landpage"""
    return render(request, 'home/home.html')


def error_404(request, exception):
    """ Function to render the 404 page"""
    return render(request, 'home/404.html')
