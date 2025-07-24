import tkinter as tk

def paint(event):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    canvas.create_oval(x1, y1, x2, y2, fill="black")

def clear():
    canvas.delete("all")

root = tk.Tk()
root.title("Paint App")

canvas = tk.Canvas(root, bg="white", width=500, height=400)
canvas.pack()
canvas.bind("<B1-Motion>", paint)

tk.Button(root, text="Clear", command=clear).pack()

root.mainloop()