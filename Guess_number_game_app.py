import tkinter as tk
import random

# Set up the main application window
root = tk.Tk()
root.title("Number Guessing Game")

number_to_guess = random.randrange(0, 100)
chances = 7
guess_count = 0

def check_guess():
    global guess_count
    guess_count += 1
    my_guess = int(guess_entry.get())
    
    if my_guess == number_to_guess:
        result_label.config(text=f"Congratulations! The number is {number_to_guess}. You found it in {guess_count} attempts.")
        guess_entry.config(state='disabled')
        guess_button.config(state='disabled')
        
    elif guess_count >= chances:
        result_label.config(text=f"Oops, sorry! The number was {number_to_guess}. Better luck next time.")
        guess_entry.config(state='disabled')
        guess_button.config(state='disabled')
        
    elif my_guess > number_to_guess:
        result_label.config(text="Your guess is higher.")
        
    else:
        result_label.config(text="Your guess is lower.")

# Create GUI elements
welcome_label = tk.Label(root, text="Welcome to the number guessing game! You have 7 chances.")
welcome_label.pack()

guess_label = tk.Label(root, text="Please enter your guess number:")
guess_label.pack()

guess_entry = tk.Entry(root)
guess_entry.pack()

guess_button = tk.Button(root, text="Submit Guess", command=check_guess)
guess_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Start the Tkinter event loop
root.mainloop()
