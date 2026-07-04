import tkinter as tk
import random

# Main Window
window = tk.Tk()
window.title("Dice Rolling Game")
window.geometry("400x350")
window.config(bg="#1e1e2f")

# Function to roll dice
def roll_dice():
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)

    dice1_label.config(text=str(d1))
    dice2_label.config(text=str(d2))
    total_label.config(text=f"Total = {d1 + d2}")

# Title
title = tk.Label(
    window,
    text="🎲 Dice Rolling Game 🎲",
    font=("Arial", 22, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title.pack(pady=20)

# Dice Frame
dice_frame = tk.Frame(window, bg="#1e1e2f")
dice_frame.pack(pady=20)

# Dice 1
dice1_label = tk.Label(
    dice_frame,
    text="1",
    font=("Arial", 40, "bold"),
    width=3,
    bg="white",
    fg="#ff5733",
    relief="solid",
    bd=3
)
dice1_label.grid(row=0, column=0, padx=20)

# Dice 2
dice2_label = tk.Label(
    dice_frame,
    text="1",
    font=("Arial", 40, "bold"),
    width=3,
    bg="white",
    fg="#33a1ff",
    relief="solid",
    bd=3
)
dice2_label.grid(row=0, column=1, padx=20)

# Total Label
total_label = tk.Label(
    window,
    text="Total = 2",
    font=("Arial", 18, "bold"),
    bg="#1e1e2f",
    fg="#00ff99"
)
total_label.pack(pady=15)

# Roll Button
roll_button = tk.Button(
    window,
    text="Roll Dice",
    font=("Arial", 16, "bold"),
    bg="#ffcc00",
    fg="black",
    padx=20,
    pady=10,
    command=roll_dice,
    cursor="hand2"
)
roll_button.pack(pady=20)

# Run Window
window.mainloop()