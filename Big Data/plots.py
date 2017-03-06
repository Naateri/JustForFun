# BONUS!
# Write a loop that interactively asks the user to enter a team name.
# If the team exists, print how many games the team played, how many
# yellow cards and red cards the team had, and the average number of
# minutes played by players on that team.
# If the team doesn't exist, print "Team not in 2010 World Cup".
# If 'quit' is entered, terminate the loop.
# Note: To read a string from the user instead of a number, use
# raw_input() instead of input()
# Resuelto mientras estaba privado jijijijojojo
import csv
cities = list()
with open("Cities.csv", "rU") as f:
	rows = csv.DictReader(f)
	for r in rows:
		cities.append(r)
countries = list()
with open("Countries.csv", "rU") as f:
	rows = csv.DictReader(f)
	for r in rows:
		countries.append(r)
teams = list()
with open("Teams.csv", "rU") as f:
	rows = csv.DictReader(f)
	for r in rows:
		teams.append(r)
players = list()
with open("Players.csv", "rU") as f:
	rows = csv.DictReader(f)
	for r in rows:
		players.append(r)


def avg_num_min(team):
	average = 0
	tplayers = 0
	tminutes = 0
	for player in players:
		if player["team"] == team:
			tplayers += 1
			tminutes += int(player["minutes"])
	average = tminutes/tplayers
	return average

def display():
	while True:
		tims = 0
		team = raw_input("Enter the name of a team: ")
		if team == "quit":
			break
		for tem in teams:
			#games = int(team["games"])
			#ycards = int(team["yellowCards"])
			#rcards = int(team["redCards"])
			if (tem["team"]) == team:
				print "Games played: ", tem["games"]
				print "Yellow cards: ", tem["yellowCards"]
				print "Red cards: ", tem["redCards"]
				print "Average minutes played by players: ", avg_num_min(team)
			else:
				tims += 1
		if tims == 32:
			print "Team not in 2010 World Cup"

def main():
	#lel = raw_input("Enter the name of a team: ")
	display()
	print "See you later!"

main()
