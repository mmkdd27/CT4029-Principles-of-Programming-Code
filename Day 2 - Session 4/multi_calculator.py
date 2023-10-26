import tkinter
import math

choose = tkinter.Tk()
choice = tkinter.IntVar()

square_root = tkinter.Radiobutton(choose,text="square root",variable= choice,value= 1 )
square_root.pack()

cube = tkinter.Radiobutton(choose,text="cube",variable= choice,value= 2 )
cube.pack()

factorial = tkinter.Radiobutton(choose,text="factorial" ,variable= choice,value= 3)
factorial.pack()

enter = tkinter.Entry(choose)
enter.pack()

def calculate(choice,num):
    if choice == 1:
        print(math.sqrt(mum))
    elif choice == 2:
        print((mum**2))
    elif choice == 3:
        print(math.factorial(mum))


entery = (enter.get())
print(entery)
tkinter.Button(choose,text="calculate",command=(lambda:calculate(choice,3)).pack(pady=10)
choose.mainloop()

