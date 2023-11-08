import tkinter as tk

def change_to_blue():
    button1.config(bg="blue")

def change_to_yellow():
    button2.config(bg="yellow")

root = tk.Tk()

root.title("Button Color Changer")

label1 = tk.Label(root, text="Button 1 Color")
label1.pack()

button1 = tk.Button(root, text="Change to Blue", command=change_to_blue)
button1.pack()

label2 = tk.Label(root, text="Button 2 Color")
label2.pack()

button2 = tk.Button(root, text="Change to Yellow", command=change_to_yellow)
button2.pack()

root.mainloop()
