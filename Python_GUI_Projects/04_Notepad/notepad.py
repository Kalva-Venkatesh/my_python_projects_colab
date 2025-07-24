import tkinter as tk
from tkinter import filedialog

def open_file():
    path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if path:
        with open(path, "r") as f:
            text.delete(1.0, tk.END)
            text.insert(tk.END, f.read())

def save_file():
    path = filedialog.asksaveasfilename(defaultextension=".txt")
    if path:
        with open(path, "w") as f:
            f.write(text.get(1.0, tk.END))

root = tk.Tk()
root.title("Notepad")

text = tk.Text(root, wrap='word')
text.pack(expand=1, fill='both')

menu = tk.Menu(root)
file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
menu.add_cascade(label="File", menu=file_menu)

root.config(menu=menu)
root.mainloop()