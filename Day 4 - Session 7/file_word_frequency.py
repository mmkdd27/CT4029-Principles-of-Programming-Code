pete_song = open("im_just_pete.txt", "r")
word = str(input("please enter your word : ")).lower()
word_counter = 0
for i in pete_song:
    words = i.strip().split()
    for word in words:
        word.lower()
    word_counter += words.count(word)

print(word_counter)
pete_song.close()
