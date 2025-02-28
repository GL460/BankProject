import sqlite3
import hashlib

# Connect to the database (or create one if it doesn't exist)
conn = sqlite3.connect("featherbank.db") # Connects to the database (or creates it)
cursor = conn.cursor() # Allows us to execute database commands

# Create users table (if not exists)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        balance REAL DEFAULT 0.00
    )
''')

conn.commit()
conn.close()

#Function which handles signups - storing their email and a securely hashed password.
def register_user(email, password):
    conn = sqlite3.connect("featherbank.db")
    cursor = conn.cursor()

    hashed_password = hashlib.sha256(password.encode()).hexdigest() #This line encrypts the password using hashlib SHA-256

    try:
        cursor.execute("INSERT INTO users (email, password) VALUES (?,?)", (email, hashed_password)) #The "?" in this line are known as placeholders and are there to prevent SQL injection (hacking technique!)
        conn.commit()
        print("User registered successfully")
    except sqlite3.IntegrityError: #Removes duplicate emails
        print("Error: Email already exists.")

    conn.close()

#Function which handles login attempts by checking if the user inputs an email and password stored in the featherbank database.
def login_user(email, password):
    conn = sqlite3.connect("featherbank.db") #This is Python code which connects the db 
    cursor = conn.cursor() #This is the Python code which enables SQL to be used below (cursor.execute line 44)

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, hashed_password)) #This is where the check occurs
    user = cursor.fetchone() #This SQL function gets the first matching user from the db.

    if user:
        print("Login successfull!")
        return True
    else:
        print("Invalid credentials.")
        return False

    conn.close()