file1 = open("im_just_pete.txt", "r")
lines1 = file1.read()

lines2 = lines1.splitlines()
middle = len(lines2) // 2

new1 = "something"
lines2.insert(middle, new1)

new2 = "\n".join(lines2)

file2 = open("im_just_pete.txt", "w")
file2.write(new2)
