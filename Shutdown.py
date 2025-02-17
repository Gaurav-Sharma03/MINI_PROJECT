import os
import tkinter as tk
from tkinter import messagebox

def shutdown():
    if messagebox.askyesno("Shutdown", "Are you sure you want to shut down the PC?"):
        os.system("shutdown /s /t 1")

def restart():
    if messagebox.askyesno("Restart", "Are you sure you want to restart the PC?"):
        os.system("shutdown /r /t 1")

def cancel():
    root.destroy()

root = tk.Tk()
root.title("PC Control")
root.geometry("300x150")

shutdown_btn = tk.Button(root, text="Shutdown", command=shutdown, width=10, height=2)
shutdown_btn.pack(pady=10)

restart_btn = tk.Button(root, text="Restart", command=restart, width=10, height=2)
restart_btn.pack(pady=10)

cancel_btn = tk.Button(root, text="Cancel", command=cancel, width=10, height=2)
cancel_btn.pack(pady=10)

root.mainloop()

