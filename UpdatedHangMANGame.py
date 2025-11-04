import random
import tkinter as tk
from tkinter import messagebox

# Hangman stages
hangman_stages = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

# Categories of words
word_categories = {
    
    "fruits": ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon"],
    "animals": ["elephant", "giraffe", "zebra", "lion", "tiger", "bear", "monkey"],
    "countries": ["canada", "brazil", "france", "germany", "india", "japan", "nigeria"],
    "colors": ["red", "blue", "green", "yellow", "orange", "purple", "violet"]
}

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        
        self.category = random.choice(list(word_categories.keys()))
        self.word = random.choice(word_categories[self.category])
        self.emptylist = ["_"] * len(self.word)
        self.guesses = 0
        self.max_guesses = 6
        
        # GUI Elements
        self.label_category = tk.Label(root, text=f"Category: {self.category}", font=("Helvetica", 16))
        self.label_category.pack(pady=10)

        self.label_word = tk.Label(root, text=" ".join(self.emptylist), font=("Helvetica", 24))
        self.label_word.pack(pady=10)

        self.label_hangman = tk.Label(root, text=hangman_stages[0], font=("Courier", 16))
        self.label_hangman.pack(pady=10)

        self.label_guesses = tk.Label(root, text=f"Guesses left: {self.max_guesses}", font=("Helvetica", 16))
        self.label_guesses.pack(pady=10)
        
        self.entry_guess = tk.Entry(root, font=("Helvetica", 16))
        self.entry_guess.pack(pady=10)
        
        self.button_submit = tk.Button(root, text="Submit Guess", command=self.check_guess, font=("Helvetica", 16))
        self.button_submit.pack(pady=10)

    def check_guess(self):
        guess = self.entry_guess.get().lower()
        self.entry_guess.delete(0, tk.END)

        if len(guess) != 1 or not guess.isalpha():
            messagebox.showerror("Invalid Input", "Please enter a single letter.")
            return

        if guess in self.word:
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.emptylist[i] = guess
            self.label_word.config(text=" ".join(self.emptylist))
        else:
            self.guesses += 1
            self.label_hangman.config(text=hangman_stages[self.guesses])

        self.label_guesses.config(text=f"Guesses left: {self.max_guesses - self.guesses}")

        if "_" not in self.emptylist:
            messagebox.showinfo("Hangman", f"You won! The word was {self.word}.")
            self.root.quit()

        if self.guesses >= self.max_guesses:
            messagebox.showinfo("Hangman", f"You lost! The word was {self.word}.")
            self.root.quit()
 
 
 
 
if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
