list1 = ["apples", "oranges", "duren", "food", 1, 5, 43, 9]
duplicate_words = []

for item in list1:
    if item not in duplicate_words:

        duplicate_words.append(item)
    else:
        list1.remove(itemi)

print(list1)
