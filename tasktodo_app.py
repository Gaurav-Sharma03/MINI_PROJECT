import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        # Initialize the tasks list
        self.tasks = []

        # Frame for the list and scroll bar
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(frame, height=10, width=50, selectmode=tk.SINGLE)
        self.task_listbox.grid(row=0, column=0)

        # Scrollbar for the listbox
        scrollbar = tk.Scrollbar(frame)
        scrollbar.grid(row=0, column=1, sticky="ns")

        # Attach the scrollbar to the listbox
        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)

        # Entry field to add/update tasks
        self.task_entry = tk.Entry(self.root, width=52)
        self.task_entry.pack(pady=10)

        # Buttons for adding, removing, and updating tasks
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=5)

        self.add_button = tk.Button(button_frame, text="Add Task", width=20, command=self.add_task)
        self.add_button.grid(row=0, column=0, padx=5)

        self.remove_button = tk.Button(button_frame, text="Remove Task", width=20, command=self.remove_task)
        self.remove_button.grid(row=0, column=1, padx=5)

        self.update_button = tk.Button(button_frame, text="Update Task", width=20, command=self.update_task)
        self.update_button.grid(row=0, column=2, padx=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def remove_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_task_index)
            self.tasks.remove(task)
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to remove.")

    def update_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_task_index)
            new_task = self.task_entry.get()
            if new_task:
                self.tasks[selected_task_index] = new_task
                self.update_task_listbox()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Input Error", "Please enter a new task.")
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to update.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)


# Create the main window
root = tk.Tk()
app = TodoListApp(root)

# Run the application
root.mainloop()
