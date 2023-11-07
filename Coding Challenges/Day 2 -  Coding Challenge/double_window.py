import tkinter as tk

root = tk.Tk()
root.title("Custom Labels")

label1 = tk.Label(root, text="Label 1", bg="black", fg="white")
label1.pack()

label2 = tk.Label(root, text="Label 2", bg="red", fg="yellow")
label2.pack()

root.mainloop()
