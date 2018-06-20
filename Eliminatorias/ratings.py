import csv;

players = ["Uruguay", "Argentina", "Brasil", "Ecuador", "Peru", "Bolivia", "Chile", "Paraguay", "Venezuela", "Colombia"];

def guardarPartidos(games):
	with open("games.csv", "rU") as f: #importing games 
		rows = csv.DictReader(f)
		for r in rows:
			games.append(r) #guardando los partidos

def sacandoRating(games):
	ratings = list();
	for player in players: #sacando el rating
	#############################
	#Formula del rating: 
	#(((victorias * 3) + (empates) - (derrotas*2) + diferencia de goles
	#+ (2*goles a favor) - goles en contra) + 100) / 2
	#############################
		geims = list() #array donde se guardan los juegos jugador por el jugador
		for game in games:
			if (game["jugadorL"] == player) or (game["jugadorV"] == player):
				geims.append(game)
		wins = 0
		draws = 0
		losses = 0
		gf = 0
		gc = 0
		dg = 0
		temp = geims
		for geim in geims:
			if geim["jugadorL"] == player:
				gf += int(geim["golesL"])
				gc += int(geim["golesV"])
				if int(geim["golesL"]) > int(geim["golesV"]):
					wins += 1
				elif int(geim["golesL"]) == int(geim["golesV"]):
					draws += 1
				else:
					losses += 1
			else:
				gf += int(geim["golesV"])
				gc += int(geim["golesL"])				
				if int(geim["golesL"]) > int(geim["golesV"]):
					losses += 1
				elif int(geim["golesL"]) == int(geim["golesV"]):
					draws += 1
				else:
					wins += 1
		dg = gf-gc
		rating = ((wins*3)+(draws)-(losses*2)+(2*gf)-(2*gc))+100
		rating = rating >> 1;
		ratings.append(rating);
	return ratings;

def getIndex(jug):
	for i in range(len(players)):
		if (players[i] == jug):
			return i;

