import pandas

reader = pandas.read_excel("file_application.xlsx")
number_players = int(input("how many players do you wish to find ? : "))
players = []
for i in range(0, number_players):
    print("now entering dtata for player", i + 1)
    name = input("whats the name ?")
    players.append(name)
print(reader[reader["Player Name"].isin(players)])
