import random
import string
import tkinter as tk
from tkinter import messagebox, ttk

# Function to generate a random password
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4 characters.")
            return

        # Character sets
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase if uppercase_var.get() else ""
        digits = string.digits if numbers_var.get() else ""
        special = string.punctuation if special_var.get() else ""

        all_chars = lower + upper + digits + special
        if not all_chars:
            messagebox.showerror("Error", "Please select at least one character type.")
            return

        # Generate a strong password
        password = (
            (random.choice(lower) if lower else "") +
            (random.choice(upper) if upper else "") +
            (random.choice(digits) if digits else "") +
            (random.choice(special) if special else "")
        )

        password += ''.join(random.choices(all_chars, k=length - len(password)))
        password = ''.join(random.sample(password, len(password)))

        password_var.set(password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# Copy password to clipboard
def copy_to_clipboard():
    generated_password = password_var.get()
    if generated_password:
        root.clipboard_clear()
        root.clipboard_append(generated_password)
        root.update()
        messagebox.showinfo("Success", "Password copied to clipboard!")

# Toggle password visibility
def toggle_password():
    password_entry.config(show="" if show_password_var.get() else "*")

# Save password to file
def save_password():
    generated_password = password_var.get()
    if generated_password:
        with open("saved_passwords.txt", "a") as file:
            file.write(f"{generated_password}\n")
        messagebox.showinfo("Success", "Password saved to file!")

# Exit application
def exit_app():
    root.destroy()

# Toggle Theme
def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    theme = dark_theme if dark_mode else light_theme

    root.configure(bg=theme["bg"])
    title_label.config(bg=theme["bg"], fg=theme["fg"])
    length_label.config(bg=theme["bg"], fg=theme["fg"])
    length_entry.config(bg=theme["entry_bg"], fg=theme["entry_fg"])
    uppercase_check.config(bg=theme["bg"], fg=theme["fg"])
    numbers_check.config(bg=theme["bg"], fg=theme["fg"])
    special_check.config(bg=theme["bg"], fg=theme["fg"])
    generate_btn.config(bg=theme["button_bg"], fg=theme["button_fg"])
    password_entry.config(bg=theme["entry_bg"], fg=theme["entry_fg"])
    show_password_check.config(bg=theme["bg"], fg=theme["fg"])
    copy_btn.config(bg=theme["button_bg"], fg=theme["button_fg"])
    save_btn.config(bg=theme["button_bg"], fg=theme["button_fg"])
    exit_btn.config(bg="red", fg="white")
    toggle_theme_btn.config(bg=theme["button_bg"], fg=theme["button_fg"])

# Themes
dark_theme = {
    "bg": "#121212", "fg": "white", "entry_bg": "#333", "entry_fg": "blue",
    "button_bg": "#0078D7", "button_fg": "white"
}

light_theme = {
    "bg": "#f0f0f0", "fg": "black", "entry_bg": "#fff", "entry_fg": "black",
    "button_bg": "#0078D7", "button_fg": "white"
}

# Initial Theme
dark_mode = True

# Create main window
root = tk.Tk()
root.title("Password Generator")
root.attributes('-fullscreen', True)
root.configure(bg=dark_theme["bg"])

# Title Label
title_label = tk.Label(root, text="🔒 Secure Password Generator 🔑", font=("Arial", 28, "bold"))
title_label.pack(pady=20)

# Password Length Input
length_label = tk.Label(root, text="Enter Password Length:", font=("Arial", 16))
length_label.pack(pady=5)
length_entry = tk.Entry(root, font=("Arial", 16), width=10)
length_entry.pack(pady=5)

# Character Type Selection
uppercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

checkbox_frame = tk.Frame(root)
checkbox_frame.pack(pady=10)

uppercase_check = tk.Checkbutton(checkbox_frame, text="🔠 Uppercase", variable=uppercase_var, font=("Arial", 14))
uppercase_check.pack(side="left", padx=10)

numbers_check = tk.Checkbutton(checkbox_frame, text="🔢 Numbers", variable=numbers_var, font=("Arial", 14))
numbers_check.pack(side="left", padx=10)

special_check = tk.Checkbutton(checkbox_frame, text="🔣 Special Characters", variable=special_var, font=("Arial", 14))
special_check.pack(side="left", padx=10)

# Generate Password Button
generate_btn = tk.Button(root, text="🎲 Generate Password", font=("Arial", 16, "bold"), command=generate_password)
generate_btn.pack(pady=10)

# Display Password
password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, font=("Arial", 18, "bold"), width=30, state="readonly", show="*")
password_entry.pack(pady=10)

# Show/Hide Password Checkbox
show_password_var = tk.BooleanVar()
show_password_check = tk.Checkbutton(root, text="👁 Show Password", variable=show_password_var, command=toggle_password, font=("Arial", 14))
show_password_check.pack(pady=5)

# Action Buttons (Copy & Save)
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

copy_btn = tk.Button(button_frame, text="📋 Copy", font=("Arial", 16, "bold"), command=copy_to_clipboard)
copy_btn.pack(side="left", padx=10)

save_btn = tk.Button(button_frame, text="💾 Save", font=("Arial", 16, "bold"), command=save_password)
save_btn.pack(side="left", padx=10)

# Toggle Theme Button
toggle_theme_btn = tk.Button(root, text="🌗 Toggle Theme", font=("Arial", 16, "bold"), command=toggle_theme)
toggle_theme_btn.pack(pady=10)

# Exit Button
exit_btn = tk.Button(root, text="❌ Exit", font=("Arial", 16, "bold"), command=exit_app)
exit_btn.pack(pady=20)

# Apply initial theme
toggle_theme()

# Run application
root.mainloop()
