pete_song = open("im_just_pete.txt", "r")
list1 = pete_song.readlines()
list_of_lists1 = [line.strip().split() for line in list1]
list_of_lists2 = [line.strip().split("\n") for line in list1]
print(list1)
print(list_of_lists1)
print(list_of_lists2)
# I don't know which one is the final goal
