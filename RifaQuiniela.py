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
  good_teams = [
    ['Rusia','A'], ['Uruguay', 'A'], ['Espana', 'B'], ['Portugal', 'B'],
    ['Francia', 'C'], ['Dinamarca', 'C'], ['Argentina', 'D'], ['Croacia', 'D'],
    ['Brasil', 'E'], ['Suiza', 'E'], ['Alemania', 'F'], ['Mexico', 'F'],
    ['Belgica', 'G'], ['Inglaterra', 'G'], ['Colombia', 'H'], ['Polonia','H']
  ]
  bad_teams = [
    ['Arabia Saudi','A'], ['Egipto', 'A'], ['Marruecos', 'B'], ['Ri de Iran', 'B'],
    ['Australia', 'C'], ['Peru', 'C'], ['Islandia', 'D'], ['Nigeria', 'D'],
    ['Costa Rica', 'E'], ['Serbia', 'E'], ['Suecia', 'F'], ['Republica de Corea', 'F'],
    ['Tunez', 'G'], ['Panama', 'G'], ['Senegal', 'H'], ['Japon','H']
  ]

  all_teams = good_teams + bad_teams
  break_situation = all_teams.copy()
  iterator = lambda x: x % len(players)
  picked_teams = 0
  repeated = False

  while len(all_teams) != 0 or len(break_situation) != 0:
    if repeated:
      repeated = False
      input('Presiona Enter')
    else:
      input('El siguiente equipo es para: ' + players[iterator(picked_teams)][0])

    team = choice(all_teams)

    if (
      team in good_teams
      and players[iterator(picked_teams)][1]<2
      and team[1] not in players[iterator(picked_teams)]
    ):
      players[iterator(picked_teams)][1]+= 1
      players[iterator(picked_teams)].append(team)
      players[iterator(picked_teams)].insert(3, team[1])
      break_situation=all_teams.copy()
      all_teams.remove(team)
      picked_teams += 1
      input('El equipo es: ' + team[0].upper() + '!!!\n')
    elif (
      team in bad_teams
      and players[iterator(picked_teams)][2]<2
      and team[1] not in players[iterator(picked_teams)]
    ):
      players[iterator(picked_teams)][2]+= 1
      players[iterator(picked_teams)].append(team)
      players[iterator(picked_teams)].insert(3, team[1])
      break_situation=all_teams.copy()
      all_teams.remove(team)
      picked_teams += 1
      input('El equipo es: ' + team[0].upper() + '!!!\n')
    else:
      print(
        'El equipo {} no esta disponible para {}, sus equipos son {}\nTry it Again!!\n'.format(
        team[0],
        players[iterator(picked_teams)][0],
        players[iterator(picked_teams)][-((len(players[iterator(picked_teams)])-3)//2):])
      )
      repeated=True

    if team in break_situation:
      break_situation.remove(team)

    if len(break_situation) == 0 and len(all_teams) != 0:
      print(
        'El jugador {} ya no puede elegir ninguno de los equipos restantes: {} \n\nEmpecemos de nuevo!!!\n\n'.format(
        players[iterator(picked_teams)],
        all_teams)
      )
      all_teams = good_teams + bad_teams
      break_situation = all_teams.copy()
      reset_players()
      raffleling()
      break

def raffle_players():
  print('--PLAYERS--')
  shuffle(players)
  print_players_name(players)
  print('\nEL SIGUIENTE ORDEN ES EL BUENO....\n')
  print('--PLAYERS--')
  shuffle(players)
  print_players_name(players)
  input('----------------------------------------')

def reset_players():
  global players
  m=0
  for n in players:
    players[m]=[n[0],0,0]
    m+=1

def print_players_name(list):
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
        print('Ok')
        return False
    else:
      print('Respuesta Invalida, intentalo de nuevo\n')
      continue

if __name__ == '__main__':
  read_answer('Deseas rifar el orden de los jugadores?(S/n)\n', raffle_players)
  raffle_done = read_answer('Deseas iniciar la rifa?(S/n)\n', raffleling)

  if raffle_done:
    print('\n ############# THE FINAL LIST!! #############\n')
    for n in range(len(players)):
      print(
        'Los equipos para {} son:\n{},{},{} and {}.\n'.format(
        players[n][0],
        players[n][7][0],
        players[n][8][0],
        players[n][9][0],
        players[n][10][0])
      )

  exit

