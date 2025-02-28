from tkinter import *
from Database import login_user #Importing function from Database.py which handles login verification. 

#Function to handle login button click
def login():
    email = email_entry.get()
    pin = pin_entry.get()

    if login_user(email, pin):
        status_label.config(text='Login successful!', fg='green')
    else:
        status_label.config(text='Invalid email or PIN', fg='red')


#Window/Client code
window = Tk() #instantiates an instance of a window. 
window.geometry("500x500")
window.title("FeatherBank Login")
window.config(background="#161616") #Dark mode

#Main title label
title_label = Label(window, text="FeatherBank", font=("Arial", 20))
title_label.pack (pady=10)

#Instruction label
instruction_label = Label(window, text="Please enter your email and PIN", font=("Arial", 12))
instruction_label.pack (pady=10)

#Frame to align labels and entry boxes
frame = Frame(window, bg="#161616")
frame.pack(pady=10)

#Email label and entry
email_label = Label(frame, text='Email:', font=('Arial',12), bg="#161616", fg="white")
email_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

email_entry = Entry(frame, width=30)
email_entry.grid(row=0, column=1, pady=5)

#PIN and entry
pin_label = Label(frame, text="PIN:", font=('Arial',12), bg="#161616", fg="white")
pin_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

pin_entry = Entry(frame, width=30, show="*")
pin_entry.grid(row=1, column=1, padx=5)

#Login button (calls login function)
login_button = Button(window, text="Login", command=login, bg="#4CAF50", fg="white")
login_button.pack(pady=10)

#Status Message (Login success/fail message)
status_label = Label(window, text="", bg="#161616", fg="white")
status_label.pack()

#Runs application
window.mainloop() #This will place a window on the screen and listen for events.
print("FeatherBank application closed.")