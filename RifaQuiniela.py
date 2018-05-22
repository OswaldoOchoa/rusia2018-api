from random import shuffle, choice

# Format of players: Name, GoodTeams, BadTeams
players = [
    ['Angel',0,0],
    ['Oswaldo',0,0],
    ['Ricardo',0,0],
    ['Fidel',0,0],
    ['Giovanni',0,0],
    ['Sergio',0,0],
    ['Miguel',0,0],
    ['Charly',0,0]
]

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

def raffle_players():
  print('--PLAYERS--')
  shuffle(players)
  print_list(players)
  print('\nEL SIGUIENTE ORDEN ES EL BUENO....')
  print('--PLAYERS--')
  shuffle(players)
  print_list(players)
  input('Presiona cualquier tecla para continuar')

def reset_players():
  global players
  m=0
  for n in players:
    players[m]=[n[0],0,0]
    m+=1

def print_list(list):
  for element in list:
    print(element[0])

def read_answer(question, fn):
  while True:
    decision = input(question).upper()
    if (
        decision == 'S'
        or decision == 'SI'
        or decision == ''
    ):
        fn()
        return True
    elif (
      decision == 'N'
      or decision == 'NO'
    ):
        print("Ok")
        return False
    else:
      print("Respuesta Invalida, intentalo de nuevo\n")
      continue

if __name__ == '__main__':
  read_answer('Deseas rifar el orden de los jugadores?(S/n)', raffle_players)
  raffle_done = read_answer('Deseas iniciar la rifa?(S/n)', raffleling)

  if raffle_done:
    print("\n ############# THE FINAL LIST!! #############\n")
    for n in range(len(players)):
      print("Los equipos para {} son:\n{},{},{} and {}.\n".format(players[n][0], players[n][7][0],players[n][8][0],players[n][9][0],players[n][10][0]))

  exit

