import pandas

reader = pandas.read_excel("file_application.xlsx")
print(reader[["Touches"]].agg(["sum", "mean", "max", "min"]))
