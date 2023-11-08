import tkinter as tk

def button_click():
    label1.config(text="Button Clicked!")
    label2.config(text="doing a specific thing !")
def button_click2():
    label1.config(text="Button Clicked!")
    label2.config(text="yay you won!")
root = tk.Tk()
root.title("Simple GUI Application")

frame1 = tk.Frame(root, bd=5, relief=tk.GROOVE, bg="lightblue")
frame1.pack(side=tk.TOP, padx=10, pady=10, fill=tk.X)

button1 = tk.Button(frame1, text="Button 1", command=button_click)
button1.pack(side=tk.LEFT, padx=10)

button2 = tk.Button(frame1, text="Button 2", command=button_click)
button2.pack(side=tk.LEFT, padx=10)

button3 = tk.Button(frame1, text="Button 3", command=button_click)
button3.pack(side=tk.LEFT, padx=10)

frame2 = tk.Frame(root, bd=5, relief=tk.GROOVE, bg="lightgreen")
frame2.pack(side=tk.TOP, padx=10, pady=10, fill=tk.X)

button4 = tk.Button(frame2, text="Button 4", command=button_click2)
button4.pack(side=tk.LEFT, padx=10)

button5 = tk.Button(frame2, text="Button 5", command=button_click)
button5.pack(side=tk.LEFT, padx=10)

label1 = tk.Label(frame2, text="Label 1", bg="lightgreen")
label1.pack(side=tk.LEFT, padx=10)

label2 = tk.Label(frame2, text="Label 2", bg="lightgreen")
label2.pack(side=tk.LEFT, padx=10)

root.mainloop()
