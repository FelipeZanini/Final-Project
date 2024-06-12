from django.http import JsonResponse
from django.shortcuts import render, redirect

from fezin import settings


def newsletter_subscribe(request):

    return render(request, 'newsletter/subscribe.html')
