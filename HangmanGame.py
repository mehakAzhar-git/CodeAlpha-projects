import tkinter as tk
from tkinter import messagebox
import random

# Words
words = ["python", "computer", "software", "program", "developer"]

word = random.choice(words)
guessed_letters = set()
wrong_guesses = 0
max_wrong = 6


def update_display():
    display = ""

    for letter in word:
    for letter in word:
        if letter in guessed_letters:
            display += letter.upper() + " "
        else:
            display += "_ "

    word_label.config(text=display)
    wrong_label.config(
        text=f"Wrong guesses: {wrong_guesses}/{max_wrong}"
    )
    guessed_label.config(
        text="Guessed letters: " + ", ".join(sorted(guessed_letters))
    )


def guess_letter():
    global wrong_guesses

    letter = entry.get().lower().strip()
    entry.delete(0, tk.END)

    if len(letter) != 1 or not letter.isalpha():
        messagebox.showwarning(
            "Invalid Input",
            "Please enter one letter."
        )
        return

    if letter in guessed_letters:
        messagebox.showinfo(
            "Already Guessed",
            "You already guessed this letter."
        )
        return

    guessed_letters.add(letter)

    if letter not in word:
        wrong_guesses += 1

    update_display()

    if all(letter in guessed_letters for letter in word):
        messagebox.showinfo(
            "You Won!",
            f"Congratulations! The word was: {word.upper()}"
        )
        new_game()

    elif wrong_guesses >= max_wrong:
        messagebox.showinfo(
            "Game Over",
            f"The word was: {word.upper()}"
        )
        new_game()


def new_game():
    global word, guessed_letters, wrong_guesses

    word = random.choice(words)
    guessed_letters = set()
    wrong_guesses = 0

    update_display()


# Main Window
root = tk.Tk()
root.title("Hangman Game")
root.geometry("600x500")
root.resizable(False, False)

title_label = tk.Label(
    root,
    text="🎮 HANGMAN GAME",
    font=("Arial", 28, "bold")
)
title_label.pack(pady=25)

instruction_label = tk.Label(
    root,
    text="Guess the hidden word!",
    font=("Arial", 16)
)
instruction_label.pack()

word_label = tk.Label(
    root,
    text="",
    font=("Arial", 30, "bold")
)
word_label.pack(pady=30)

wrong_label = tk.Label(
    root,
    text="Wrong guesses: 0/6",
    font=("Arial", 14)
)
wrong_label.pack()

guessed_label = tk.Label(
    root,
    text="Guessed letters:",
    font=("Arial", 14)
)
guessed_label.pack(pady=10)

entry = tk.Entry(
    root,
    font=("Arial", 20),
    width=5,
    justify="center"
)
entry.pack(pady=10)

guess_button = tk.Button(
    root,
    text="GUESS",
    font=("Arial", 14, "bold"),
    command=guess_letter,
    width=12
)
guess_button.pack(pady=10)

new_game_button = tk.Button(
    root,
    text="NEW GAME",
    font=("Arial", 12),
    command=new_game,
    width=12
)
new_game_button.pack(pady=10)

update_display()

root.mainloop()
