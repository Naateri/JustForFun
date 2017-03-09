import csv
import sys
import filters
games = list()
with open("primera_fase.csv", "rU") as f: #importing games 
	rows = csv.DictReader(f)
	for r in rows:
		games.append(r) #guardando los partidos

#print games

goBack = "quesoguei"

def menuPrincipal():
	print "1. Ver partidos de un jugador."
	print "2. Compare 2 jugadores."
	print "3. Ver estadisticas de un jugador."
	print "4. Instrucciones."
	print "5. Salir."
	menuPIng()

def instrucciones():
	print "Escribe un numero segun lo que quieras acceder (numeros a la izquierda)."
	print "Osea pls, eso ya debes saberlo si has llegado aqui."
	print "Para ver los partidos de un jugador, presionas 1, y apareceran los partidos que haya jugado."
	print "Para comparar 2 jugadores, pone primero el nombre del jugador con el que va a basar sus comparaciones. Esto le mostrara el record que tiene el jugador respecto al otro, ademas de goles a favor, en contra y diferencia de goles."
	print "En el caso quiera ver las estadisticas de un jugador, se le mostrara cuantas estadisticas se pueda imaginar. lol. Serio al 100% csm."
	menuPrincipal()

def menuPIng():
	a = input("Ingrese un numero: ")
	if a == 1:
		menu1()
	elif a == 2:
		menu2()
	elif a == 3:
		menu3()
	elif a == 4:
		instrucciones()
	elif a == 5:
		sys.exit()
	else:
		print "Numero no reconocido." 
		menuPrincipal()

def menu1Ing():
	player = raw_input("Ingrese el nombre del jugador (" + goBack + " para volver atras): ")
	player = player.lower()
	return player

def menu1():
	player = menu1Ing()
	mostrarPartidos(player)
	menu1()

def menu2():
	p1 = raw_input("Ingrese el nombre del primer jugador: (" + goBack + " para volver atras) ")
	if p1.lower() == goBack:
		menuPrincipal()
	else:
		p2 = raw_input("Ingrese el nombre del segundo jugador: ")
		compararJugadores(p1.lower(), p2.lower())
		menu2()
def menu3():
	player = menu1Ing()
	stats(player)
	menu3()

def mostrarPartidos(plyr):
	counter = 0
	if plyr == goBack:
		menuPrincipal()
	temp = games
	a = verTorneo()
	b = filters.wannafilter()
	if b: #si se quiere filtrar por algo
		filt = filters.filterMenu()
		if filt == 't':
			temp = filters.filterByTorneos(games)
		
	for game in temp:
		if game["jugadorL"] == plyr or game["jugadorV"] == plyr:
			counter += 1
			print game["game"] + ". " + game["jugadorL"].capitalize() + " " + game["golesL"] + " - " + game["golesV"] + " " + game["jugadorV"].capitalize()
			if a:
				print "Ocurrio en: " + game["torneo"]
	if counter == 0:
		print "Jugador no encontrado."

def verTorneo():
	a = raw_input("Desea ver en que torneo ocurrio? (s/n) ")
	a = a.lower()
	if a == "s":
		return True
	elif a == "n":
		return False
	else:
		verTorneo()

def compararJugadores(plyr1, plyr2):
	geims = list()
	counter = 0
	for game in games:
		if (game["jugadorL"] == plyr1 or game["jugadorV"] == plyr1) and (game["jugadorL"] == plyr2 or game["jugadorV"] == plyr2):
			geims.append(game) #metiendo los partidos de los dos a una lista
			counter += 1
	#if counter == 0:
	#	print "No se encontraron partidos."
	print "Partidos:"
	wins = 0
	draws = 0
	losses = 0 #todo evaluado hacia plyr1
	gf = 0
	gc = 0
	if counter == 0:
		print "No se encontraron partidos."
	else:
		temp = geims
		a = verTorneo()
		b = filters.wannafilter()
		if b: #si se quiere filtrar por algo
			filt = filters.filterMenu()
			if filt == 't':
				temp = filters.filterByTorneos(geims)

		for geim in temp:
			print geim["game"] + ". " + geim["jugadorL"].capitalize() + " " + geim["golesL"] + " - " + geim["golesV"] + " " + geim["jugadorV"].capitalize()
			if a:
				print "Ocurrio en: " + geim["torneo"]
			if geim["jugadorL"] == plyr1: #siendo p1 local
				gf += int(geim["golesL"])
				gc += int(geim["golesV"])
				if int(geim["golesL"]) > int(geim["golesV"]): #si hay mas goles local
					wins += 1
				elif int(geim["golesL"]) == int(geim["golesV"]): #si hubo la misma cant de goles
					draws += 1
				else: #si hubo mas goles de visita
					losses += 1
			else: #siendo p1 visitante
				gf += int(geim["golesV"])
				gc += int(geim["golesL"])
				if int(geim["golesL"]) > int(geim["golesV"]): #hay mas goles del local
					losses += 1 
				elif int(geim["golesL"]) == int(geim["golesV"]): #si hubo la misma cant de goles
					draws += 1
				else: #si hubo mas goles de visita
					wins += 1
		dg = gf-gc
		print "Record de " + plyr1.capitalize() + " sobre " + plyr2.capitalize() + ": "  + str(wins) + "-" + str(draws) + "-" + str(losses)
		print "Goles a favor: " + str(gf)
		print "Goles en contra: " + str(gc)
		print "Diferencia de goles: " + str(dg) 			

def stats(plyr):
	if plyr == goBack:
		menuPrincipal()
	geims = list()
	count = 0
	for game in games:
		if (game["jugadorL"] == plyr) or (game["jugadorV"] == plyr):
			geims.append(game)
			count +=1
	if count == 0:
		print "No se encontro al jugador."
	else:
		wins = 0
		draws = 0
		losses = 0
		gf = 0
		gc = 0
		dg = 0
		tpoints = 0
		avgpoints = 0 #puntos promedio por partido
		temp = geims
		#a = verTorneo()
		b = filters.wannafilter()
		if b: #si se quiere filtrar por algo
			filt = filters.filterMenu()
			if filt == 't':
				temp = filters.filterByTorneos(geims)

		for geim in geims:
			if geim["jugadorL"] == plyr:
				tpoints += int(geim["pml"])
				gf += int(geim["golesL"])
				gc += int(geim["golesV"])
				if int(geim["golesL"]) > int(geim["golesV"]):
					wins += 1
				elif int(geim["golesL"]) == int(geim["golesV"]):
					draws += 1
				else:
					losses += 1
			else:
				tpoints += int(geim["pmv"])
				gf += int(geim["golesV"])
				gc += int(geim["golesL"])				
				if int(geim["golesL"]) > int(geim["golesV"]):
					losses += 1
				elif int(geim["golesL"]) == int(geim["golesV"]):
					draws += 1
				else:
					wins += 1
		avgpoints = float(tpoints)/count
		dg = gf-gc
		print "Total de partidos: " + str(count)
		print "Goles a favor: " + str(gf)
		print "Goles en contra: " + str(gc)
		print "Diferencia de goles: " + str(dg)
		print "Total de puntos para mejorar: " + str(tpoints)
		print "Puntos para mejorar por partido: " + str(avgpoints)
		print "Partidos jugados: " + str(count)
		print "Record: " + str(wins) + "-" + str(draws) + "-" + str(losses)


def main():
	menuPrincipal()

main()
	
	
