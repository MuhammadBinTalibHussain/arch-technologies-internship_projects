import tkinter as tk
import random

# Random number
secretNumber = random.randint(1, 100)
attempts = 0


def checkGuess():
    global attempts

    guess = entryBox.get()

    if guess == "":
        resultLabel.config(text="Enter a number first!")
        return

    try:
        guess = int(guess)
    except:
        resultLabel.config(text="Only numbers allowed!")
        return

    attempts += 1

    if guess < secretNumber:
        resultLabel.config(text="Too Low! Try Again")
    elif guess > secretNumber:
        resultLabel.config(text="Too High! Try Again")
    else:
        resultLabel.config(text=f"Correct! Attempts: {attempts}")


# Main Window
window = tk.Tk()
window.title("Number Guessing Game")
window.geometry("550x500")
window.configure(bg="#191933")

# Title
titleLabel = tk.Label(
    window,
    text="🎯 Number Guessing Game",
    font=("Arial", 24, "bold"),
    fg="white",
    bg="#191933"
)
titleLabel.pack(pady=30)

# Instruction
instruction = tk.Label(
    window,
    text="Guess a number between 1 and 100",
    font=("Arial", 14),
    fg="cyan",
    bg="#191933"
)
instruction.pack()

# Entry Box
entryBox = tk.Entry(
    window,
    font=("Arial", 18),
    width=20,
    justify="center"
)
entryBox.pack(pady=20)

# Button
guessButton = tk.Button(
    window,
    text="Check Guess",
    font=("Arial", 14, "bold"),
    bg="limegreen",
    fg="white",
    width=15,
    command=checkGuess
)
guessButton.pack(pady=20)

# Result Label
resultLabel = tk.Label(
    window,
    text="Start Guessing...",
    font=("Arial", 18, "bold"),
    fg="cyan",
    bg="#191933"
)
resultLabel.pack(pady=40)

window.mainloop()