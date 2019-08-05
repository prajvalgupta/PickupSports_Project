from django import forms
import sqlite3
db = sqlite3.connect("APAD_proj.db")
cursor = db.cursor()

class EmailForm(forms.Form):
    email_id = forms.CharField(label='Please enter your Email id', max_length=100)

class VenueForm(forms.Form):
    venue_name = forms.CharField(label='Please Enter the venue name', max_length=100)
    address = forms.CharField(label='Please Enter the venue address', max_length=100)
    zip_code = forms.CharField(label='Venue zip code', max_length=100)
    contact_number = forms.CharField(label='Please provide a contact number', max_length=100)
    description = forms.CharField(label='Enter the venue description (not more than 200 characters)', max_length=100)
    open_time = forms.CharField(label='Please Enter the open time in 24hrs format (Only the hour)', max_length=100)
    close_time = forms.CharField(label='Please Enter the close time in 24hrs format: (Only the hour)', max_length=100)
    games_total_count = forms.CharField(label='Please enter the total number of games that can be played in single time slot', max_length=100)
    games_available_count = forms.CharField(label='Please enter the available number of games that can be played in single time slot', max_length=100)
