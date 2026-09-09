import tkinter as tk
from time import strftime

# Create window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("500x200")

# Clock label
label = tk.Label(
    root,
    font=("Arial", 60),
    background="black",
    foreground="white"
)
label.pack(anchor="center", pady=40)


# Function to update time
def update_time():
    current_time = strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000, update_time)


# Start clock
update_time()

# Run application
root.mainloop()