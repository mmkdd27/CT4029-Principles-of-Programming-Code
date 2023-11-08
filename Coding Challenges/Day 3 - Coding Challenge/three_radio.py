import tkinter as tk

root = tk.Tk()
root.title("choose wisely!")

selected_option = tk.IntVar()

for i in range (0,3):
    tex = "option "+str(i)
    radio_button = tk.Radiobutton(root, text=tex, variable=selected_option,value= i)
    radio_button.pack()

root.mainloop()
