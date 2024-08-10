import tkinter as tk
from tkinter import messagebox
from nltk.corpus import words
import nltk

# Download the words corpus if you haven't already
nltk.download('words')

# Load the list of words
word_list = set(words.words())

def edit_distance(word1, word2):
    if len(word1) < len(word2):
        return edit_distance(word2, word1)

    if len(word2) == 0:
        return len(word1)

    previous_row = range(len(word2) + 1)
    for i, c1 in enumerate(word1):
        current_row = [i + 1]
        for j, c2 in enumerate(word2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]

def autocorrect(input_word):
    if input_word in word_list:
        return input_word
    
    # Find the closest word
    closest_word = min(word_list, key=lambda word: edit_distance(input_word, word))
    
    return closest_word

class AutoCorrectApp:
    def __init__(self, master):
        self.master = master
        master.title("Autocorrect Application")

        self.label = tk.Label(master, text="Enter a word:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.submit_button = tk.Button(master, text="Submit", command=self.check_word)
        self.submit_button.pack()

    def check_word(self):
        input_word = self.entry.get()
        corrected_word = autocorrect(input_word)
        messagebox.showinfo("Correction Result", f"Did you mean: {corrected_word}?")

# Create the GUI
root = tk.Tk()
my_app = AutoCorrectApp(root)
root.mainloop()