import tkinter as tk
from time import strftime

def update():
    time_string = strftime('%H:%M:%S')
    label.config(text=time_string)
    label.after(1000, update)

root = tk.Tk()
root.title("Digital Clock")

label = tk.Label(root, font=('calibri', 50, 'bold'), background='black', foreground='white')
label.pack(anchor='center')

update()
root.mainloop()