# IIT Assignment3 SecureMyBike_BE.py v1.08may22 author:grantn

from PIL import ImageTk, Image
import mysql.connector

#-User Class Start---------------------------------------------------------------------------
class User:
    def __init__(self, f_name, l_name, dob, address, phone, email, password):
        self.__f_name = f_name
        self.__l_name = l_name
        self.__dob = dob
        self.__address = address
        self.__phone = phone
        self.__email = email
        self.__password = password
##        self.__user_img = user_img

    # First Name
    @property
    def f_name(self):
        return self.__f_name

    @f_name.setter
    def f_name(self, f_name):
        self.__f_name = f_name

    # Last Name
    @property
    def l_name(self):
        return self.__l_name

    @l_name.setter
    def l_name(self, l_name):
        self.__l_name = l_name

    # Date of Birth
    @property
    def dob(self):
        return self.__dob

    @dob.setter
    def dob(self, dob):
        self.__dob = dob

    # Address
    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    # Phone Number
    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    #Email
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    #Email
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password


##    #User Image
##    @property
##    def user_img(self):
##        return self.__user_img
##
##    @user_img.setter
##    def email(self, user_img):
##        self.__user_img = user_img
        
#-User Class End---------------------------------------------------------------------------


#-Item Class Start---------------------------------------------------------------------------
class Item:
    def __init__(self, make, model, colour, serial_number, place_of_purchase, proof_of_purchase, status):
        self.__make = make
        self.__model = model
        self.__colour = colour
        self.__serial_number = serial_number
        self.__place_of_purchase = place_of_purchase
        self.__proof_of_purchase = proof_of_purchase
        self.__status = status

    @property
    def make(self):
        return self.__make
        
    @make.setter
    def make(self, make):
        self.__make = make
         
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def colour(self):
        return self.__colour

    @colour.setter
    def colour(self, colour):
        self.__colour = colour
    
    @property
    def serial_number(self):
        return self.__serial_number  

    @serial_number.setter
    def serial_number(self, serial_number):
        self.__serial_number = serial_number
    
    @property
    def place_of_purchase(self):
        return self.__place_of_purchase 

    @place_of_purchase.setter
    def place_of_purchase(self, place_of_purchase):
        self.__place_of_purchase = place_of_purchase
    
    @property
    def proof_of_purchase(self):
        return self.__proof_of_purchase

    @proof_of_purchase.setter
    def proof_of_purchase(self, proof_of_purchase):
        self.__proof_of_purchase = proof_of_purchase
          
    @property
    def status(self):
        return self.__status 

    @status.setter
    def status(self, status):
        self.__status = status

        
#-Item Class End-----------------------------------------------------------------------------


#-UserManager Class Start---------------------------------------------------------------------------
class UserManager:
    def __init__(self):

        self.mydb = mysql.connector.connect(
        host="bqbjw0okdcewzqeo5swt-mysql.services.clever-cloud.com",
        user="uwvzaqz89axgep1k",
        passwd="efTB17fQfWVImVWxZPFI",
        database="bqbjw0okdcewzqeo5swt")

        self.mycursor = self.mydb.cursor()
        self.mycursor.execute("""CREATE TABLE IF NOT EXISTS users (user_id int(11) NOT NULL AUTO_INCREMENT,
                              f_name VARCHAR(255) NOT NULL,
                              l_name VARCHAR(255),
                              dob VARCHAR(255),
                              address VARCHAR(255),
                              phone VARCHAR(255),
                              email VARCHAR(255),
                              password VARCHAR(255),
                              PRIMARY KEY (user_id))""")
        
        self.mycursor.execute("""CREATE TABLE IF NOT EXISTS items (bike_id int(11) NOT NULL AUTO_INCREMENT,
                              user_id int(11),
                              make VARCHAR(255),
                              model VARCHAR(255),
                              colour VARCHAR(255),
                              serial_number VARCHAR(255),
                              place_of_purchase VARCHAR(255),
                              proof_of_purchase VARCHAR(255),
                              status VARCHAR(255),
                              PRIMARY KEY (bike_id))""")
                        
        self.users = []
        self.current_user = [0,0]

    # Add a user
    def add_user(self, f_name, l_name, dob, address, phone, email, password):
        self.sql = "INSERT INTO users (f_name, l_name, dob, address, phone, email, password) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        self.val = (f_name, l_name, dob, address, phone, email, password)
        self.mycursor.execute(self.sql, self.val)
        self.mydb.commit()
    
    # Check for a user
    def check_user(self, email):
        email_spotted = 0
        index = 0
        while index < len(self.users):
            if email == self.users[index].email:
                email_spotted = 1
            index += 1      
        return email_spotted
    
    # Login - Verify User
    def login(self, email, password):
        email_pass = None
        index = 0
        while index < len(self.users):
            if email == self.users[index].email:
                email_pass = index
                if password == self.users[email_pass].password:
                    self.current_user[0] = 1
                    self.current_user[1] = email_pass
            index += 1    
        print(str(self.current_user) + " Marker login BE")    
        return self.current_user

    def logged_in(self):
        print("Marker logged_in BE")
        if self.users != []:
            current_logged_in = self.users[self.current_user[1]]
        else:
            current_logged_in = [0,0]
        return current_logged_in

    def account_details(self, account_num):
        print("marker Acc Details BE")
        return (self.users[account_num])

    # Display all users
    def display_all_users(self):
        self.mycursor.execute("SELECT * FROM users")
        myresult = self.mycursor.fetchall()
        for x in myresult:
            print(str(x))

    

#-UserManager Class End---------------------------------------------------------------------------
