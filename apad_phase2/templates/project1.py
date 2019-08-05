#!/usr/bin/env python
# coding: utf-8

# # Python Utility Functions
# 
# This is being developed for the Project 1 of the Advanced Programming & App Developemnt course (MIS 382N) taught by Prof. Ramesh Yerraballi. These are the utility functions for the operations and access the data from the database created using `dbCreate.ipyng` file.
# 
# Creators - Prajval Gupta and Ritika Munjal

# In[1]:


# connecting to database and importing required libraries
import sqlite3
import datetime
from datetime import timedelta
db = sqlite3.connect("APAD_proj.db")
cursor = db.cursor()


# ## Function 1: Add a new user
# 
# In our application, we are allowing every user to create its own account. Hence, this functionality is not limited only at admin level. 
# 
# Actionable Sequence of this function:
# 
# 1. When user/admin tries to add a single user: [Check](#single-user-input)
# > Calls the `user_input_form` function
# > Asks for user email and then input is checked for an existing user using `email_check` function. <br>
# > Asks for user details <br>
# > Check if password and password_check fields match using `password_verify` function <br>
# > Call the `new_user` function and execute the INSERT query <br>
# 
# 2. When admin tries to add multiple users at a time: [Check](#multi-user-input)
# > Fetch the data from `user.csv` <br>
# > Call the `new_user` function and execute the INSERT query <br>

# In[2]:


# Function to check if the user already exists in the database based on the email id
def email_check(db,email):
    cursor = db.cursor()
    while(1):
        findEmail = '''SELECT * FROM user where email_id = ?'''
        cursor.execute(findEmail, (email,))
        if cursor.fetchall():
            print("Email already registered, enter again")
            email = str(input("Please provide your email-address: "))
        else:
            return email

# Function to verify new user's password in order to create account
def password_verify(pwd):
    while pwd[0]!=pwd[1]:
        print("Your passwords didn't match, enter again")
        pwd[0] = str(input("Enter the password: ")) # NEED to add constraints
        pwd[1] = str(input("Enter the password again to recheck: "))
    return pwd[0], pwd[1]
        

#Function to create a new user
def new_user(db, inputs):
    cursor = db.cursor()
    query = '''INSERT INTO user(email_id,first_name,last_name,contact_number, zip_code, password)
                    VALUES(?,?,?,?,?,?)'''
    cursor.execute(query, (inputs[:6]))  
    db.commit()
    print("User added successfully")


# Function to taking inputs from user to create a new account and make a list of all the entries. 
# Output from this function is fed to new_user(db, inputs)
def user_input_form():
    email = str(input("Please provide your email-address: "))
    email = email_check(db, email)
    first_name = str(input("Please Enter your first name: "))
    last_name = str(input("Please Enter your last name: "))
    contact_number = str(input("Please provide a valid contact number: "))
    zip_code = str(input("Your zip code: "))
    password = str(input("Enter the password: ")) # NEED to add constraints
    password_check = str(input("Enter the password again to recheck: "))
    pwd = [password, password_check]
    password, password_check = password_verify(pwd)
    inputs = [email, first_name, last_name, contact_number, zip_code, password, password_check]
    
    return inputs


# <a id="single-user-input"></a>

# In[3]:


# Triggering the add a user functionality when user/admin tries to add a single user
inputs = user_input_form()
new_user(db, inputs)


# <a id="multi-user-input"></a>

# In[5]:


# Triggering the add a user functionality when admin tries to add multiple users at a time
import csv
config = open("user.csv", 'r')
csvReader = csv.reader(config)
lis=[]
for row in csvReader:
    lis.append(row)
for i in range(1,len(lis)):
    new_user(db,lis[i])


# ## Function 2: Add a new venue (admin only)
# Only admin can add a new venue. If you will not provide the right admin email id, our system will notify that it is not the admin id and will ask for the correct admin email id.
# 
# Actionable Sequence of this function:
# 1. When admin wants to add a single venue: [Check](#single-venue-input)
# > Calls the `add_venue_form` function to take the inputs <br>
# > Checks for admin using `admin_check` function <br>
# > Asks for the venue details - Venue Name, Address, Zip Code, Contact number, Description, Open time, Close time, Total capacity at a timestamp<br>
# > Calls the `new_venue` function and execute the INSERT query<br>
# 
# 2. When admin wants to add multiple venues at a time: [Check](#multi-venue-input)
# > Fetch the data from `venue.csv`<br>
# > Calls the `new_venue` function and execute the INSERT query<br>
# 

# In[6]:


# Function to check if the entered email is admin's email or not. This function is called where only admin is allowed to make changes

def admin_check(db,email):
    cursor = db.cursor()
    findEmail = '''SELECT email_id FROM user where first_name = ?'''
    cursor.execute(findEmail, ("admin",))
    admin = cursor.fetchone()[0]
#     print(admin)
    while email != admin:
        print("Only admin is authorized to add/remove a venue")
        email = str(input("Enter the admin's email address: "))
    
    return email

# Function to add a new venue in venue table
def new_venue(db, inputs):
    cursor = db.cursor()
    query = '''INSERT INTO venue(venue_name, address, zip_code, contact_number, description, open_time, close_time, games_total_count, games_available_count)
                VALUES(?,?,?,?,?,?,?,?,?)'''
    cursor.execute(query, inputs[1:]) 
    db.commit()
    print("Venue added successfully")

    
# Function to take inputs from the admin to create a venue
# It checks for the admin email id and if entered wrong it will notify that it is not the admin id and will ask for the correct admin email id.
def add_venue_form():
    email = str(input("Please enter your email address: "))
    email1 = admin_check(db,email)
    venue_name = str(input("Please Enter the venue name: "))
    address = str(input("Please Enter the venue address: "))
    zip_code = str(input("Venue zip code: "))
    contact_number = str(input("Please provide a contact number: "))
    description = str(input("Enter the venue description (not more than 200 characters): ")) # Need to limit the length of input
    open_time = str(input("Please Enter the open time in 24hrs format (Only the hour): "))
    close_time   = str(input("Please Enter the close time in 24hrs format: (Only the hour)"))
    games_total_count = int(input("Please enter the total number of games that can be played in single time slot: "))
    # games_available_count = int(input("Please enter the available number of games that can be played in single time slot: "))
    games_available_count = 0
    inputs_venue = [email1,venue_name,address,zip_code,contact_number,description,open_time,close_time,games_total_count, games_available_count]
    return inputs_venue


# <a id="single-venue-input"></a>

# In[7]:


# Triggering the add a venue functionality
inputs_venue = add_venue_form()
new_venue(db, inputs_venue)


# <a id="multi-venue-input"></a>

# In[8]:


# Adding multiple venues at a time by fetching data from csv files
import csv
config = open("venue.csv", 'r')
csvReader = csv.reader(config)
lis1=[]
for row in csvReader:
    lis1.append(row)
for i in range(1,len(lis1)):
    new_venue(db,lis1[i])


# ## Function 3: Start an event (user or admin on behalf of user)
# This first asks for the user email id and if the user is not registered and ask to create an account first and takes the user to function 1 i.e. add a new user and then brings back to this function.
# 
# Actionable sequence for this function: [Check](#create-event)
# 
# > Calls the `event_create_inputs` function and asks for user email<br>
# > Verifies the user email-id using `email_verify` function and if user not registered asks to register first taking it back to "Function 1" and then returns back to this function<br>
# > Asks if user want to create or join an event. If user wants to create then continue else takes it to "Function 7"<br>
# > Asks for the event name<br>
# > Now displays the available sports using `fetch_sport` function and asks user/admin to select the appropriate sport<br>
# > Asks for event details - Event Date, Start time, End time, Description, Capacity<br>
# > Displays the category of events using `fetch_event_cat` function and asks user to select one. In our case we have considered three types of events - Play a sport, Watch a sport, Attend tutorial class or Workshop for a sport<br>
# > Displays the venues using `fetch_venue` function and asks user to select a venue<br>
# > Now take all these inputs and calls the `new_event` function and execute the INSERT and UPDATE queries<br>
# > Event is created successfully<br>

# In[9]:


# Function to verify if the user is registered already or not when he tries to create an event
def email_verify(db, email):
    cursor = db.cursor()
    
    findEmail = '''SELECT email_id FROM user where email_id = ?'''
    cursor.execute(findEmail, (email,))
    
    if cursor.fetchall():
        return email
    else:
        print("You can't create an event yet. Create an account first")
        inputs = user_input_form()
        new_user(db, inputs)
        return inputs[0]

# Function to show the event categories to choose from - till now we have 3 categories: Play/Watch/Workshop    
def fetch_event_cat(cursor):
    event_cat_query = '''SELECT event_category_name FROM event_category'''
    cursor.execute(event_cat_query)
    event_cat1 = cursor.fetchall()
    event_cat = []
    for i in range(len(event_cat1)):
        event_cat.append(event_cat1[i][0])
    
    print("Please select a category from the following: ") 
    for i in range(len(event_cat)):
        print(str(i) +":" + event_cat[i])
    
    
# Function to fetch all the venues to choose from and display it to the user before taking the input
def fetch_venue(cursor):
    venue_query = '''SELECT venue_name FROM venue'''
    cursor.execute(venue_query)
    venues1 = cursor.fetchall()
    venues = []
    for i in range(len(venues1)):
        venues.append(venues1[i][0])
        
    print("Please select a venue from the following: ") 
    for i in range(len(venues)):
        print(str(i) +":" + venues[i])
    return venues

# Function to fetch all the sports to choose from and display it to the user before taking the input
def fetch_sport(cursor):
    sport_query = '''SELECT sport_name FROM sports_cat'''
    cursor.execute(sport_query)
    sports1 = cursor.fetchall()
    
    sports = []
    for i in range(len(sports1)):
        sports.append(sports1[i][0])
    
    print("Please select a sport from the following: ") 
    for i in range(len(sports)):
        print(str(i) +":" + sports[i])
    return sports


# Function to create a new event using the outputs of event_create_inputs(db) function
def new_event(db,inputs):
    
    cursor = db.cursor()

    if inputs[9] == "create":

        host_insert_flag = '''INSERT INTO events(event_cat_id,venue_id,event_name, date, start_time,end_time,
                                              user_id, host_flag, member_flag, sports_cat_id, event_desc, capacity_avail)
                       VALUES(?,?,?,?,?,?,?,?,?,?,?,?)'''


        cursor.execute(host_insert_flag, (inputs[7],inputs[8],inputs[1],inputs[2],inputs[3],inputs[4],inputs[0],1,0,inputs[10],inputs[5], inputs[6]))  

        db.commit()
        
        # -1 the count of games_available count in venue table
        
        update_game_avail_ct  = '''UPDATE venue SET games_available_count = ? WHERE venue_id = ?'''
        cursor.execute(update_game_avail_ct,(inputs[11]-1,inputs[8]))
        db.commit()
        print("Event created successfully")

# Function to take inputs from the user or admin to create a new event
def event_create_inputs(db):
    
    count = 0
#     cursor = db.cursor()
#     db.row_factory = lambda cursor, row: row[0]
    #Input the email of the user
    email = str(input("Please provide your email-address: "))

    #Check if it's an existing user
    email = email_verify(db,email)
    
    create_or_join = str(input("Do you want to create/join the game: ")).lower()
    
    if create_or_join == "join":
        join_event(db)
    else:
    
        #Get the user_id from the database
        user_id_query = '''SELECT user_id FROM user where email_id = ?'''
        cursor.execute(user_id_query, (email,))
        user_id = cursor.fetchone()[0]
#         print(user_id)
        event_name = str(input("Please Enter the event name: "))

        #Fetch the list of sports 
        sports = fetch_sport(cursor)

        #Input for sport. Only accept if it exists!
        while(1):
            sport_name = str(input("Please Enter the sport name: "))
            for i in sports:
                if (sport_name == i):
                    count=1
                    break
            if count==1:
                break
            else:
                print("Please enter the correct sport from choices above!")

        #Get the sport id from the database
        sports_cat_id_query = '''SELECT sports_cat_id FROM sports_cat where sport_name = ?'''
        cursor.execute(sports_cat_id_query, (sport_name,))
        sports_cat_id = cursor.fetchone()[0]

        event_date = str(input("Please Enter the event date (yyyy-mm-dd):"))
        start_time = str(input("Please Enter the start time in 24hrs format (Only the hour): "))
        end_time   = str(input("Please Enter the end time in 24hrs format (Only the hour): "))
        event_desc = str(input("Please Enter the event description: "))
        capacity   = str(input("Please Enter the capacity avail: "))

        #Fetch all event categories
        fetch_event_cat(cursor)

        #Input for event category. Only accept if it exists!
        while(1):
            event_category_name = str(input("Please Enter the event category name : "))
            if (event_category_name == "watch" or event_category_name == "play" or event_category_name == "workshop" ):
                break
            else:
                print("Please enter the right category from choices above!")

        #Get the Event cat id from the database
        event_cat_id_query = '''SELECT event_cat_id FROM event_category where event_category_name = ?'''
        cursor.execute(event_cat_id_query, (event_category_name,))
        event_cat_id = cursor.fetchone()[0]

        #Fetch all the venues
        venues = fetch_venue(cursor)

        #Input for venue. Only accept if it exists!
        count=0
        while(1):
            venue_name = str(input("Please Enter the venue name: "))
            for i in venues:
                if (venue_name == i):
                    count=1
                    break
            if count==1:
                break
            else:
                print("Please enter the correct venue from choices above!")

        #Get the venue id from the database
        venue_id_query = '''SELECT venue_id FROM venue where venue_name = ?'''
        cursor.execute(venue_id_query, (venue_name,))
        venue_id = cursor.fetchone()[0]

        #Get the available no. of game counts from a venue
        venue_count_query = '''SELECT games_available_count FROM venue where venue_id = ?'''
        cursor.execute(venue_count_query, (venue_id,))
        games_avail_count = cursor.fetchone()[0]

        inputs = [user_id,event_name,event_date,start_time,end_time,event_desc,capacity,event_cat_id,venue_id,create_or_join,sports_cat_id, games_avail_count]

        return inputs


# <a id="create-event"></a>

# In[10]:


# Triggering the create an event functionality
inputs2 = event_create_inputs(db)
if inputs2:
    new_event(db,inputs2)


# ## Function 4: Display timeslot availability at a venue
# Here we have considered that there can be simultaneous events at a venue and that is why we have asked the admin to enter the capacity of the venue to host multiple events at a given time stamp. The output of this function displays the available timeslots and their instances left for a given date and time.
# 
# Actionable sequence of this function: [Check](#find-slots)
# 
# > Asks user to enter the venue name and the date for which he wants to look at the available timeslots<br>
# > Calls the `find_booked_slots` function to print the time slot availability at that venue<br>
# > Fetches the Total capacity of the event to host simultaneous events<br>
# > Fetches the Open time and Close time of a venue using `fetch_venue_time` function<br>
# > Fetches the Start time and Close time of all events for that date using `fetch_event_time` function<br>
# > Maps the date with the times and the scripts find the booked slots and available slots for the given date at that venue<br>
# > Finally prints to the user the Total Available slots at that venue with the instances left for each slot<br>

# In[11]:


# Function to fetch the open and close timings of a venue
def fetch_venue_time(cursor, venue):  
    venue_avail_query = '''SELECT open_time, close_time FROM venue where venue_name = ?'''
    cursor.execute(venue_avail_query, (venue,) )
    venues = cursor.fetchall()
    return venues

# Function to fetch the start time and end time of an event
def fetch_event_time(cursor, venue, date):
    event_avail_query = '''SELECT start_time, end_time FROM venue, events where venue.venue_id = events.venue_id and venue_name = ? and events.date = ? '''
    cursor.execute(event_avail_query, (venue,date))
    events = cursor.fetchall()
    return events

# Function to fetch the counts of instances of event that can be hosted simultaneously at a venue at a given timestamp
def fetch_avail_slot(cursor, venue):
    venue_avail_query = '''SELECT games_total_count, games_available_count FROM venue where venue_name = ?'''
    cursor.execute(venue_avail_query, (venue,) )
    count = cursor.fetchone()
    return count

# Function to count instances of a tuple in a list and then store it in a dictionary
def count(tuplelist): 
    dct = {} 
    for i in tuplelist: 
        dct[i] = dct.get(i, 0) + 1
    return dct

# Function to find the available timeslots at a venue for a given date
def find_booked_slots(db,venue,date,debug=True):
    cursor = db.cursor()
    venues = fetch_venue_time(cursor, venue)
#     print(venues)
    games_avail_count = fetch_avail_slot(cursor, venue)

    booked_slots = []
    event_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    open_time = str(venues[0][0])
    close_time = str(venues[0][1])
    open_time = datetime.datetime.strptime(open_time, '%H').time()
    close_time = datetime.datetime.strptime(close_time, '%H').time()

    event_times = fetch_event_time(cursor, venue, date)
#     print(event_times)
    for i in event_times:
        start_time = str(i[0]) 
        end_time = str(i[1])

        start_time = datetime.datetime.strptime(start_time, '%H').time()
        end_time = datetime.datetime.strptime(end_time, '%H').time()
        #  print(start_time, end_time)
        #  print("Hey")
        #  booked_slots= [((datetime.datetime.combine(event_date,start_time)), (datetime.datetime.combine(event_date,end_time)))]
        #  print(booked_slots)
        #  print(datetime.datetime.combine(event_date,start_time).date()
        booked_slots.append(((datetime.datetime.combine(event_date,start_time)), (datetime.datetime.combine(event_date,end_time))))
    total_hours = ((datetime.datetime.combine(event_date,open_time)), (datetime.datetime.combine(event_date,close_time)))

    duration=timedelta(hours=1)
    slots = sorted([(total_hours[0],total_hours[0])]+ booked_slots + [(total_hours[1],total_hours[1])])
    if debug==True:
        print("-----Time Slots Avalibility at " + venue + "----\n")
        print("Time slot\tInstances left")
    for start, end in ((slots[i][1], slots[i+1][0]) for i in range(len(slots)-1)):
    #     assert start <= end, "Cannot attend all appointments"
        while start + duration <= end:
            if games_avail_count!=0 :
                if debug==True:
                    print ("{:%H:%M} - {:%H:%M}".format(start, start + duration) + "\t" + "(" + str(games_avail_count[0]) + ")")
                start += duration
    hours = []    
    for time,end in booked_slots:   

        while time <= end:
            hours.append(time)
            time += datetime.timedelta(hours=1)

    hours = (sorted(hours))    
#     print(hours)
    temp = []
    i=0
    while(i < len(hours)-1):
        temp.append((hours[i],hours[i]+timedelta(hours=1)))
        i+=1
#     print(temp)
    temp1 = count(temp)
    
    end_time_list = [j for i,j in event_times]
#     print(temp1)
    for i in end_time_list:
        for j in temp1:
            if j[0].hour == i: 
                temp1[j] = temp1[j]-1
#     print(temp1)
    for items in temp1:
        if debug==True:
            print("{:%H:%M} - {:%H:%M}".format(items[0],items[1]) + "\t" + "(" + str(games_avail_count[0]-temp1[items]) + ")")  
    return temp1


# <a id="find-slots"></a>

# In[12]:


# Triggering the function to find the available slots at a particular venue for the given date. It also provided the instances left for that timeslot 
date = str(input("Please enter a date in yyyy-mm-dd format: "))
venue = str(input("Please enter the venue name"))
temp1 = find_booked_slots(db,venue,date)


# # Function 5 : Display all venues where a particular timeslot is available
# 
# Here we are displaying all venue names that are available in time slot provided by the user. 
# 
# Actionable sequence for this function: [Check](#find-venues)
# > Asks the user for Date, Start time and End time<br>
# > Calls the `event_date_strp` function to find the list of available venues for that timeslot<br>
# > Fetches the venue list<br>
# > For each veneue, it runs the `find_booked_slots` functions to find the booked slots and then matches it with the required slot<br>
# > Select all the venues which have an instance left for that timeslot on a given day and returns<br>
# > Prints all the available venues at that time slot<br>

# In[13]:


# Function to return a list of available venues for a given timeslot
def display_venues_given_time(db, event_date, start_time, end_time):
    
    cursor = db.cursor()
    
    event_date_strp = datetime.datetime.strptime(event_date, '%Y-%m-%d').date()
    
    venue_query = '''SELECT venue_name FROM venue'''
    cursor.execute(venue_query)
    venues = cursor.fetchall()
    venue_list = []
    
    for i in range(len(venues)):
        venue_list.append(venues[i][0])
    
#     print(venue_list)
    
    avail_venues = []
    for j in venue_list:
        temp1 = find_booked_slots(db, j, event_date, False)
        if temp1=={}:
            avail_venues.append(j)
        else:
            initial_time = datetime.datetime.strptime(start_time, '%H').time()
            finish_time = datetime.datetime.strptime(end_time, '%H').time()

            initial_datetime = datetime.datetime.combine(event_date_strp,initial_time)
            finish_datetime = datetime.datetime.combine(event_date_strp,finish_time)

            timestamp = (initial_datetime, finish_datetime)

            for items in temp1:
                if items == timestamp and temp1[items]!=0:
                    avail_venues.append(j)
                    
    return avail_venues


# <a id="find-venues"></a>

# In[14]:


# Triggering the function to display the available venues for the required timeslot at a given date
event_date = str(input("Please Enter the event date in yyyy-mm-dd format: "))
start_time = str(input("Please Enter the start time in hrs: "))
end_time   = str(input("Please Enter the end time in hrs: "))

avail_venues = display_venues_given_time(db, event_date, start_time, end_time)
print("\nThe available venues for the required timeslot are: ")
for i in range(len(avail_venues)):
    print(str(i) + ":" + avail_venues[i])
# print(available_venues)


# # Function 6 : Display all events for a particular venue for given date and time
# Here we are displaying all events for a venue, date and time provided by the user
# 
# Actionable sequence of this function: [Check](#find-events)
# > Asks the user to input the date and the start time for events he/she may be looking for<br>
# > Calls the `display_events_given_time` function to find all the events at that venue with a start time equal to what user provided<br>
# > Displays the list of venues using `fetch_venue` function and asks the user to select a venue<br>
# > Fetches and prints all the events at that venue for a given date and time<br>

# In[15]:


# Function to display the events at a particular venue for the given timestamp
def display_events_given_time(cursor, event_date, start_time):
    
#     end_time   = str(input("Please Enter the end time in hrs: "))
    venues = fetch_venue(cursor)
    #Input for venue. Only accept if it exists!
    count=0
    while(1):
        venue_name = str(input("Please Enter the venue name: "))
        for i in venues:
            if (venue_name == i):
                count=1
                break
        if count==1:
            break
        else:
            print("Please enter the correct venue from choices above!")
    
    display_event = ''' select e.event_name 
                        from events e, venue v 
                        where e.venue_id = v.venue_id
                        and e.date = ? and e.start_time = ? and v.venue_name = ?'''
    
    cursor.execute(display_event, (event_date,start_time,venue_name,) )
    events = cursor.fetchall()
    if events:
        print("Available events on for given time and date are: ",events)
    else:
        print("No events available")


# <a id="find-events"></a>

# In[16]:


#Triggering the function to display all the events at a venue for a given timestamp
event_date = str(input("Please Enter the event date in yyyy-mm-dd format: "))
start_time = str(input("Please Enter the start time in hrs: "))
display_events_given_time(cursor, event_date, start_time)


# # Function 7 : User joins an event
# Below is the function called if user inputs to join an event
# 
# Actionable sequence for this event: [Check](#join-event)
# > Calls the `join_event` function to let user enter an event<br>
# > Displays the sports using `fetch_sport` function and asks user to select a sport<br>
# > Asks user to enter the event date, start time and end time<br>
# > Fetches the event categories (play/watch/workshop) using `fetch_event_cat` function and asks user to select one<br>
# > If an event matches with the provided info then joins the user else returns "No such event exists"
# > Fetches the capacity available for the event and updates it after the user joins. Also, displays the remaining capacity for the event<br>

# In[17]:


# Function to join an event
def join_event(db):
    #Fetch the list of sports 
    
    sports = fetch_sport(cursor)
    
    #Input for sport. Only accept if it exists!
    while(1):
        sport_name = str(input("Please Enter the sport name: "))
        for i in sports:
            if (sport_name == i):
                count=1
                break
        if count==1:
            break
        else:
            print("Please enter the correct sport from choices above!")

    #Get the sport id from the database
    sports_cat_id_query = '''SELECT sports_cat_id FROM sports_cat where sport_name = ?'''
    cursor.execute(sports_cat_id_query, (sport_name,))
    sports_cat_id = cursor.fetchone()[0]
    
    event_date = str(input("Please Enter the event date: "))
    start_time = str(input("Please Enter the start time in hrs: "))
    end_time   = str(input("Please Enter the end time in hrs: "))
    
    #Fetch all event categories
    fetch_event_cat(cursor)
    
    #Input for event category. Only accept if it exists!
    while(1):
        event_category_name = str(input("Please Enter the event category name : "))
        if (event_category_name == "watch" or event_category_name == "play" or event_category_name == "workshop" ):
            # see if event is available
            find_event = '''SELECT ec.event_category_name FROM events e, event_category ec where 
                            e.event_cat_id = ec.event_cat_id and
                            e.date = ? and e.start_time = ? and e.end_time = ?'''
            cursor.execute(find_event, (event_date, start_time, end_time,))
            if cursor.fetchone()[0] == event_category_name:
                print("User joined the event")
                break
            else:
                print("No such event exists")
    
    #Show all available slots
    find_event = '''SELECT capacity_avail FROM events where date = ? and start_time = ? and end_time = ?'''
    cursor.execute(find_event, (event_date, start_time, end_time,))
    capacity_avail = cursor.fetchone()[0]
    
    # update the table events by adding a member
    join_event = '''UPDATE events SET capacity_avail = ? where date = ? and start_time = ? and end_time = ?'''
    cursor.execute(join_event, (capacity_avail-1, event_date, start_time, end_time,))
#     update_capacity = cursor.fetchone()
    print("capacity now available is : ",capacity_avail-1)
    
    db.commit()
    


# <a id="join-event"></a>

# In[18]:


#Triggering the join an event function
join_event(db)


# # Function 8 : Remove an event
# Here we are deleting the event entry based on admin's selected event_id. This is an admin only activity.
# 
# Actionable sequence for this function: [Check](#delete-event)
# 
# > Asks for the admin email-id and verifies it using the `admin_check` function<br>
# > Confirms if the user wants to delete the event<br>
# > Asks the admin to enter the event id he wants to delete<br>
# > Deletes the event from the database and updates the database<br>

# In[19]:


# Function to delete an event using event_id. Only admin is allowed to do so.
def delete_an_event(db):
    cursor = db.cursor()
    email = str(input("Please provide your email-address: "))
    email = admin_check(db, email)
    
    delete_or_not = str(input("Do you want to delete an event?y/n: "))
    
    if delete_or_not == "y":
        event_id = str(input("Please provide event_id you want to delete: "))
        select_event_id = '''SELECT * FROM events where event_id = ? '''
        present = cursor.execute(select_event_id, (event_id,)) 
        if present:
            delete_an_event = '''DELETE FROM events where event_id = ?'''
            cursor.execute(delete_an_event, (event_id,))  
            db.commit()
            print("The event is deleted")
        else:
            print("The event_id is not present in events database. Check again")


# <a id="delete-event"></a>

# In[20]:


#Triggering the delete an event fucntion
delete_an_event(db)


# In[21]:


db.close()

