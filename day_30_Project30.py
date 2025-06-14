# Day 30
# Project-30 = The Password Manager with json Project
import json
from tkinter import *
from tkinter import messagebox
import random
import string

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = string.ascii_letters
    digits = string.digits
    symbols = "!#$%&()*+"

    password_list = (
        [random.choice(letters) for _ in range(8)] +
        [random.choice(digits) for _ in range(3)] +
        [random.choice(symbols) for _ in range(2)]
    )
    random.shuffle(password_list)
    password = ''.join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()

    if not website or not password:
        messagebox.showwarning(title="Oops", message="Please fill out all fields.")
        return

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    try:
        with open("data.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        data = {}

    data.update(new_data)

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

    website_entry.delete(0, END)
    password_entry.delete(0, END)
    messagebox.showinfo(title="Success", message="Password saved successfully!")

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get().strip()

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
        return

    if website in data:
        email = data[website]['email']
        password = data[website]['password']
        messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
    else:
        messagebox.showwarning(title="Not Found", message="No details for the website exists.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Labels
Label(text="Website:").grid(row=1, column=0)
Label(text="Email/Username:").grid(row=2, column=0)
Label(text="Password:").grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1)
email_entry.insert(0, "you@example.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
Button(text="Generate Password", command=generate_password).grid(row=3, column=2)
Button(text="Add", width=36, command=save_password).grid(row=4, column=1, columnspan=2)
Button(text="Search", width=14, command=find_password).grid(row=1, column=2)

window.mainloop()
