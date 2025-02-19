from tkinter import *

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

#Login button
login_button = Button(window, text="Login")
login_button.pack(pady=5)

#Runs application
window.mainloop() #This will place a window on the screen and listen for events.
print("FeatherBank application closed.")