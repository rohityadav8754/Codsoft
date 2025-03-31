import tkinter as tk
import random
from tkinter import ttk, messagebox
import winsound  # For sound effects (Windows only)

# Function to toggle between dark and light mode
def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    
    bg_color = "#222244" if dark_mode else "white"
    fg_color = "#ffcc00" if dark_mode else "black"
    button_bg = "#444466" if dark_mode else "#cccccc"
    
    root.configure(bg=bg_color)
    title_label.config(bg=bg_color, fg=fg_color)
    user_label.config(bg=bg_color, fg="white" if dark_mode else "black")
    computer_label.config(bg=bg_color, fg="white" if dark_mode else "black")
    result_label.config(bg=bg_color, fg="white" if dark_mode else "black")
    user_score_label.config(bg=bg_color, fg="#66ff66" if dark_mode else "black")
    computer_score_label.config(bg=bg_color, fg="#ff6666" if dark_mode else "black")
    theme_button.config(text="🌙 Dark Mode" if dark_mode else "💡 Light Mode", bg=button_bg, fg="white" if dark_mode else "black")

# Function to play game
def play_game(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    user_label.config(text=f"You chose: {user_choice}", fg="#ffcc00")
    computer_label.config(text=f"Computer chose: {computer_choice}", fg="#ff6666")

    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=result, fg="#66ff66")

    update_score(result)

# Function to determine the winner
def determine_winner(user, computer):
    if user == computer:
        return "It's a Tie!"
    if (user == "Rock" and computer == "Scissors") or \
       (user == "Scissors" and computer == "Paper") or \
       (user == "Paper" and computer == "Rock"):
        return "You Win! 🎉"
    else:
        return "You Lose! 😞"

# Function to update score and check for winner
def update_score(result):
    global user_score, computer_score
    if "Win" in result:
        user_score += 1
    elif "Lose" in result:
        computer_score += 1

    user_score_label.config(text=f"User Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

    user_progress["value"] = user_score
    computer_progress["value"] = computer_score

    if user_score == 10:
        announce_winner("🎉 Congratulations! You Win! 🎉")
    elif computer_score == 10:
        announce_winner("💀 Game Over! Computer Wins! 💀")

# Function to announce the winner and reset the game
def announce_winner(message):
    winsound.Beep(1000, 500)  # Play a sound effect
    messagebox.showinfo("Game Over", message)
    reset_game()
    

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_score_label.config(text="User Score: 0")
    computer_score_label.config(text="Computer Score: 0")
    user_progress["value"] = 0
    computer_progress["value"] = 0
    user_label.config(text="You chose: ", fg="white")
    computer_label.config(text="Computer chose: ", fg="white")
    result_label.config(text="", fg="white")

# Function to make the window full-screen
def make_fullscreen(event=None):
    root.attributes("-fullscreen", True)

# Function to exit full-screen mode
def exit_fullscreen(event=None):
    root.attributes("-fullscreen", False)

# Initialize main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.attributes("-fullscreen", True)  # Full-screen mode
root.configure(bg="#222244")  # Default Dark Mode

# Game Title
title_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Arial", 40, "bold"), bg="#222244", fg="#ffcc00")
title_label.pack(pady=30)

# Theme Toggle Button
dark_mode = True
theme_button = tk.Button(root, text="🌙 Dark Mode", font=("Arial", 14, "bold"), bg="#444466", fg="white", 
                         padx=10, pady=5, command=toggle_theme)
theme_button.place(x=20, y=20)

# User & Computer Choice Labels
user_label = tk.Label(root, text="You chose: ", font=("Arial", 20), bg="#222244", fg="white")
user_label.pack()
computer_label = tk.Label(root, text="Computer chose: ", font=("Arial", 20), bg="#222244", fg="white")
computer_label.pack()

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 25, "bold"), bg="#222244", fg="white")
result_label.pack(pady=20)

# Score Labels
user_score = 0
computer_score = 0
user_score_label = tk.Label(root, text="User Score: 0", font=("Arial", 20), bg="#222244", fg="#66ff66")
user_score_label.pack()
computer_score_label = tk.Label(root, text="Computer Score: 0", font=("Arial", 20), bg="#222244", fg="#ff6666")
computer_score_label.pack()

# Score Meter Frame
score_frame = tk.Frame(root, bg="#222244")
score_frame.pack(pady=20)

# User Score Meter
user_progress = ttk.Progressbar(score_frame, orient="horizontal", length=200, mode="determinate", maximum=10)
user_progress.grid(row=0, column=0, padx=20)
tk.Label(score_frame, text="User", font=("Arial", 18, "bold"), bg="#222244", fg="white").grid(row=1, column=0)

# Computer Score Meter
computer_progress = ttk.Progressbar(score_frame, orient="horizontal", length=200, mode="determinate", maximum=10)
computer_progress.grid(row=0, column=1, padx=20)
tk.Label(score_frame, text="Computer", font=("Arial", 18, "bold"), bg="#222244", fg="white").grid(row=1, column=1)

# Buttons for game choices
button_frame = tk.Frame(root, bg="#222244")
button_frame.pack(pady=20)

rock_btn = tk.Button(button_frame, text="🪨 Rock", font=("Arial", 18, "bold"), bg="#ffcc00", fg="black",
                     padx=20, pady=10, command=lambda: play_game("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="📄 Paper", font=("Arial", 18, "bold"), bg="#66ff66", fg="black",
                      padx=20, pady=10, command=lambda: play_game("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="✂ Scissors", font=("Arial", 18, "bold"), bg="#ff6666", fg="black",
                         padx=20, pady=10, command=lambda: play_game("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

# Play Again Button
play_again_btn = tk.Button(root, text="🔄 Play Again", font=("Arial", 18, "bold"), bg="#ffcc00", fg="black",
                           padx=20, pady=10, command=reset_game)
play_again_btn.pack(pady=20)

# Exit Button
exit_btn = tk.Button(root, text="❌ Exit Game", font=("Arial", 18, "bold"), bg="red", fg="white",
                     padx=20, pady=10, command=root.quit)
exit_btn.pack(pady=10)

# Bind full-screen toggle keys
root.bind("<F11>", make_fullscreen)
root.bind("<Escape>", exit_fullscreen)

# Run the Tkinter event loop
root.mainloop()
