from django.http import JsonResponse
from django.shortcuts import render, redirect

from fezin import settings
from newsletter.forms import EmailForm

from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError
import logging
import os



logger = logging.getLogger(__name__)


def mailchimp_ping_view(request):
    response = mailchimp.ping.get()
    return JsonResponse(response)


def subscribe_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)

        if form.is_valid():
            try:
                form_email = form.cleaned_data['email']
                mailchimp = Client()
                mailchimp.set_config({
                    # After I should change to git secret envoriments------
                    'api_key': "9b1e4c40316a6e7f587dacf80abbfbf3-us22",
                })
                member_info = {
                    'email_address': form_email,
                    'status': 'subscribed',
                     "merge_fields": {
                    "FNAME": "firstName",
                    "LNAME": "lastName"
            }
                }
                
                response = mailchimp.lists.add_list_member("b9adfc5597", member_info, )
                logger.info(f'API call successful: {response}')
                return render(request, 'newsletter/subscribe.html', {
                'form': EmailForm(),
    })

            except ApiClientError as error:
                logger.error(f'An exception occurred: {error.text}')
                print(error.text)
                return render(request, 'newsletter/subscribe.html', {
                'form': EmailForm(),
    })

    return render(request, 'newsletter/subscribe.html', {
        'form': EmailForm(),
    })


def subscribe_success_view(request):
    return render(request, 'message.html', {
        'title': 'Successfully subscribed',
        'message': 'Yay, you have been successfully subscribed to our mailing list.',
    })


def subscribe_fail_view(request):
    return render(request, 'message.html', {
        'title': 'Failed to subscribe',
        'message': 'Oops, something went wrong.',
    })


def unsubscribe_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form_email = form.cleaned_data['email']
            # TODO: use Mailchimp API to unsubscribe
            return redirect('newsletter/unsubscribe-success')

    return render(request, 'newsletter/unsubscribe.html', {
        'form': EmailForm(),
    })


def unsubscribe_success_view(request):
    return render(request, 'message.html', {
        'title': 'Successfully unsubscribed',
        'message': 'You have been successfully unsubscribed from our mailing list.',
    })


def unsubscribe_fail_view(request):
    return render(request, 'message.html', {
        'title': 'Failed to unsubscribe',
        'message': 'Oops, something went wrong.',
    })