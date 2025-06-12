# Day 28
# Project-28 = Building a Promodoro App
from tkinter import *
import time

# Create window
window = Tk()
window.title("Digital Clock (12-Hour Format)")
window.geometry("400x200")
window.config(bg="black")

# Time label
clock_label = Label(window, font=('Courier', 40, 'bold'), background='black', foreground='cyan')
clock_label.pack(anchor='center', expand=True)

# Update time
def update_time():
    current_time = time.strftime('%I:%M:%S %p')  # 12-hour format with AM/PM
    clock_label.config(text=current_time)
    window.after(1000, update_time)

update_time()
window.mainloop()
