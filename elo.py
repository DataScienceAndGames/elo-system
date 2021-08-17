import sys

k = 20


def expected_result(elo1, elo2):
    return 1/(
        1+(10**((elo2-elo1)/400))
    )

def new_rank(base_elo, elo1, elo2, result): #computes new rank of player1
    return int(base_elo + k*(result-expected_result(elo1,elo2)))

players = []
with open("players.csv","r") as r:
    for line in r.readlines():
        split_line = line.split(",")
        players.append([split_line[0],split_line[1]])

for i in range(len(players)):
    players[i][1] = int(players[i][1])
#will assume that the two winners are written first, and that the two losers are written last

current_players = []

#next((x for x in test_list if x.value == value), None)

for i in range(1,5):
    this_player = None
    for x in range(len(players)):
        if players[x][0]==sys.argv[i]:
            this_player = x
    if this_player == None:
        print(f"Player {sys.argv[i]} not in list")
        quit()
    current_players.append(this_player)


    
players[current_players[0]][1] = new_rank(players[current_players[0]][1],(players[current_players[0]][1]+players[current_players[1]][1])//2,
(players[current_players[2]][1]+players[current_players[3]][1])//2,1)

players[current_players[1]][1] = new_rank(players[current_players[1]][1],(players[current_players[0]][1]+players[current_players[1]][1])//2,
(players[current_players[2]][1]+players[current_players[3]][1])//2,1)

players[current_players[2]][1] = new_rank(players[current_players[2]][1],(players[current_players[2]][1]+players[current_players[3]][1])//2,
(players[current_players[0]][1]+players[current_players[1]][1])//2,-1)

players[current_players[3]][1] = new_rank(players[current_players[3]][1],(players[current_players[2]][1]+players[current_players[3]][1])//2,
(players[current_players[0]][1]+players[current_players[1]][1])//2,-1)

for i in range(len(players)):
    players[i][1] = int(players[i][1])
    print(f"{players[i][1]} {players[i][0]}")

with open("players.csv","w") as w:
    for player in players:
        w.write(f"{player[0]},{player[1]}\n")