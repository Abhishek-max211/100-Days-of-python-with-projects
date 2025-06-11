# Day 27
# Project-27 = Mile to Kilometers Converter Project
from tkinter import *

# ---------- CONSTANTS ----------
MILES_TO_KM = 1.60934

# ---------- CONVERSION LOGIC ----------
def miles_to_km():
    """Get the number of miles from the input box, convert to km, and
    update the result label."""
    miles = float(miles_input.get() or 0)
    km = round(miles * MILES_TO_KM, 2)
    kilometer_result_label.config(text=f"{km}")

# ---------- UI SETUP ----------
window = Tk()
window.title("Miles to Kilometers Converter")
window.config(padx=20, pady=20)   # Nice padding all around

# Miles input box
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

# Static labels
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

# Result label (starts at 0)
kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

# Calculate button
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

# Keep the window open
window.mainloop()
