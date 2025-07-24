import os
import shutil
from tkinter import filedialog, Tk, Button, Label

def organize():
    folder_path = filedialog.askdirectory()
    if not folder_path:
        return

    for file in os.listdir(folder_path):
        filename, ext = os.path.splitext(file)
        ext = ext[1:].upper()
        if ext:
            new_dir = os.path.join(folder_path, ext)
            os.makedirs(new_dir, exist_ok=True)
            shutil.move(os.path.join(folder_path, file), os.path.join(new_dir, file))

root = Tk()
root.title("File Organizer")
root.geometry("300x150")

Label(root, text="Click to organize files").pack(pady=10)
Button(root, text="Choose Folder", command=organize).pack()

root.mainloop()