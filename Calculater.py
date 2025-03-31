import tkinter as tk
from tkinter import messagebox

# Function to handle button clicks
def on_button_click(value):
    current_text = entry_var.get()
    if value == "Enter":
        try:
            result = str(eval(current_text))
            entry_var.set(result)
        except:
            messagebox.showerror("Error", "Invalid Calculation!")
            entry_var.set("")
    elif value == "C":
        entry_var.set("")
    elif value == "Exit":
        root.quit()
    else:
        entry_var.set(current_text + str(value))

# Function to toggle themes
def toggle_theme():
    if root["bg"] == "#2C3E50":  # Dark Mode
        root.config(bg="white")
        entry_display.config(bg="lightgray", fg="black")
        theme_button.config(bg="#16A085", fg="white")
        for btn in buttons:
            btn.config(bg="white", fg="black")
    else:  # Light Mode
        root.config(bg="#2C3E50")
        entry_display.config(bg="#34495E", fg="white")
        theme_button.config(bg="white", fg="black")
        for btn in buttons:
            btn.config(bg="#3498DB", fg="white")

# Function to handle keyboard input
def on_key(event):
    key = event.char
    if key in "0123456789+-*/.":
        on_button_click(key)
    elif key == "\r":  # Enter key
        on_button_click("Enter")
    elif key == "\x08":  # Backspace
        entry_var.set(entry_var.get()[:-1])

# Create main window
root = tk.Tk()
root.title("Stylish Full-Screen Calculator")
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
root.configure(bg="#2C3E50")

# Display Entry
entry_var = tk.StringVar()
entry_display = tk.Entry(root, textvariable=entry_var, font=("Arial", 30), bd=5, relief="ridge", width=15, justify="right")
entry_display.pack(pady=20, ipady=10)

# Button Frame
button_frame = tk.Frame(root, bg="#2C3E50")
button_frame.pack()

# Buttons Layout
button_values = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", "Enter", "+"),
    ("Exit",)
]

buttons = []
for row in button_values:
    button_row = tk.Frame(button_frame, bg="#2C3E50")
    button_row.pack(side="top")
    for value in row:
        btn = tk.Button(button_row, text=value, font=("Arial", 24, "bold"), width=6, height=2, 
                        bg="#3498DB", fg="white", command=lambda v=value: on_button_click(v))
        btn.pack(side="left", padx=5, pady=5)
        buttons.append(btn)

# Theme Toggle Button
theme_button = tk.Button(root, text="Toggle Theme", font=("Arial", 18, "bold"), bg="#16A085", fg="white", padx=20, pady=10, command=toggle_theme)
theme_button.pack(pady=20)

# Bind keyboard inputs
root.bind("<Key>", on_key)

#
root.mainloop()