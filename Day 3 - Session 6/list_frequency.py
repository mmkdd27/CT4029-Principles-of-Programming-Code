list1 = ["apples", "oranges", "duren", "food", 1, 5, 43, 9]
counted_words = []
for item in list1:
    if item not in counted_words:
        item_frequency = list1.count(item)
        print(item_frequency)
        counted_words.append(item)
