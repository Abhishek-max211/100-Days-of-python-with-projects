# Day 29
# Project-29 = Building a Password Manager Project 
from tkinter import *
from tkinter import messagebox

def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website == "" or password == "":
        messagebox.showwarning(title="Oops", message="Website and Password can't be empty!")
    else:
        with open("passwords.txt", "a") as file:
            file.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)

# GUI
window = Tk()
window.title("Simple Password Manager")
window.config(padx=20, pady=20)

Label(text="Website:").grid(row=0, column=0)
Label(text="Email:").grid(row=1, column=0)
Label(text="Password:").grid(row=2, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=0, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=1, column=1, columnspan=2)
email_entry.insert(0, "you@example.com")

password_entry = Entry(width=35)
password_entry.grid(row=2, column=1, columnspan=2)

Button(text="Add", width=36, command=save_password).grid(row=3, column=1, columnspan=2)

window.mainloop()
