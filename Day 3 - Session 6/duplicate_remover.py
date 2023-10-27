list1 =["none","whatevrt","whatevrt","wuh",1,2,3,4,1]
duplicate_words = []

for i in list1:
    if i not in duplicate_words:

        duplicate_words.append(i)
    else:
        list1.remove(i)

print(list1)