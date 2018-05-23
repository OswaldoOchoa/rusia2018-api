import json
import subprocess
from random import shuffle, choice

#Utils
def print_contenders_order(users):
  for contender in users:
      print(contender["name"])

def print_pretty_dict(dict):
  print(json.dumps(dict, indent=2*" "))

def read_json(filePath):
  with open(filePath, 'r') as file:
    data = json.load(file)
  return data

def write_json(filePath, data):
  with open(filePath, 'w') as file:
    json.dump(data, file, indent=2*" ")

#Raffle
def run_one_round():
  user_list = raffle_contenders()
  for user in user_list:
    done = raffle(user["id"])
    if not done:
      return False
  return True

def raffle_contenders():
  with open("users.json", "r") as file:
    data = json.load(file)

  users_list = data["users"]
  shuffle(users_list)
  print_contenders_order(users_list)
  print('----------------------------')

  with open("users.json", "w") as file:
    json.dump(data, file, indent=2*" ")

  return users_list

def valid_group(group, isFavorite):
  teams_list = [team for team in group
  ["teams"] if not team["picked"] and team["favorite"] == isFavorite]

  if teams_list == []:
    return False
  else:
    return True

def get_user_data(user_id, users_list):
  for user in users_list:
    if user["id"] == user_id:
      #Decide if choose a favorite team
      user_teams = user["teams"]
      good_teams = len([team["favorite"] for team in user_teams if team["favorite"] == True])
      bad_teams = len([team["favorite"] for team in user_teams if team["favorite"] == False])

      if (good_teams == 2):
        isFavorite = False
      elif (bad_teams == 2):
        isFavorite = True
      else:
        isFavorite = choice([True, False])

      return {
        "user": user,
        "favorite": isFavorite
      }

def choose_group(user_data, groups_list):
  user = user_data["user"]
  isFavorite = user_data["favorite"]
  open_groups = [group for group in groups_list if not group["closed"]]
  available_groups = [group for group in open_groups if group["letter"] not in user["groups"] and valid_group(group, isFavorite)]

  groups_qty = len(available_groups)
  if groups_qty == 0:
    print("---------------------------------------------")
    print("########ERROR: Can't continue, restarting...")
    print("########USER:")
    print_pretty_dict(user)
    print("########OPEN GROUPS:")
    print_pretty_dict(open_groups)
    print("---------------------------------------------")
    return False
  elif groups_qty == 1:
    return available_groups[0]
  else:
    return choice(available_groups)

def choose_team(user_data, group):
  isFavorite = user_data["favorite"]

  teams_list = [team for team in group["teams"] if not team["picked"] and team["favorite"] == isFavorite]
  team_chosen = choice(teams_list)

  return team_chosen

def verify_group(group):
    # check if the group needs to be closed
  picked_teams = [team for team in group["teams"] if team["picked"]]

  if len(picked_teams) == 4:
    group["closed"] = True
    return True

def raffle(user_id):
  try:
    data_groups = read_json("groups.json")
    groups_list = data_groups["groups"]

    data_users = read_json("users.json")
    users_list = data_users["users"]

    user_data = get_user_data(user_id, users_list)
    user = user_data["user"]

    group_chosen = choose_group(user_data, groups_list)

    if group_chosen == False:
      return False

    user["groups"].append(group_chosen["letter"])

    team_chosen = choose_team(user_data, group_chosen)
    team_chosen["picked"] = True
    user["teams"].append({
      "name": team_chosen["name"],
      "favorite": team_chosen["favorite"]
    })

    group_closed = verify_group(group_chosen)

    write_json("groups.json", data_groups)
    write_json("users.json", data_users)

    return True
  except Exception as ex:
    print(ex)
    return False

def run():
  subprocess.call(['./reset.sh'])
  for i in range(4):
    valid_round = run_one_round()
    if not valid_round:
      break
  if not valid_round:
    run()

if __name__ == "__main__":
  run()
