from random import shuffle, choice

players = [['Cotty',0,0], ['Otoniel',0,0], ['Nereyda',0,0], ['Erik',0,0], ['Paulina',0,0], ['Oswaldo',0,0], ['P1',0,0], ['P2',0,0]]
# Format of players: Name, GoodTeams, BadTeams, GroupAB, GroupCD, GroupEF, GroupGH 


def raffleling():
    global players
    goodones2 = [['Rusia','A'], ['Uruguay', 'A'], ['Espana', 'B'], ['Portugal', 'B'], ['Francia', 'C'], ['Dinamarca', 'C'], ['Argentina', 'D'], ['Croacia', 'D'], ['Brasil', 'E'], ['Suiza', 'E'], ['Alemania', 'F'], ['Mexico', 'F'], ['Belgica', 'G'], ['Inglaterra', 'G'], ['Colombia', 'H'], ['Polonia','H']]
    badones2 = [['Arabia Saudi','A'], ['Egipto', 'A'], ['Marruecos', 'B'], ['Ri de Iran', 'B'], ['Australia', 'C'], ['Peru', 'C'], ['Islandia', 'D'], ['Nigeria', 'D'], ['Costa Rica', 'E'], ['Serbia', 'E'], ['Suecia', 'F'], ['Republica de Corea', 'F'], ['Tunez', 'G'], ['Panama', 'G'], ['Senegal', 'H'], ['Japon','H']]
    allteams = goodones2+badones2
    breaksituation = allteams
    iter = lambda x: x % len(players)
    n = 0
    #repeated=False
    print(len(breaksituation))
    while len(allteams) !=0 or len(breaksituation) !=0:
        #if repeated:
        #repeated=False
        #    input("Presiona Enter")
        #else:
        #    input("El siguiente equipo es para: " + players[iter(n)][0])
        team = choice(allteams)
        #input(team)
        #input(len(allteams))
        if team in goodones2 and players[iter(n)][1]<2 and team[1] not in players[iter(n)]:
            players[iter(n)][1]+=1
            players[iter(n)].append(team)
            players[iter(n)].insert(3, team[1])
            breaksituation=allteams
            allteams.remove(team)
            n+=1
            #print("El equipo es: " + team[0].upper() + "!!!")
        elif team in badones2 and players[iter(n)][2]<2 and team[1] not in players[iter(n)]:
            players[iter(n)][2]+=1
            players[iter(n)].append(team)
            players[iter(n)].insert(3, team[1])
            breaksituation=allteams
            allteams.remove(team)
            n+=1
            #print("El equipo es: " + team[0].upper() + "!!!")
        else:
            #print("El equipo {} no esta disponible para {}, Intentemoslo de nuevo!".format(team[0], players[iter(n)][0]))
            #repeated=True
            pass
        breaksituation.remove(team)
        if len(breaksituation)==0:
            input("Lo siento, llegamos a un punto de no retorno, el jugador {} ya no puede elegir ninguno de los equipos restantes, Empecemos de nuevo!!".format(players[iter(n)]))
            allteams = goodones2+badones2
            breaksituation = allteams
            raffleling()
    print("\n THE FINAL LIST!!\n")
    for n in range(len(players)):
        print("Los equipos para {} son:\n{},{},{} and {}.\n".format(players[n][0], players[n][7][0],players[n][8][0],players[n][9][0],players[n][10][0]))



decision = input('Quieres rifar el order de los jugadores? [Si/no]\n')
while True:
    if decision.upper() == 'S' or 'SI':
        shuffle(players)
        break
    elif decision.upper() == 'N' or 'NO':
        print("Ok")
        break
    else:
        decision = input("Respuesta Invalida, intentalo de nuevo? [Si/no]\n")



if decision.upper() == 'S' or 'SI':
    raffle = input("Quieres empezar la Rifa? [Si/no]\n")
    while True:
        if raffle.upper() == 'S' or 'SI':
            raffleling()
        elif raffle.upper() == 'N' or 'NO':
            print("Ok")
            break
        else:
            raffle = input("Respuesta Invalida, intentalo de nuevo [Si/No]?\n")
            continue
        break