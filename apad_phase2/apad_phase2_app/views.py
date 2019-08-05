# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

from apad_phase2_app.utils.forms import EmailForm
from apad_phase2_app.utils.forms import VenueForm
from apad_phase2_app.utils.apad_project_functions import admin_check, new_venue


# Create your views here.
def index(request):
    return HttpResponse("Welcome to Ritika APAD app")


def emailForm(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            return HttpResponse('/thanks/')
    else:
        form = EmailForm()

    form_action = "venueFormPath"
    return render(request, 'venue_form.html', {'form': form, 'form_action': form_action})


def venueForm(request):
    # validate email here
    if not admin_check(request.POST.get('email_id', '')):
        error_message = 'Not an Admin. Enter email again'
        form_action = "venueFormPath"
        return render(request, 'venue_form.html',
                      {'form': EmailForm(), 'form_action': form_action, 'error_message': error_message})
    else:
        form_action = "insertVenuePath"
        return render(request, 'venue_form.html', {'form': VenueForm(), 'form_action': form_action})


def insertVenue(request):
    venue_name = request.POST.get('venue_name', '')
    address = request.POST.get('address', '')
    zip_code = request.POST.get('zip_code', '')
    contact_number = request.POST.get('contact_number', '')
    description = request.POST.get('description', '')
    open_time = request.POST.get('open_time', '')
    close_time = request.POST.get('close_time', '')
    games_total_count = request.POST.get('games_total_count', '')
    games_available_count = request.POST.get('games_available_count', '')

    venue_details = [venue_name, address, zip_code, contact_number, description, open_time, close_time,
                     games_total_count, games_available_count]
    if new_venue(venue_details):
        return HttpResponse('New venue is created successfully')
    #
    # new_venue(request.POST.get('venue_details', ''))
