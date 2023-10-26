import tkinter

def calculate():
    value1 = int(entry1.get())
    value2 = int(entry2.get())
    operation = choice.get()

    if operation == 1:
        result.set(value1 + value2)
    elif operation == 2:
        result.set(value1 - value2)
    elif operation == 3:
        result.set(value1 * value2)
    elif operation == 4:
        result.set(value1 / value2)
calculator = tkinter.Tk()
calculator.title("Simple Calculator")

entry1_label = tkinter.Label(calculator, text="Enter first value:")
entry1_label.pack()
entry1 = tkinter.Entry(calculator)
entry1.pack()

entry2_label = tkinter.Label(calculator, text="Enter second value:")
entry2_label.pack()
entry2 = tkinter.Entry(calculator)
entry2.pack()

choice = tkinter.IntVar()

Addition_button = tkinter.Radiobutton(calculator, text="Addition", variable=choice, value=1)
Addition_button.pack()

Subtraction_button = tkinter.Radiobutton(calculator, text="Subtraction", variable=choice, value=2)
Subtraction_button.pack()

Multiplication_button = tkinter.Radiobutton(calculator, text="Multiplication", variable=choice, value=3)
Multiplication_button.pack()

Division_button = tkinter.Radiobutton(calculator, text="Division", variable=choice, value=4)
Division_button.pack()

calculate_button = tkinter.Button(calculator, text="Calculate", command=calculate)
calculate_button.pack()

result = tkinter.StringVar()
result_label = tkinter.Label(calculator, textvariable=result)
result_label.pack()

calculator.mainloop()
