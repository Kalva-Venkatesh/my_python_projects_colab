import tkinter as tk
import random

def roll():
    num.set(str(random.randint(1, 6)))

root = tk.Tk()
root.title("Dice Roller")
root.geometry("200x200")

num = tk.StringVar()
tk.Label(root, textvariable=num, font=("Arial", 100)).pack()
tk.Button(root, text="Roll Dice", command=roll).pack(pady=10)

root.mainloop()