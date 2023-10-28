import pandas

reader = pandas.read_excel("file_application.xlsx")
print(reader[["Player Name", "Position", "Time Played"]])
