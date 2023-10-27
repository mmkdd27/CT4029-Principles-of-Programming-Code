word1 = str(input("please enter the first word : "))
word2 = str(input("please enter the second word : "))
sort1 = sorted(word1)
sort2 = sorted(word2)
if sort1 == sort2:
    print ("the given words are anagrams")
else:
    print ("the given words are not anagrams")