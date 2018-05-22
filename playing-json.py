import json
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
  for i in range(1, 9):
    choose_team(i)

def raffle_contenders():
  with open("users.json", "r") as file:
    data = json.load(file)

  users_list = data["users"]
  shuffle(users_list)
  print_contenders_order(users_list)

  with open("users.json", "w") as file:
    json.dump(data, file, indent=2*" ")

def valid_group(group, isFavorite):
  teams_list = [team for team in group
  ["teams"] if not team["picked"] and team["favorite"] == isFavorite]

  if teams_list == []:
    return False
  else:
    return True

def choose_team(user_id):
  data_users = read_json("users.json")
  users_list = data_users["users"]

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

      # all open groups
      data_groups = read_json("groups.json")
      groups_list = [group for group in data_groups["groups"] if not group["closed"]]

      # choose an open group untils is not previously chosen
      group_chosen = choice(groups_list)
      while(group_chosen["letter"] in user["groups"]
            or not valid_group(group_chosen, isFavorite)):
        group_chosen = choice(groups_list)

      teams_list = [team for team in group_chosen["teams"] if not team["picked"] and team["favorite"] == isFavorite]

      # choose an open group untils is not previously chosen
      team_chosen = choice(teams_list)

      team_chosen["picked"] = True

      # check if the group needs to be closed
      picked_teams = [team for team in group_chosen["teams"] if team["picked"]]
      if len(picked_teams) == 4:
        group_chosen["closed"] = True

      write_json("groups.json", data_groups)

      user["groups"].append(group_chosen["letter"])
      user["teams"].append({
          "name": team_chosen["name"],
          "favorite": team_chosen["favorite"]
          })
      write_json("users.json", data_users)
      break


if __name__ == "__main__":
  for i in range(4):
    run_one_round()
