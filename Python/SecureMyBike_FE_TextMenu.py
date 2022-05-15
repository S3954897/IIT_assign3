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
           
            #Page-1 Start
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
                msg = ""
                msg += "\n\nLogin\n\n"
                msg += "1 - Display all users\n"
                msg += "2 - New User Registration\n"

                self.terminal_out(msg)
                self.action = self.get_str()
            
                if self.action == "1":
                    wait = 1
                    self.backend.display_all_users()
                    while wait == 1:
                        msg = "1 - to continue: "
                        self.terminal_out(msg)
                        self.action = self.get_str()
                        wait = 0

                elif self.action == "2":
                    page_menu_active = 3
                
                else:
                    msg = "Incorrect selection, Try again.\n"
                    self.terminal_out(msg)
                    msg = ""

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
                            self.dob = ""
                            self.phone = ""
                            self.address = ""
                            self.backend.add_user(self.f_name, self.l_name, self.dob, self.address, self.phone, self.email, self.password)
                            new_user_step = 0
                            page_menu_active = 2


                # while new_user_step == 2:


                #     os.system('clear')
                #     msg = "\n\nNew User Registration\n\n"
                #     self.terminal_out(msg)

                #     msg = "Enter your Date of Birth: "
                #     self.terminal_out(msg)
                #     self.dob = self.get_str()

                #     msg = "Contact Phone Number: "
                #     self.terminal_out(msg)
                #     self.phone = self.get_str()

                #     msg = "Address: "
                #     self.terminal_out(msg)
                #     self.address = self.get_str()


            #Page-4 User Home
            while page_menu_active == 4:
                msg = ""
                msg += "\n\nUser Home\n\n"
                msg += "1 - Login Screen\n"
                msg += "2 - Exit\n"

                self.terminal_out(msg)
                self.action = self.get_str()
                
                if self.action == "1":
                    print("action 1")
                    page_menu_active = 2

                elif self.action == "2":
                    print("action 2")
                    app_active = False
                
                else:
                    msg = "Incorrect selection, Try again.\n"
                    self.terminal_out(msg)
                    msg = ""



app = SecureMyBikeUI()
                       
 

