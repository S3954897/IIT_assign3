#IIT Assignment3 SecureMyBike_FE_Raw.py v1.08may22 author:grantn

import sys
import os
from turtle import clear
import SecureMyBike_BE as bE


class SecureMyBikeUI:
    def __init__(self):
        self.backend = bE.UserManager()
        self.page_control()
    
    @staticmethod
    def get_str() -> str:
        user_input = sys.stdin.readline().strip()
        return user_input

    @staticmethod
    def get_int(self) -> int:
        user_input = sys.stdin.readline().strip()
        return user_input
    
    @staticmethod
    def terminal_out(terminal_msg: str)->None:
        sys.stdout.write(terminal_msg)
    
    def page_control(self):
        app_active = True
        page_menu_active = 1
        new_user_step = 0

        while app_active == True:
           
            #Page-1 Start1
            while page_menu_active == 1:
                os.system('clear')
                msg = ""
                msg += "\n\nStart Screen\n\n"
                msg += "1 - Login Screen\n"
                msg += "2 - New User Registration\n"

                self.terminal_out(msg)
                self.action = self.get_str()
                
                if self.action == "1":
                    page_menu_active = 2

                elif self.action == "2":
                    page_menu_active = 3
                
                else:
                    msg = "Incorrect selection, Try again.\n"
                    self.terminal_out(msg)
                    msg = ""

            #Page-2 Login
            while page_menu_active == 2:
                os.system('clear')
                email_spotted = 1
                user_active = 0
                msg = ""
                msg += "\n\nLogin\n\n"
                msg += "Email: "
                self.terminal_out(msg)
                self.email = self.get_str()
                msg = "Password: "
                self.terminal_out(msg)
                self.password = self.get_str()
                email_spotted = self.backend.check_user(self.email)
                if email_spotted == 0:
                    msg = "This is not registered a email"
                    self.terminal_out(msg)
                else:
                    check_passwd = self.backend.login(self.email, self.password)
                    if check_passwd == 1:
                        page_menu_active = 4
                    else:
                        msg = "Password incorrect"
                        self.terminal_out(msg)

            #Page - 3 User Registration
            while page_menu_active == 3:
                os.system('clear')
                msg = "\n\nNew User Registration\n\n"
                self.terminal_out(msg)    
                
                new_user_step = 1
                while new_user_step == 1:

                    msg = "Enter your first name: "
                    self.terminal_out(msg)
                    self.f_name = self.get_str()

                    msg = "Enter your last name: "
                    self.terminal_out(msg)
                    self.l_name = self.get_str()

                    email_spotted = 1
                    while email_spotted == 1:
                        msg = "Enter your email: "
                        self.terminal_out(msg)
                        self.email = self.get_str()
                        email_spotted = self.backend.check_user(self.email)
                        if email_spotted == 1:
                            msg = "This email address is already registered!\n"
                            msg += "1 - Go to login screen\n"
                            msg += "2 - Change your email address\n"
                            self.terminal_out(msg)
                            self.action = self.get_str()
                            if self.action == "1":
                                page_menu_active = 2 
                                new_user_step = 0
                                email_spotted = 2

                        elif email_spotted == 0:
                            msg = "Enter a password: "
                            self.terminal_out(msg)
                            self.password = self.get_str()
                            self.dob = "Update in your account settings"
                            self.phone = "Update in your account settings"
                            self.address = "Update in your account settings"
                            self.backend.add_user(self.f_name, self.l_name, self.dob, self.address, self.phone, self.email, self.password)
                            new_user_step = 0
                            page_menu_active = 2

            #Page-4 User Home
            while page_menu_active == 4:
                acc_details = self.backend.logged_in(self.email)
                
                msg = "\n\nUser Home\n\n"
                msg += "You are logged as \n\n"+self.backend.first_name()+"\n\n\n"
                msg += "1 - Account details\n"
                msg += "2 - Check a serial number\n"
                msg += "3 - My bike list\n"
                msg += "4 - Logout\n"
                
                self.terminal_out(msg)
                self.action = self.get_str()
                
                if self.action == "1":
                    page_menu_active = 5

                elif self.action == "2":
                    page_menu_active = 8

                elif self.action == "3":
                    page_menu_active = 9

                elif self.action == "4":
                    page_menu_active = 2
                
                else:
                    msg = "Incorrect selection, Try again.\n"
                    self.terminal_out(msg)
                    msg = ""

            #Page-5 Account Details
            while page_menu_active == 5:
                msg = "\n\nAccount Details\n\n"
                msg += self.backend.account_details()+"\n\n\n"
                msg += "1 - Home\n"
                msg += "2 - Edit Details\n"
                msg += "3 - Terms and Conditions\n"
                
                self.terminal_out(msg)
                self.action = self.get_str()

                if self.action == "1":
                    page_menu_active = 4

                elif self.action == "2":
                    #page_menu_active = ??
                    pass

                elif self.action == "3":
                    #page_menu_active = ??
                    pass
                
                else:
                    msg = "Incorrect selection, Try again.\n"
                    self.terminal_out(msg)
                    msg = ""

            #Page-6 Account Edit
            while page_menu_active == 6:
                pass

            #Page-7 Terms/Conditions
            while page_menu_active == 7:
                pass

            #Page-8 Check Serial Number
            while page_menu_active == 8:
                pass

            #Page-9 Item List
            while page_menu_active == 9:
                msg = "\n\nBike list\n\n"
                msg += self.backend.item_list()+"\n\n\n"
                msg += "1 - Add a new bike\n"
                msg += "2 - Edit a bike\n"
                msg += "3 - Home\n"
                
                self.terminal_out(msg)
                self.action = self.get_str()

                if self.action == "1":
                    page_menu_active = 10

                elif self.action == "2":
                    page_menu_active = 11
                    pass

                elif self.action == "3":
                    page_menu_active = 4
                    pass
                
                else:
                    msg = "Incorrect selection, Try again.\n"
                    self.terminal_out(msg)
                    msg = ""

            #Page-8 Add item
            while page_menu_active == 10:
                msg = "\n\nAdd a bike\n\n"
                self.terminal_out(msg)    
                
                new_item_dup = 1
                while new_item_dup == 1:
                    msg = "Enter the bike serial number: "
                    self.terminal_out(msg)
                    self.serial_number = self.get_str()


            #Page-8 Edit item
            while page_menu_active == 11:
                pass



app = SecureMyBikeUI()
                       
 

