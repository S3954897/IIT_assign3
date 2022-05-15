#IIT Assignment3 SecureMyBike_FE.py v1.08may22 author:grantn

import SecureMyBike_BE as bE
import tkinter as tk
from tkinter import X, messagebox
backend = bE.UserManager()

LARGE_FONT = ("Arial", 20,"bold")
MED_FONT = ("Arial", 16)
       
class Frame(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container=tk.Frame(self)
        container.pack()
        container.grid_rowconfigure(0, minsize = 800)
        container.grid_columnconfigure(0, minsize = 500)

        self.frames = {}

        for i in (Page01, Page02, Page03, Page04):
            frame = i(container, self)
            self.frames[i] = frame
            frame.grid (row = 0, column = 0, sticky = "nsew")

        self.show_frame(Page01)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        self.title("Secure My Bike")

class Page01(tk.Frame):
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="First Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Visit Page 2",command=lambda:controller.show_frame(Page02))
        button1.place(x=200, y=750)

class Page02(tk.Frame):
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        label = tk.Label(self, text="Login", font=LARGE_FONT)
        label.grid(row=1,column=2)

        label1 = tk.Label(self,text="Email", font=MED_FONT)
        label1.grid(row=2,column=1)
        text_entry1 = tk.Entry(self, width = 30, bd = 2.5)
        text_entry1.grid(row=2,column=2)
        
        label2 = tk.Label(self,text="Password", font=MED_FONT)
        label2.grid(row=3,column=1)
        text_entry2 = tk.Entry(self, show = "*", width = 30, bd = 2.5)
        text_entry2.grid(row=3,column=2)
        text_entry1.bind("<Return>", lambda event: text_entry2.focus())
        text_entry2.bind("<Return>", lambda event: text_entry1.focus())

        def login_fun():          
            account_verified = backend.login(text_entry1.get(), text_entry2.get())
            if account_verified[0] != 0:
                controller.show_frame(Page04)
            else:
                messagebox.showerror("Error", "There is no matching account for this email")
            
        button1 = tk.Button(self, text="Login",command=lambda:login_fun())
        button1.grid(row=4,column=2)

        button2 = tk.Button(self, text="Register",command=lambda:controller.show_frame(Page03))
        button2.grid(row=5,column=2)


class Page03(tk.Frame):
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self,parent)
        labelH = tk.Label(self,text="New User Registration", font=LARGE_FONT)
        labelH.pack(pady=10,padx=10)
        
        label1 = tk.Label(self,text="First Name", font=MED_FONT)
        label1.pack(pady=5,padx=5)
        text_entry1 = tk.Entry(self, width = 30, bd = 2.5)
        text_entry1.pack(pady=10,padx=10)
        
        label2 = tk.Label(self,text="Last Name", font=MED_FONT)
        label2.pack(pady=5,padx=5)
        text_entry2 = tk.Entry(self, width = 30, bd = 2.5)
        text_entry2.pack(pady=10,padx=10)
        
        label3 = tk.Label(self,text="Date of Birth", font=MED_FONT)
        label3.pack(pady=5,padx=5)
        text_entry3 = tk.Entry(self, width = 30, bd = 2.5)
        text_entry3.pack(pady=10,padx=10)
        
        label4 = tk.Label(self,text="Address", font=MED_FONT)
        label4.pack(pady=5,padx=5)
        text_entry4 = tk.Entry(self, width = 30, bd = 2.5)
        text_entry4.pack(pady=0,padx=0)
        text_entry5 = tk.Entry(self, width = 30, bd = 2.5)
        text_entry5.pack(pady=0,padx=0)
        
        label6 = tk.Label(self,text="Phone Number", font=MED_FONT)
        label6.pack(pady=5,padx=5)
        text_entry6 = tk.Entry(self, width = 30, bd = 2.5)
        text_entry6.pack(pady=10,padx=10)
        
        label7 = tk.Label(self,text="Email", font=MED_FONT)
        label7.pack(pady=5,padx=5)
        text_entry7 = tk.Entry(self, width = 30, bd = 2.5)
        text_entry7.pack(pady=10,padx=10)

        label8 = tk.Label(self,text="Password", font=MED_FONT)
        label8.pack(pady=5,padx=5)
        text_entry8 = tk.Entry(self, show = "*", width = 30, bd = 2.5)
        text_entry8.pack(pady=10,padx=10)
        
        text_entry1.bind("<Return>", lambda event: text_entry2.focus())
        text_entry2.bind("<Return>", lambda event: text_entry3.focus())
        text_entry3.bind("<Return>", lambda event: text_entry4.focus())
        text_entry4.bind("<Return>", lambda event: text_entry5.focus())
        text_entry5.bind("<Return>", lambda event: text_entry6.focus())
        text_entry6.bind("<Return>", lambda event: text_entry7.focus())
        text_entry7.bind("<Return>", lambda event: text_entry8.focus())
        text_entry8.bind("<Return>", lambda event: text_entry1.focus())

        button1 = tk.Button(self, text="Back to Start",command=lambda:controller.show_frame(Page01))
        button1.place(x=200, y=750)
        
        def submit():
            backend.add_user(text_entry1.get(),text_entry2.get(),text_entry3.get(),(text_entry4.get()+" "+text_entry5.get()),text_entry6.get(),text_entry7.get(),text_entry8.get())
            text_entry1.delete(0, tk.END)
            text_entry2.delete(0, tk.END)
            text_entry3.delete(0, tk.END)
            text_entry4.delete(0, tk.END)
            text_entry5.delete(0, tk.END)
            text_entry6.delete(0, tk.END)
            text_entry7.delete(0, tk.END)
            text_entry8.delete(0, tk.END)
            controller.show_frame(Page02)
            (backend.display_all_users())
        
        button2 = tk.Button(self, text="Submit",command =lambda: submit())
                                                                                                                                                                                                                                                 
        button2.place(x=200, y=700)

        button3 = tk.Button(self, text="List",command = lambda: backend.display_all_users())                                                                 
        button3.place(x=200, y=650)

class Page04(tk.Frame):
    def __init__ (self, parent, controller):
        user_details = []
        def logged_in_func():
            logged_in = backend.logged_in(self)
            if (logged_in[0]) == 1:
                print("Marker Page 4")
                print(logged_in[1])
                current_user = backend.account_details(logged_in[1])
            return current_user  
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Home Screen", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        label1 = tk.Label(self, text="Temp",font=MED_FONT)
        label1.pack(pady=10,padx=10)
        label1.after(10, user_details = logged_in_func())
        print(str(user_details[0]))

    

        button1 = tk.Button(self, text="Visit Page 2",command=lambda:controller.show_frame(Page02))
        button1.place(x=200, y=750)


app = Frame()
app.mainloop()

        
