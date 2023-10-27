word1 = str(input("Please enter the first word : "))
word2 = str(input("Please enter the second word : "))
sort1 = sorted(word1)
sort2 = sorted(word2)
if sort1 == sort2:
    print("The given words are anagrams")
else:
    print("The given words are not anagrams")
