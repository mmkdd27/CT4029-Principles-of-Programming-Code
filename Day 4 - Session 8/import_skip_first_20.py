import pandas

reader = pandas.read_excel("file_application.xlsx")
print(reader.iloc[20:])
