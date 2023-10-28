import pandas
reader = pandas.read_excel("file_application.xlsx")
reader.set_index("Successful Passes Own Half",inplace=True)
print(reader)