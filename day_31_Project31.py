# Day 31
# Project-31 = Capstone Project - Flash card Program
import tkinter as tk
import random

# Sample flashcards (you can add more)
flashcards = [
    {"question": "Bonjour", "answer": "Hello"},
    {"question": "Merci", "answer": "Thank you"},
    {"question": "Chat", "answer": "Cat"},
    {"question": "Chien", "answer": "Dog"},
    {"question": "Pomme", "answer": "Apple"},
]

current_card = {}

# -------------- Functions ---------------- #
def next_card():
    global current_card
    current_card = random.choice(flashcards)
    card_label.config(text=current_card["question"])
    answer_label.config(text="")
    window.after(3000, show_answer)

def show_answer():
    answer_label.config(text=current_card["answer"])

# -------------- UI Setup ----------------- #
window = tk.Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg="#f9f9f9")

card_label = tk.Label(window, text="", font=("Arial", 40, "bold"), bg="#f9f9f9")
card_label.pack(pady=20)

answer_label = tk.Label(window, text="", font=("Arial", 30), fg="green", bg="#f9f9f9")
answer_label.pack(pady=20)

next_button = tk.Button(window, text="Next", command=next_card, font=("Arial", 20))
next_button.pack(pady=20)

next_card()  # Show first card
window.mainloop()
