from tkinter import *
from Database import register_user #Importing the signup (register_user) function from Database.py


#Window/Client
window = Tk() #instantiates an instance of a window. 
window.geometry("500x500")
window.title("FeatherBank - Sign Up")
window.config(background="#161616") #Dark mode

#Labels and Entry Fields
Label(window, text="Sign Up", font=("Arial", 18), bg="#161616", fg="white").pack(pady=10)
Label(window, text="Email:", font=("Arial", 12), bg="#161616", fg="white").pack()
email_entry = Entry(window, width=30)
email_entry.pack(pady=5)

Label(window, text="Password:", font=("Arial", 12), bg="#161616", fg="white").pack()
password_entry = Entry(window, width=30, show="*")  # Hide password input
password_entry.pack(pady=5)

#Function to handle the below signup button
def signup():
    email = email_entry.get()
    password = password_entry.get()

    if email and password:
        register_user(email, password)
        status_label.config(text="Sign up successful!", fg="green")
    else:
        status_label.config(text="Please fill in all fields.")

#Signup Button
signup_button = Button(window, text="Sign Up", command=signup, bg="#4CAF50", fg="white")
signup_button.pack(pady=10)

#Status Message
status_label = Label(window, text="", bg="#161616", fg="white")
status_label.pack()

#Run the Tkinter app
window.mainloop()