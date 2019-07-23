
# Adding a new user

def new_user(db):


    cursor = db.cursor()
    

    while(1):
        email = str(input("Please provide your email-address: "))
        findEmail = '''SELECT * FROM user where email_id = ?'''

        cursor.execute(findEmail, (email,))

        if cursor.fetchall():
            print("Email already registered, enter again")

        else:

            first_name = str(input("Please Enter your first name: "))
            last_name = str(input("Please Enter your last name: "))
            contact_number = str(input("Please provide a valid contact number: "))
            zip_code = str(input("Your zip code: "))
            password = str(input("Enter the password: ")) # NEED to add constraints
            password_check = str(input("Enter the password again to recheck: "))

            while password!=password_check:
                password = str(input("Your passwords did not match, try again: "))
                password_check = str(input("Enter the password again to recheck: "))

            query = '''INSERT INTO user(email_id,first_name,last_name,contact_number, zip_code, password)
                            VALUES(?,?,?,?,?,?)'''
                
            cursor.execute(query, (email, first_name, last_name, contact_number,  zip_code, password, password_check))  
            db.commit()
            break



def new_venue(db, admin):
    
    cursor = db.cursor()

    email = str(input("Please enter your email address: "))

    while email != admin:
        print("You are not authorized to add a venue")
        email = str(input("Enter your email address again: "))
    
    venue_name = str(input("Please Enter the venue name: "))
    address = str(input("Please Enter the venue address: "))
    zip_code = str(input("Venue zip code: "))
    contact_number = str(input("Please provide a contact number: "))
    description = str(input("Enter the venue description (not more than 200 characters): ")) # Need to limit the length of input

    query = '''INSERT INTO venue(venue_id, venue_name, address, zip_code, contact_number, description)
                VALUES(?,?,?,?,?)'''

    # cursor = db.cursor()
    cursor.execute(query, (venue_name, address, zip_code, contact_number, description)) 




