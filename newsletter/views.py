from django.http import JsonResponse
from django.shortcuts import render, redirect

from fezin import settings
from newsletter.forms import EmailForm

from mailchimp_marketing import Client
import hashlib
from mailchimp_marketing.api_client import ApiClientError
import logging
import os



logger = logging.getLogger(__name__)


def subscribe_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)

        if form.is_valid():
            try:
                form_email = form.cleaned_data['email']
                mailchimp = Client()
                mailchimp.set_config({
                    # After I should change to git secret envoriments------
                    'api_key': "03ffcdbe7160e1dbb9691ad66d7328df-us22",
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
                return redirect('subscribe_success_view')

            except ApiClientError as error:
                logger.error(f'An exception occurred: {error.text}')
                print(error.text)
                return redirect('subscribe_fail_view')

    return render(request, 'newsletter/subscribe.html', {
        'form': EmailForm(),
    })


def subscribe_success_view(request):
    return render(request, 'newsletter/message.html', {
        'title': 'Successfully subscribed',
        'message': 'Yay, you have been successfully subscribed to our mailing list.',
    })


def subscribe_fail_view(request):
    return render(request, 'newsletter/message.html', {
        'title': 'Failed to subscribe',
        'message': 'Oops, something went wrong.',
    })


def unsubscribe_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            mailchimp = Client()
            mailchimp.set_config({
                    # After I should change to git secret envoriments------
                    'api_key': "12224ab58c5e8383c4e170eab85d6b19-us22",
                })
            try:
                form_email = form.cleaned_data['email']
                form_email_hash = hashlib.md5(form_email.encode('utf-8').lower()).hexdigest()
                member_update = {
                    'status': 'unsubscribed',
                }
                response = mailchimp.lists.update_list_member(
                    "b9adfc5597",
                    form_email_hash,
                    member_update,
                )
                logger.info(f'API call successful: {response}')
                return redirect('unsubscribe_success_view')

            except ApiClientError as error:
                logger.error(f'An exception occurred: {error.text}')
                return redirect('unsubscribe_fail_view')

    return render(request, 'newsletter/unsubscribe.html', {
        'form': EmailForm(),
    })

def unsubscribe_success_view(request):
    return render(request, 'newsletter/message.html', {
        'title': 'Successfully unsubscribed',
        'message': 'You have been successfully unsubscribed from our mailing list.',
    })


def unsubscribe_fail_view(request):
    return render(request, 'newsletter/message.html', {
        'title': 'Failed to unsubscribe',
        'message': 'Oops, something went wrong.',
    })