# IIT Assignment3 SecureMyBike_BE.py v1.08may22 author:grantn

from PIL import ImageTk, Image
import mysql.connector

#-User Class Start---------------------------------------------------------------------------
class User:
    def __init__(self, user_id, f_name, l_name, dob, address, phone, email, password):
        self.__user_id = user_id
        self.__f_name = f_name
        self.__l_name = l_name
        self.__dob = dob
        self.__address = address
        self.__phone = phone
        self.__email = email
        self.__password = password

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id):
        self.__user_id = user_id

    @property
    def f_name(self):
        return self.__f_name

    @f_name.setter
    def f_name(self, f_name):
        self.__f_name = f_name

    @property
    def l_name(self):
        return self.__l_name

    @l_name.setter
    def l_name(self, l_name):
        self.__l_name = l_name

    @property
    def dob(self):
        return self.__dob

    @dob.setter
    def dob(self, dob):
        self.__dob = dob

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    def __str__(self):
        return (self.user_id, self.f_name, self.l_name, self.dob, self.address, self.phone, self.email, self.password)
        
#-User Class End-----------------------------------------------------------------------------


#-Item Class Start---------------------------------------------------------------------------
class Item:
    def __init__(self, bike_id, make, model, colour, serial_number, place_of_purchase, proof_of_purchase, status):
        self.__bike_id = bike_id
        self.__make = make
        self.__model = model
        self.__colour = colour
        self.__serial_number = serial_number
        self.__place_of_purchase = place_of_purchase
        self.__proof_of_purchase = proof_of_purchase
        self.__status = status
 

    @property
    def bike_id(self):
        return self.__bike_id
        
    @bike_id.setter
    def bike_id(self, make):
        self.__bike_id = bike_id

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

    def __str__(self):
        return (self.bike_id, self.make, self.model, self.colour, self.serial_number, self.place_of_purchase, self.proof_of_purchase, self.status) 

        
#-Item Class End------------------------------------------------------------------------------------


#-UserManager Class Start---------------------------------------------------------------------------
class UserManager:
    def __init__(self):
        self.user_info = []
        self.bike_info = []
        
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
                        

    # Add a user
    def add_user(self, f_name, l_name, dob, address, phone, email, password):
        self.sql = "INSERT INTO users (f_name, l_name, dob, address, phone, email, password) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        self.val = (f_name, l_name, dob, address, phone, email, password)
        self.mycursor.execute(self.sql, self.val)
        self.mydb.commit()
    
    # Check for a user
    def check_user(self, new_email):
        email_spotted = 0
        self.mycursor.execute("SELECT email FROM users WHERE email = '"+ new_email +"'")
        myresult = self.mycursor.fetchall()
        for i in myresult:
            if new_email in i:
                email_spotted = 1
        return email_spotted
    
    # Login - Verify User
    def login(self, email, check_password):
        check_passwd = 0
        myresult = None
        self.mycursor.execute("SELECT * FROM users WHERE email = '"+ email +"'")
        myresult = self.mycursor.fetchall()
        acc_info_tuple = myresult[0] 
        user_id, f_name, l_name, dob, address, phone, email, password = acc_info_tuple
        if password == check_password:
                check_passwd = 1
                self.user_info.append(User(user_id, f_name, l_name, dob, address, phone, email, password))
        return check_passwd

    def logout(self):
        self.user_info.clear()
        self.bike_info.clear()

    def first_name(self):
        first_name = self.user_info[0].f_name
        return (first_name)

    def account_details(self):
        acc_details ="First name: "+self.user_info[0].f_name+"\n"
        acc_details +="Last name: "+self.user_info[0].l_name+"\n"
        acc_details +="D.O.B.: "+self.user_info[0].dob+"\n"
        acc_details +="Address: "+self.user_info[0].address+"\n"
        acc_details +="Phone: "+self.user_info[0].phone+"\n"
        acc_details +="Email: "+self.user_info[0].email+"\n"           
        return (acc_details)

#--Item Control ----------------------------------------------------------------------------------------
    
    def add_item(self, make, model, colour, serial_number, place_of_purchase, proof_of_purchase, status):
        user_id = self.user_info[0].user_id
        self.sql = "INSERT INTO items (user_id, make, model, colour, serial_number, place_of_purchase, proof_of_purchase, status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        self.val = (user_id, make, model, colour, serial_number, place_of_purchase, proof_of_purchase, status)
        self.mycursor.execute(self.sql, self.val)
        self.mydb.commit()
        self.bike_info.append(Item(user_id, make, model, colour, serial_number, place_of_purchase, proof_of_purchase, status))
    
    # Check for an item
    def check_item(self, new_serial):
        serial_spotted = 0 
        self.mycursor.execute("SELECT * FROM items WHERE serial_number= '"+ new_serial +"'")
        myresult = self.mycursor.fetchall()
        try:
            items_info_tuple = myresult
            serial_number = items_info_tuple
            if new_serial == serial_number:
                serial_spotted = 1
        except IndexError:
            pass
        return serial_spotted

    def item_list(self):
        index = 0
        i_list = ""
        myresult = None
        if self.bike_info == []:         
            self.mycursor.execute("SELECT * FROM items WHERE user_id = '"+ str(self.user_info[0].user_id) +"'")
            myresult = self.mycursor.fetchall()
            for row in myresult:
                item_info_tuple = row
                bike_id, user_id, make, model, colour, serial_number, place_of_purchase, proof_of_purchase, status = item_info_tuple
                self.bike_info.append(Item(bike_id, make, model, colour, serial_number, place_of_purchase, proof_of_purchase, status))
                i_list += (str(index+1))+": "+self.bike_info[index].make+", "+self.bike_info[index].model+", "+self.bike_info[index].serial_number+", "+self.bike_info[index].status+"\n"
                index += 1
        else:
            while index < len(self.bike_info):
                i_list += (str(index+1))+": "+self.bike_info[index].make+", "+self.bike_info[index].model+", "+self.bike_info[index].serial_number+", "+self.bike_info[index].status+"\n"
                index += 1
        return i_list

    def check_status(self, check_serial):
        serial_msg = "This serial does not have a registered user\n"
        self.mycursor.execute("SELECT status FROM items WHERE serial_number= '"+ check_serial +"'")
        myresult = self.mycursor.fetchall()
        for row in myresult:
            items_info_tuple = row
            serial_status, = items_info_tuple
            serial_status_str = str(serial_status)
            if serial_status_str == "Registered":
                serial_msg = "This serial is registered to a user\n"
            elif serial_status_str == "For Sale":
                serial_msg = "This serial is registered For Sale\n"
            elif serial_status_str == "Stolen":
                serial_msg = "This serial has been reported stolen\n"    
        return serial_msg

    def del_item(self, serial_number):
        self.mycursor.execute("DELETE FROM items WHERE serial_number = '"+serial_number+"'")
        self.bike_info = []
        i_list = self.item_list()
        return i_list

    def item_edit_list(self, item_sel):
        index = int(item_sel) - 1
        i_list = "\n\n1: "+self.bike_info[index].make+"\n"
        i_list +="2: "+self.bike_info[index].model+"\n"
        i_list +="3: "+self.bike_info[index].serial_number+"\n"
        i_list +="4: "+self.bike_info[index].status+"\n"
        i_list +="5: "+self.bike_info[index].place_of_purchase+"\n"
        i_list +="6: "+self.bike_info[index].proof_of_purchase+"\n"
        return i_list

    def item_edit(self, item_sel, field_sel_str, new_val):
        
        index = int(item_sel) - 1
        field_sel = int(field_sel_str)
        if field_sel == 1:
            self.bike_info[index].make = new_val
        elif field_sel == 2:
            self.bike_info[index].model = new_val
        elif field_sel == 3:
            self.bike_info[index].serial_number = new_val
        elif field_sel == 4:
            self.bike_info[index].status = new_val
        elif field_sel == 5:
            self.bike_info[index].place_of_purchase = new_val
        elif field_sel == 6:
            self.bike_info[index].proof_of_purchase = new_val
        elif field_sel == 7:
            self.sql = ("UPDATE items (make, model, serial_number, status, place_of_purchase, proof_of_purchase) VALUES (%s,%s,%s,%s,%s,%s)")
            self.val = (self.bike_info[index].make, self.bike_info[index].model, self.bike_info[index].serial_number, self.bike_info[index].status, self.bike_info[index].place_of_purchase, self.bike_info[index].proof_of_purchase)
            self.mycursor.execute(self.sql, self.val)
            self.mydb.commit()
        elif field_sel == 8:
            self.bike_info = []
            self.item_list()
            
    
#-UserManager Class End---------------------------------------------------------------------------
