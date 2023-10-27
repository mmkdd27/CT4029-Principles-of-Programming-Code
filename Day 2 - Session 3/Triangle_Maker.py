def func(rows, character):
    for i in range(0, 9):
        for q in range(i + 1, rows):
            print(" ", end="")
        for j in range(0, 2 * i + 1):
            print(character, end="")
        print()


func(10, "#")
func(10, "*")
