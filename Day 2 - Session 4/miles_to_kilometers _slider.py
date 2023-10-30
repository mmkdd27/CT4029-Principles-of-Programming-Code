import tkinter


def ml_to_km(miles1):
    km = float(miles1) * 1.609344
    kilo.config(text=km)


main = tkinter.Tk()
main.title("miles to kilometers converter")
miles = tkinter.Scale(main, from_=100, to=0, command=ml_to_km)
miles.pack()

kilo = tkinter.Label(main, text="move the slider to begin calculating")
kilo.pack(pady=20)
main.mainloop()
