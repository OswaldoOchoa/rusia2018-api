#!/bin/zsh

_groups_template="groups_template.json"
_users_template="users_template.json"

if [ "$1" = "groups" ]; then
  echo "Reset groups.json"
  cp $_groups_template "groups.json"
  exit 1
elif [ "$1" = "users" ]; then
    echo "Reset users.json"
  cp $_users_template "users.json"
    exit 1
else
  echo "Reset All"
  cp $_groups_template "groups.json"
  cp $_users_template "users.json"
fi