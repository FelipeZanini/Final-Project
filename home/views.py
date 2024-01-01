from django.shortcuts import render


def home(request):
    """ Function to render the landpage"""
    return render(request, 'home/home.html')
