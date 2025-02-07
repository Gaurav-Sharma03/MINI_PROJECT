import tkinter as tk
import random

# Set up the main application window
root = tk.Tk()
root.title("Detail filling form")


# Create GUI elements
welcome_label = tk.Label(root, text="welcome please fill your details")
welcome_label.pack()

guess_label = tk.Label(root, text="Please enter your name")
guess_label.pack()

guess_entry = tk.Entry(root)
guess_entry.pack()

guess_button = tk.Button(root, text="Submit Answer", command="")
guess_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Start the Tkinter event loop
root.mainloop()
