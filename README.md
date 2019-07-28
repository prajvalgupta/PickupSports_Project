# APAD_project
Started the project...

By - Prajval Gupta and Ritika Munjal

Project 1- Developing the basic data model in SQL for storing out application’s data, followed by python utility functions to manipulate the data.

Expected Deliverables - 

Function 1: Add a new user (admin only) 
Function 2: Add a new venue (admin only)
Function 3: Start an event (user or admin on behalf of a user)
Function 4: Display timeslot availability at a venue
Function 5: Display all venues where a particular timeslot is available
Function 6: List events at a venue given date/time
Function 7: User joins an event
Function 8: Remove an event (admin only)


CREATING A DATABASE:

-> file name : dbCreate.ipynb
-> DB name : APAD_proj.db
-> Table names and their use:
    -> user : stores the user information - name, password, email, contact_number, zip code
    -> venue : stores the venue information - venue name, address, open_time, close_time, total game slots, contact number etc
    -> event_category : stores the information regarding what king of event person wants to join/create- options are Watch/Play/Workshop
    -> sports_cat : stores the sports available on this application: sport_name, player_count, equipment required flag etc
    -> feedback : stores the feedback or conflicts from users: ticket_no, reason/subject, description, email_id etc
    -> events : stores information about all events created by user/admin - event_name, category, date, time, description, capacity_avaialble 
    
CREATING PYTHON FUNCTIONS:

-> file name : project1.ipynb (All functions clearly explained in the iPython file)

-> email_check(db,email) : to check if the user already exists in the database based on the email id
-> admin_check(db,email) : to check if the entered email is admin's email or not. This function is called where only admin is allowed to make changes
-> password_verify(pwd) : to verify new user's password in order to create account
-> new_user(db, inputs) : to create a new user/make a new account
-> user_input_form() : taking inputs from user to create a new account and make a list of all the entries. Output from this function is fed to new_user(db, inputs)
-> new_venue(db, inputs) : insert a new venue in venue table
-> add_venue_form() : checking if the person trying to create a venue is admin or not. If admin, then input all the values required to create a new venue
-> email_verify(db, email) : verify if the user is registered already or not if he tries to create an event
-> fetch_event_cat(cursor) : show the event categories to choose from - till now we have 3 categories: Play/Watch/Workshop
-> fetch_venue(cursor) : show the all the venues to choose from 
-> fetch_sport(cursor) : show all the sports available in the table
-> new_event(db,inputs) : creates a new event from the list output of event_create_inputs(db) function
-> event_create_inputs(db) : inputs to create a new event
-> fetch_venue_time(cursor, venue) : Function to fetch the open and close timings of a venue
-> fetch_event_time(cursor, venue, date) : Function to fetch the start time and end time of an event
-> fetch_avail_slot(cursor, venue) : Function to fetch the counts of instances of event that can be hosted simultaneously at a venue at a given timestamp
-> count(tuplelist) : Function to count instances of a tuple in a list and then store it in a dictionary
-> find_booked_slots(db,venue,date,debug=True) : Function to find the available timeslots at a venue for a given date
-> display_venues_given_time(db, event_date, start_time, end_time) : Function to return a list of available venues for a given timeslot
-> display_events_given_time(cursor, event_date, start_time) : Function to display the events at a particular venue for the given timestamp
-> join_event(db) : Function to join an event
-> delete_an_event(db) : Function to delete an event using event_id. Only admin is allowed to do so.

CSV FILES:
1. user.csv : Contains the user data for the add a user functionality
2. venue.csv : Contains the venue details for add a venue functionality

