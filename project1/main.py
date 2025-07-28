import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import os
import time

# Constants
RESOURCE_DIR = r"D:\GitHub\python\project1\resources"
CHOICES = ["rock", "paper", "scissor"]
ANIMATION_DELAY = 100  # ms

# Game Stats
stats = {"Win": 0, "Lose": 0, "Tie": 0}

# Game logic
def determine_winner(player, computer):
    if player == computer:
        stats["Tie"] += 1
        return "It's a tie!"
    elif (player == "rock" and computer == "scissor") or \
         (player == "scissor" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        stats["Win"] += 1
        return "You win!"
    else:
        stats["Lose"] += 1
        return "Computer wins!"

# Animate computer thinking
def animate_computer_choice(i=0, cycles=6):
    choice = CHOICES[i % len(CHOICES)]
    comp_img = image_dict[choice]
    computer_label.config(image=comp_img)
    computer_label.image = comp_img

    if i < cycles:
        root.after(ANIMATION_DELAY, lambda: animate_computer_choice(i+1, cycles))
    else:
        final_computer_choice = random.choice(CHOICES)
        final_img = image_dict[final_computer_choice]
        computer_label.config(image=final_img)
        computer_label.image = final_img

        result = determine_winner(current_player_choice[0], final_computer_choice)
        result_label.config(text=f"Computer chose: {final_computer_choice}\n{result}")
        update_leaderboard()

def play(player_choice):
    current_player_choice[0] = player_choice
    result_label.config(text="Computer is thinking...")
    animate_computer_choice()

# Update stats
def update_leaderboard():
    leaderboard_label.config(
        text=f"Wins: {stats['Win']} | Losses: {stats['Lose']} | Ties: {stats['Tie']}"
    )

# Reset game
def reset_game():
    stats.update({"Win": 0, "Lose": 0, "Tie": 0})
    update_leaderboard()
    result_label.config(text="")
    computer_label.config(image="")
    computer_label.image = None

# GUI Setup
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("420x580")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# Load images
image_dict = {}
for choice in CHOICES:
    path = os.path.join(RESOURCE_DIR, f"{choice}.png")
    img = Image.open(path).resize((100, 100))
    image_dict[choice] = ImageTk.PhotoImage(img)

current_player_choice = [""]  # mutable reference

# Header
tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=15)

# Player choice
tk.Label(root, text="Choose your move:", font=("Arial", 12), bg="#f0f0f0").pack()

btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=10)

for choice in CHOICES:
    btn = tk.Button(btn_frame, image=image_dict[choice], command=lambda c=choice: play(c), bd=2, relief="groove", cursor="hand2")
    btn.pack(side=tk.LEFT, padx=10)

# Computer choice
tk.Label(root, text="Computer's choice:", font=("Arial", 12), bg="#f0f0f0").pack(pady=10)
computer_label = tk.Label(root, bg="#f0f0f0")
computer_label.pack()

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0", fg="#333")
result_label.pack(pady=20)

# Leaderboard
leaderboard_label = tk.Label(root, text="Wins: 0 | Losses: 0 | Ties: 0", font=("Arial", 12, "bold"), fg="#005f73", bg="#f0f0f0")
leaderboard_label.pack(pady=10)

# Reset button
reset_btn = tk.Button(root, text="Reset Game", command=reset_game, font=("Arial", 11), bg="#e63946", fg="white", relief="raised", cursor="hand2")
reset_btn.pack(pady=10)

root.mainloop()