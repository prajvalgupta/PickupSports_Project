# APAD_project
Started the project...

Day 1 (Status - Task Completed) -

-> SQL Layout discussion
-> Table Names
-> Field Names

Day 2 (Status - Yet to start) -

-> Creating a database
-> Coding SQL queries
-> Starting work on Python functions

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

-> file name : testing.ipynb

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

