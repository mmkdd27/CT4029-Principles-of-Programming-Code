list1 = ["apples", "oranges", "duren", "food", 1, 5, 43, 9, ("tomatoes", "cucumbers")]
for i in list1:
    if isinstance(i, tuple):
        print("congrats its a tuple!")
    else:
        print("its not a tuple")
