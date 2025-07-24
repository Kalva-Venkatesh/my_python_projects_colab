import tkinter as tk
import random
import string

def generate():
    length = int(entry.get())
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    result.config(text=password)

root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Enter length:").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Generate", command=generate).pack()
result = tk.Label(root, text="")
result.pack()

root.mainloop()