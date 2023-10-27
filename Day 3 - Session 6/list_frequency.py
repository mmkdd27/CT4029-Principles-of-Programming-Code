list1 =["none","whatevrt","whatevrt","wuh"]
counted_words = []
for i in list1:
    if i not in counted_words:
        inum = list1.count(i)
        print(inum)
        counted_words.append(i)
