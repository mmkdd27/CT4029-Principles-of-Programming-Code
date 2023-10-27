pete_song = open("im_just_pete.txt","r")
list = pete_song.readlines()
list_of_lists1 = [line.strip().split() for line in list]
list_of_lists2 = [line.strip().split("\n") for line in list]
print(list)
print(list_of_lists1)
print(list_of_lists2)
#i dont know which one is the final goal