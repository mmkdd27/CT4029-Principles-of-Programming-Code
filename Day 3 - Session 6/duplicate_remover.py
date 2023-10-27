list1 = ["apples", "oranges", "duren", "food", 1, 5, 43, 9, "oranges"]
duplicate_words = []

for item in list1:
    if item not in duplicate_words:

        duplicate_words.append(item)
    else:
        list1.remove(item)

print(list1)
