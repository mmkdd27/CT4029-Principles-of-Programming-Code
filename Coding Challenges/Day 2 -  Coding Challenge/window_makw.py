import tkinter as tk

# Function to create a window with specific properties
def create_window(title, geometry):
    window = tk.Tk()
    window.title(title)
    window.geometry(geometry)
    label = tk.Label(window, text=f" {title} window!")
    label.pack(padx=20, pady=20)
    return window

window1 = create_window("first", "300x200+100+100")

window2 = create_window("second", "400x300+500+100")

window1.mainloop()
window2.mainloop()
