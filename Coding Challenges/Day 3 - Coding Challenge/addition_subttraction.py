import tkinter
import math

choose = tkinter.Tk()
choice = tkinter.IntVar()

square_root = tkinter.Radiobutton(choose, text="addition", variable=choice, value=1)
square_root.pack()

cube = tkinter.Radiobutton(choose, text="subtraction", variable=choice, value=2)
cube.pack()


enter1 = tkinter.Entry(choose)
enter1.pack()
enter2 = tkinter.Entry(choose)
enter2.pack()

def calculate():
    num1 = float(enter1.get())
    num2 = float(enter2.get())
    if choice.get() == 1:
        result.set(num2+num1)
    elif choice.get() == 2:
        result.set(num2-num1)


calculater = tkinter.Button(choose, text="calculate", command=calculate)
calculater.pack(pady=10)

result = tkinter.StringVar()
result_label = tkinter.Label(choose, textvariable=result)
result_label.pack()

choose.mainloop()