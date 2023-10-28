import pandas

reader = pandas.read_excel("file_application.xlsx")
print(reader[reader["Date"] > pandas.to_datetime("15/02/2016", format="%d/%m/%Y")])
