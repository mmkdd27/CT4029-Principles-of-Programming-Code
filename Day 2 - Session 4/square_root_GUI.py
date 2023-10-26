import tkinter
import math

top = tkinter.Tk()

num = tkinter.Entry(top)
num.pack(side=tkinter.TOP)

def square_root():
    number =int(num.get())
    number =math.sqrt(number)
    print(number)
b = tkinter.Button(top,text="calculate square root",command=square_root)
b.pack()
top.mainloop()