import pandas

reader = pandas.read_excel("file_application.xlsx")
print(reader[(reader["Rating"] > 80) & (reader["Total Successful Passes"] > 20)])
# there is no row matching this set of instructions
