import tkinter
import math

choose = tkinter.Tk()
choice = tkinter.IntVar()

square_root = tkinter.Radiobutton(choose, text="square root", variable=choice, value=1)
square_root.pack()

cube = tkinter.Radiobutton(choose, text="cube", variable=choice, value=2)
cube.pack()

factorial = tkinter.Radiobutton(choose, text="factorial", variable=choice, value=3)
factorial.pack()

enter = tkinter.Entry(choose)
enter.pack()


def calculate():
    num = float(enter.get())
    if choice.get() == 1:
        result = math.sqrt(num)
    elif choice.get() == 2:
        result = num ** 3
    elif choice.get() == 3:
        result = math.factorial(int(num))
    print(result)


calculater = tkinter.Button(choose, text="calculate", command=calculate)
calculater.pack(pady=10)
choose.mainloop()
