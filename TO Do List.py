import tkinter as tk
from tkinter import messagebox
import json

# File to store tasks
tasks_file = "tasks.json"

# Function to load tasks from file
def load_tasks():
    try:
        with open(tasks_file, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Function to save tasks to file
def save_tasks():
    with open(tasks_file, "w") as file:
        json.dump(tasks, file, indent=4)

# Function to update the task list UI
def update_listbox():
    task_listbox.delete(0, tk.END)
    for idx, task in enumerate(tasks):
        status = "✔" if task["completed"] else "✖"
        task_listbox.insert(tk.END, f"{idx+1}. {task['task']} [{status}]")
    update_task_count()

# Function to update task count
def update_task_count():
    total_count = len(tasks)
    completed_count = sum(1 for task in tasks if task["completed"])
    count_label.config(text=f"Tasks: {total_count} | Completed: {completed_count}")

# Function to add a new task
def add_task():
    task = task_entry.get()
    if task:
        tasks.append({"task": task, "completed": False})
        save_tasks()
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Function to mark a task as completed
def complete_task():
    try:
        selected = task_listbox.curselection()[0]
        tasks[selected]["completed"] = True
        save_tasks()
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to complete!")

# Function to delete a task
def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        del tasks[selected]
        save_tasks()
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to delete!")

# Function to toggle Dark Mode and Light Mode
def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode

    if dark_mode:
        root.configure(bg="#1E1E1E")
        task_listbox.configure(bg="#2E2E2E", fg="white")
        frame.configure(bg="#333333")
        btn_frame.configure(bg="#333333")
        toggle_button.config(text="Light Mode", bg="#F39C12", fg="black")
        count_label.config(bg="#1E1E1E", fg="white")
    else:
        root.configure(bg="#ECF0F1")
        task_listbox.configure(bg="white", fg="black")
        frame.configure(bg="#BDC3C7")
        btn_frame.configure(bg="#BDC3C7")
        toggle_button.config(text="Dark Mode", bg="#2C3E50", fg="white")
        count_label.config(bg="#ECF0F1", fg="black")

# Load tasks on startup
tasks = load_tasks()
dark_mode = False  # Default to Light Mode

# GUI Setup
root = tk.Tk()
root.title("To-Do List")
root.geometry("500x600")
root.configure(bg="#ECF0F1")

# Open in full-screen mode
root.state('zoomed')  # Windows full-screen mode
# root.attributes('-fullscreen', True)  # Alternative full-screen mode

# Task Count Label
count_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#ECF0F1", fg="black")
count_label.pack(pady=5)

# Frame for entry and add button
frame = tk.Frame(root, bg="#BDC3C7")
frame.pack(pady=10)

# Entry box for new tasks
task_entry = tk.Entry(frame, width=40, font=("Arial", 14), bg="white", fg="black")
task_entry.pack(side=tk.LEFT, padx=10)

# Add Button
add_button = tk.Button(frame, text="Add", command=add_task, bg="#1ABC9C", fg="white", font=("Arial", 12), padx=10, pady=5)
add_button.pack(side=tk.LEFT)

# Task Listbox
task_listbox = tk.Listbox(root, width=50, height=15, font=("Arial", 14), bg="white", fg="black")
task_listbox.pack(pady=10)
update_listbox()

# Frame for action buttons
btn_frame = tk.Frame(root, bg="#BDC3C7")
btn_frame.pack()

# Complete Task Button
complete_button = tk.Button(btn_frame, text="Complete", command=complete_task, bg="#3498DB", fg="white", font=("Arial", 12), padx=10, pady=5)
complete_button.pack(side=tk.LEFT, padx=5)

# Delete Task Button
delete_button = tk.Button(btn_frame, text="Delete", command=delete_task, bg="#E74C3C", fg="white", font=("Arial", 12), padx=10, pady=5)
delete_button.pack(side=tk.LEFT, padx=5)

# Toggle Dark/Light Mode Button
toggle_button = tk.Button(root, text="Dark Mode", command=toggle_theme, bg="#2C3E50", fg="white", font=("Arial", 12), padx=10, pady=5)
toggle_button.pack(pady=10)

# Exit Button
exit_button = tk.Button(root, text="Exit", command=root.quit, bg="#C0392B", fg="white", font=("Arial", 12), padx=10, pady=5)
exit_button.pack(pady=10)

# Run the application
root.mainloop()
