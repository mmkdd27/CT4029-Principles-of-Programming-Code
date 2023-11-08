file1 = open("im_just_pete.txt", "r")
lines = file1.readlines()
middle_line = len(lines) // 2

lines.insert(middle_line, "something\n")

file2 =  open("im_just_pete.txt", "w")
file2.writelines(lines)
