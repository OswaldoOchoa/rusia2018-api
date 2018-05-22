from random import shuffle, choice

players = [['Angel',0,0], ['Oswaldo',0,0], ['Ricardo',0,0], ['Fidel',0,0], ['Giovanni',0,0], ['Sergio',0,0], ['Miguel',0,0], ['Charly',0,0]]
# Format of players: Name, GoodTeams, BadTeams, GroupAB, GroupCD, GroupEF, GroupGH 


def raffleling():
    global players
    goodteams = [['Rusia','A'], ['Uruguay', 'A'], ['Espana', 'B'], ['Portugal', 'B'], ['Francia', 'C'], ['Dinamarca', 'C'], ['Argentina', 'D'], ['Croacia', 'D'], ['Brasil', 'E'], ['Suiza', 'E'], ['Alemania', 'F'], ['Mexico', 'F'], ['Belgica', 'G'], ['Inglaterra', 'G'], ['Colombia', 'H'], ['Polonia','H']]
    badteams = [['Arabia Saudi','A'], ['Egipto', 'A'], ['Marruecos', 'B'], ['Ri de Iran', 'B'], ['Australia', 'C'], ['Peru', 'C'], ['Islandia', 'D'], ['Nigeria', 'D'], ['Costa Rica', 'E'], ['Serbia', 'E'], ['Suecia', 'F'], ['Republica de Corea', 'F'], ['Tunez', 'G'], ['Panama', 'G'], ['Senegal', 'H'], ['Japon','H']]
    allteams = goodteams+badteams
    breaksituation = allteams.copy()
    iter = lambda x: x % len(players)
    n = 0
    repeated=False
    while len(allteams) !=0 or len(breaksituation) !=0:
        if repeated:
            repeated=False
            input("Presiona Enter")
        else:
            input("El siguiente equipo es para: " + players[iter(n)][0])
        team = choice(allteams)
        if team in goodteams and players[iter(n)][1]<2 and team[1] not in players[iter(n)]:
            players[iter(n)][1]+=1
            players[iter(n)].append(team)
            players[iter(n)].insert(3, team[1])
            breaksituation=allteams.copy()
            allteams.remove(team)
            n+=1
            input("El equipo es: " + team[0].upper() + "!!!\n")
        elif team in badteams and players[iter(n)][2]<2 and team[1] not in players[iter(n)]:
            players[iter(n)][2]+=1
            players[iter(n)].append(team)
            players[iter(n)].insert(3, team[1])
            breaksituation=allteams.copy()
            allteams.remove(team)
            n+=1
            input("El equipo es: " + team[0].upper() + "!!!\n")
        else:
            print("El equipo {} no esta disponible para {}, sus equipos son {}\nTry it Again!!\n".format(team[0], players[iter(n)][0], players[iter(n)][-((len(players[iter(n)])-3)//2):]))
            repeated=True
            pass
        if team in breaksituation:
            breaksituation.remove(team)
        if len(breaksituation)==0 and len(allteams)!=0:
            print("Lo siento, llegamos a un punto de no retorno, el jugador {} ya no puede elegir ninguno de los equipos restantes que son: {} \n\nEmpecemos de nuevo!!!\n\n".format(players[iter(n)], allteams))
            allteams = goodteams+badteams
            breaksituation = allteams.copy()
            reset_players()
            raffleling()
            break

def reset_players():
    global players
    m=0
    for n in players:
      players[m]=[n[0],0,0]
      m+=1


decision = input('\nPresiona para rifar DOS veces el orden de los jugadores\n')
while True:
    if decision.upper() == 'S' or 'SI':
        shuffle(players)
        print('--PLAYERS--')
        for n in players:
            print([n][0][0])
        shuffle(players)
        print('\nEL SIGUIENTE ORDEN ES EL BUENO....\n--PLAYERS--')
        for n in players:
            print([n][0][0])
        input()
        break
    elif decision.upper() == 'N' or 'NO':
        print("Ok")
        break
    else:
        decision = input("Respuesta Invalida, intentalo de nuevo?\n")


if decision.upper() == 'S' or 'SI':
    raffle = input("Presiona para iniciar la rifa\n")
    while True:
        if raffle.upper() == 'S' or 'SI':
            raffleling()
            print("\n THE FINAL LIST!!\n")
            for n in range(len(players)):
                print("Los equipos para {} son:\n{},{},{} and {}.\n".format(players[n][0], players[n][7][0],players[n][8][0],players[n][9][0],players[n][10][0]))
            break
        elif raffle.upper() == 'N' or 'NO':
            print("Ok")
            break
        else:
            raffle = input("Respuesta Invalida, intentalo de nuevo [Si/No]?\n")
            continue