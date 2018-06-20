import csv
from random import random

loopies = 10000; #cantidad de simulaciones

games = list()
ratings = list() #se van a guardar los ratings de 0 a 99 que salgan
#segun los partidos
#en el siguiente orden:
#Chichico, Diego, FAMO, Pachec, Ganzo, Chavez, Queso, Barbachan, Cuajo
players = ["Chichico", "Diego", "FAMO", "Pachec", "Ganzo", "Chavez", "Queso", "Barbachan", "Cuajo"] 

with open("pachec.csv", "rU") as f: #importing games 
	rows = csv.DictReader(f)
	for r in rows:
		games.append(r) #guardando los partidos

def sacandoRating():
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
		rating = ((wins*3)+(draws)-(losses*2)+(dg)+(2*gf)-(gc))+100
		rating = rating >> 1;
		ratings.append(rating)

def getIndex(jug):
	for i in range(len(players)):
		if (players[i] == jug):
			return i;

############FUNCIONES PARA SIMULAR PARTIDOS###
##############################################

def simularPartido(jug1, jug2): #basado en probabilidades (ratings)
	rat1 = float(ratings[getIndex(jug1)]);
	rat2 = float(ratings[getIndex(jug2)]);
	probDe1 = (rat1 + (100-rat2))/2;
	probDe2 = (rat2 + (100-rat1))/2;
	#probDe1 /= 100;
	#probDe2 /= 100;
	maxi = max(probDe1, probDe2);
	if (random() < maxi/100):
		if (maxi == probDe1):
			return jug1;
		else: 
			return jug2;
	else:
  		if (maxi == probDe1):
			return jug2;
		else: 
			return jug1;
	 
def simularNPartidos(jug1, jug2, n = 255):
	ganaJug1 = 0;
	ganaJug2 = 0;
	for i in range(n):
		resultado = simularPartido(jug1, jug2);
		if (resultado == jug1):
			ganaJug1 += 1;
		else:
			ganaJug2 += 1;
	if (ganaJug1 == ganaJug2):
		return simularNPartidos(jug1, jug2, n);		
	return ganaJug1, ganaJug2;

def simularNPartidosD(jug1, jug2, n = 70): #Simulando partidos empate incluido
	ganaJug1 = 0;
	ganaJug2 = 0;
	for i in range(n):
		resultado = simularPartido(jug1, jug2);
		if (resultado == jug1):
			ganaJug1 += 1;
		else:
			ganaJug2 += 1;
	return ganaJug1, ganaJug2;

######FUNCIONES DE SIMULACION DEL TORNEO###############

def repechaje1():
	a,b = simularNPartidos("Cuajo", "Barbachan");
	if (a > b):
		repe1 = "Cuajo";
		noveno = "Barbachan";
	else:
		repe1 = "Barbachan";
		noveno = "Cuajo";
	return repe1, noveno;

def repechaje2(repe1):
	a,b = simularNPartidos("Queso", repe1);
	if (a > b):
		repe2 = "Queso";
		octavo = repe1; 
	else:
		repe2 = repe1;
		octavo = "Queso";
	return repe2, octavo;

def repechaje3(repe2):
	a,b = simularNPartidos("Ganzo", repe2);
	if (a > b):
		uRepe = "Ganzo";
		septimo = repe2;
	else:
		uRepe = repe2;
		septimo = "Ganzo";
	return uRepe,septimo;

def repechajes():
	repe1 = repechaje1()[0]; #primer partido
	repe2 = repechaje2(repe1)[0]; #segundo partido
	return repechaje3(repe2)[0]; #ultimo repechaje

def fecha13(a, b, c, d, e, r3, puntos):
	res1, res2 = simularNPartidosD(a, d);
	if (res1 > res2):
		puntos[0][0] += 3;
	elif (res1 < res2):
		puntos[3][0] += 3;
	else:
		puntos[0][0] += 1;
		puntos[3][0] += 1;
	res1, res2 = simularNPartidosD(d, a);
	if (res1 > res2):
		puntos[3][0] += 3;
	elif (res1 < res2):
		puntos[0][0] += 3;
	else:
		puntos[0][0] += 1;
		puntos[3][0] += 1;
	res1, res2 = simularNPartidosD(e, c);
	if (res1 > res2):
		puntos[4][0] += 3;
	elif (res1 < res2):
		puntos[2][0] += 3;
	else:
		puntos[4][0] += 1;
		puntos[2][0] += 1;
	res1, res2 = simularNPartidosD(c, e);
	if (res1 > res2):
		puntos[2][0] += 3;
	elif (res1 < res2):
		puntos[4][0] += 3;
	else:
		puntos[4][0] += 1;
		puntos[2][0] += 1;
	res1, res2 = simularNPartidosD(r3, b);
	if (res1 > res2):
		puntos[5][0] += 3;
	elif (res1 < res2):
		puntos[1][0] += 3;
	else:
		puntos[5][0] += 1;
		puntos[1][0] += 1;
	res1, res2 = simularNPartidosD(b, r3);
	if (res1 > res2):
		puntos[1][0] += 3;
	elif (res1 < res2):
		puntos[5][0] += 3;
	else:
		puntos[5][0] += 1;
		puntos[1][0] += 1;

def fecha14(a, b, c, d, e, r3, puntos):
	#res1, res2 = simularNPartidosD(d, c);
	#if (res1 > res2):
	#	puntos[3][0] += 3;
	#elif (res1 < res2):
	#	puntos[2][0] += 3;
	#else:
	#	puntos[3][0] += 1;
	#	puntos[2][0] += 1;
	#res1, res2 = simularNPartidosD(c, d);
	#if (res1 > res2):
	#	puntos[2][0] += 3;
	#elif (res1 < res2):
	#	puntos[3][0] += 3;
	#else:
	#	puntos[2][0] += 1;
	#	puntos[3][0] += 1;
	#res1, res2 = simularNPartidosD(r3, a);
	#if (res1 > res2):
	#	puntos[5][0] += 3;
	#elif (res1 < res2):
	#	puntos[0][0] += 3;
	#else:
	#	puntos[5][0] += 1;
	#	puntos[0][0] += 1;
	#res1, res2 = simularNPartidosD(a, r3);
	#if (res1 > res2):
	#	puntos[0][0] += 3;
	#elif (res1 < res2):
	#	puntos[5][0] += 3;
	#else:
	#	puntos[5][0] += 1;
	#	puntos[0][0] += 1;
	res1, res2 = simularNPartidosD(e, b);
	if (res1 > res2):
		puntos[4][0] += 3;
	elif (res1 < res2):
		puntos[1][0] += 3;
	else:
		puntos[4][0] += 1;
		puntos[1][0] += 1;
	res1, res2 = simularNPartidosD(b, e);
	if (res1 > res2):
		puntos[1][0] += 3;
	elif (res1 < res2):
		puntos[4][0] += 3;
	else:
		puntos[4][0] += 1;
		puntos[1][0] += 1;

def fecha15(a, b, c, d, e, r3, puntos):
	res1, res2 = simularNPartidosD(d, r3);
	if (res1 > res2):
		puntos[3][0] += 3;
	elif (res1 < res2):
		puntos[5][0] += 3;
	else:
		puntos[3][0] += 1;
		puntos[5][0] += 1;
	res1, res2 = simularNPartidosD(r3, d);
	if (res1 > res2):
		puntos[5][0] += 3;
	elif (res1 < res2):
		puntos[3][0] += 3;
	else:
		puntos[5][0] += 1;
		puntos[3][0] += 1;
	res1, res2 = simularNPartidosD(c, b);
	if (res1 > res2):
		puntos[2][0] += 3;
	elif (res1 < res2):
		puntos[1][0] += 3;
	else:
		puntos[2][0] += 1;
		puntos[1][0] += 1;
	res1, res2 = simularNPartidosD(b, c);
	if (res1 > res2):
		puntos[1][0] += 3;
	elif (res1 < res2):
		puntos[2][0] += 3;
	else:
		puntos[2][0] += 1;
		puntos[1][0] += 1;
	res1, res2 = simularNPartidosD(e, a);
	if (res1 > res2):
		puntos[4][0] += 3;
	elif (res1 < res2):
		puntos[0][0] += 3;
	else:
		puntos[4][0] += 1;
		puntos[0][0] += 1;
	res1, res2 = simularNPartidosD(a, e);
	if (res1 > res2):
		puntos[0][0] += 3;
	elif (res1 < res2):
		puntos[4][0] += 3;
	else:
		puntos[4][0] += 1;
		puntos[0][0] += 1;

def fecha16(a, b, c, d, e, r3, puntos):
	res1, res2 = simularNPartidosD(d, b);
	if (res1 > res2):
		puntos[3][0] += 3;
	elif (res1 < res2):
		puntos[1][0] += 3;
	else:
		puntos[3][0] += 1;
		puntos[1][0] += 1;
	res1, res2 = simularNPartidosD(b, d);
	if (res1 > res2):
		puntos[1][0] += 3;
	elif (res1 < res2):
		puntos[3][0] += 3;
	else:
		puntos[1][0] += 1;
		puntos[3][0] += 1;
	res1, res2 = simularNPartidosD(c, a);
	if (res1 > res2):
		puntos[2][0] += 3;
	elif (res1 < res2):
		puntos[0][0] += 3;
	else:
		puntos[2][0] += 1;
		puntos[0][0] += 1;
	res1, res2 = simularNPartidosD(a, c);
	if (res1 > res2):
		puntos[0][0] += 3;
	elif (res1 < res2):
		puntos[2][0] += 3;
	else:
		puntos[2][0] += 1;
		puntos[0][0] += 1;
	res1, res2 = simularNPartidosD(e, r3);
	if (res1 > res2):
		puntos[4][0] += 3;
	elif (res1 < res2):
		puntos[5][0] += 3;
	else:
		puntos[4][0] += 1;
		puntos[5][0] += 1;
	res1, res2 = simularNPartidosD(r3, e);
	if (res1 > res2):
		puntos[5][0] += 3;
	elif (res1 < res2):
		puntos[4][0] += 3;
	else:
		puntos[4][0] += 1;
		puntos[5][0] += 1;

def fecha17(a, b, c, d, e, r3, puntos):
	res1, res2 = simularNPartidosD(d, e);
	if (res1 > res2):
		puntos[3][0] += 3;
	elif (res1 < res2):
		puntos[4][0] += 3;
	else:
		puntos[3][0] += 1;
		puntos[4][0] += 1;
	res1, res2 = simularNPartidosD(e, d);
	if (res1 > res2):
		puntos[4][0] += 3;
	elif (res1 < res2):
		puntos[3][0] += 3;
	else:
		puntos[4][0] += 1;
		puntos[3][0] += 1;
	res1, res2 = simularNPartidosD(a, b);
	if (res1 > res2):
		puntos[0][0] += 3;
	elif (res1 < res2):
		puntos[1][0] += 3;
	else:
		puntos[0][0] += 1;
		puntos[1][0] += 1;
	res1, res2 = simularNPartidosD(b, a);
	if (res1 > res2):
		puntos[1][0] += 3;
	elif (res1 < res2):
		puntos[0][0] += 3;
	else:
		puntos[2][0] += 1;
		puntos[0][0] += 1;
	res1, res2 = simularNPartidosD(c, r3);
	if (res1 > res2):
		puntos[2][0] += 3;
	elif (res1 < res2):
		puntos[5][0] += 3;
	else:
		puntos[2][0] += 1;
		puntos[5][0] += 1;
	res1, res2 = simularNPartidosD(r3, c);
	if (res1 > res2):
		puntos[5][0] += 3;
	elif (res1 < res2):
		puntos[2][0] += 3;
	else:
		puntos[2][0] += 1;
		puntos[5][0] += 1;


def segundaFase():
	#r3 = repechajes();
	r3 = "Queso";
	a = "Chichico";
	b = "Diego";
	c = "FAMO";
	d = "Pachec";
	e = "Chavez";
	#puntos = [[0, a], [0, b], [0, c], [0, d], [0, e], [0, r3]];
	puntos = [[9, a], [3, b], [9, c], [0, d], [3, e], [6, r3]];
	#puntos[0][1] = a;
	#puntos[1][1] = b;
	#puntos[2][1] = c;
	#puntos[3][1] = d;
	#puntos[4][1] = e;
	#puntos[5][1] = r3;
	#fecha13(a, b, c, d, e, r3, puntos);
	fecha14(a, b, c, d, e, r3, puntos);
	fecha15(a, b, c, d, e, r3, puntos);
	fecha16(a, b, c, d, e, r3, puntos);
	fecha17(a, b, c, d, e, r3, puntos);
	return puntos;

######################################################################################
#FUNCIONES DE SIMULACION DE PUESTOS#####################

def novenoPuesto(n = loopies):
	barbachan = 0.0
	cuajo = 0.0	
	for i in range(n):
		if (repechaje1()[1] == "Cuajo"):
			cuajo += 1;
		else:
			barbachan += 1;
	cuajo = float((cuajo * 100) / n);
	print "Posibilidades de acabar noveno: ";
	print "Cuajo: " + str(cuajo) + "%";
	print "Barbachan: " + str(100.0 - cuajo) + "%";

def octavoPuesto(n = loopies):
	barbachan = 0.0;
	cuajo = 0.0;
	queso = 0.0;
	for i in range(n):
		repe1 = repechaje1()[0];
		octavo = repechaje2(repe1)[1];
		if (octavo == "Queso"):
			queso += 1;
		elif (octavo == "Barbachan"):
			barbachan += 1;
		else:
			cuajo += 1;
	queso = float((queso * 100) / n);
	barbachan = float((barbachan * 100) / n);	
	cuajo = float((cuajo * 100) / n);
	print "Posibilidades de acabar octavo: ";
	print "Queso: " + str(queso) + "%";
	print "Barbachan: " + str(barbachan) + "%";
	print "Cuajo: " + str(cuajo) + "%";

def septimoPuesto(n = loopies):
	#barbachan = 0.0;
	#cuajo = 0.0;
	queso = 0.0;
	ganzo = 0.0;
	for i in range(n):
		#repe1 = repechaje1()[0];
		#repe2 = repechaje2(repe1)[0];
		repe2 = "Queso";
		septimo = repechaje3(repe2)[1]
		if (septimo == "Queso"):
			queso += 1;
		#elif (septimo == "Ganzo"):
		#	ganzo += 1;
		#elif (septimo == "Barbachan"):
		#	barbachan += 1;
		#else:
		#	cuajo += 1;
		else:
			ganzo += 1;
	ganzo = float((ganzo * 100) / n);			
	queso = float((queso * 100) / n);
	#barbachan = float((barbachan * 100) / n);	
	#cuajo = float((cuajo * 100) / n);
	print "Posibilidades de acabar septimo: ";
	print "Ganzo: " + str(ganzo) + "%";
	print "Queso: " + str(queso) + "%";
	#print "Barbachan: " + str(barbachan) + "%";
	#print "Cuajo: " + str(cuajo) + "%";
			
def pasaRepechaje(n = loopies):
	#barbachan = 0.0;
	#cuajo = 0.0;
	queso = 0.0;
	ganzo = 0.0;
	for i in range(n):
		#pasa = repechajes();
		repe2 = "Queso";
		pasa = repechaje3(repe2)[0]
		if (pasa == "Ganzo"):
			ganzo += 1;
		elif (pasa == "Queso"):
			queso += 1;
		#elif (pasa == "Barbachan"):
		#	barbachan += 1;
		#else:
		#	barbachan += 1;
	ganzo = float((ganzo * 100) / n);			
	queso = float((queso * 100) / n);
	#barbachan = float((barbachan * 100) / n);	
	#cuajo = float((cuajo * 100) / n);
	print "Posibilidades de pasar el repechaje: ";
	print "Ganzo: " + str(ganzo) + "%";
	print "Queso: " + str(queso) + "%";
	#print "Barbachan: " + str(barbachan) + "%";
	#print "Cuajo: " + str(cuajo) + "%";

def sextoPuesto(n = loopies):
	lel = n;
	barbachan = 0.0;
	queso = 0.0;
	ganzo = 0.0;
	pachec = 0.0;
	chavez = 0.0;
	famo = 0.0;
	diego = 0.0;
	chichico = 0.0;
	for i in range(n):
		puntos1 = segundaFase();
		puntos1.sort();
		puntos1.reverse();
		o = puntos1[5];
		ne = puntos1[4];
		if (ne == puntos1[3]): #en caso de que el 4to y el 5to tengan la misma cantidad
			lel -= 1;
			continue; #de puntos pues gg
		a,b = simularNPartidos(ne[1], o[1]);
		if (a > b):
			sexto = o[1];
		else:
			sexto = ne[1];
		#if (sexto == "Ganzo"):
		#	ganzo += 1;
		if (sexto == "Queso"):
			queso += 1;
		elif (sexto == "Pachec"):
			pachec += 1;
		elif (sexto == "Chavez"):
			chavez += 1;
		#elif (sexto == "Barbachan"):
		#	barbachan += 1;
		elif (sexto == "FAMO"):
			famo += 1;
		elif (sexto == "Diego"):
			diego += 1;
		else:
			chichico += 1; 
	#ganzo = float((ganzo * 100) / lel);			
	queso = float((queso * 100) / lel);
	#barbachan = float((barbachan * 100) / lel);	
	pachec = float((pachec * 100) / lel);
	chavez = float((chavez * 100) / lel);
	famo = float((famo * 100) / lel);
	diego = float((diego * 100) / lel);
	chichico = float((chichico * 100) / lel);
	print "Posibilidades de acabar sexto: ";
	#print "Ganzo: " + str(ganzo) + "%";
	print "Queso: " + str(queso) + "%";
	#print "Barbachan: " + str(barbachan) + "%";
	print "Pachec: " + str(pachec) + "%";
	print "Chavez: " + str(chavez) + "%";
	print "FAMO: " + str(famo) + "%";
	print "Diego: " + str(diego) + "%";
	print "Chichico: " + str(chichico) + "%";

def quintoPuesto(n = loopies):
	lel = n;
	barbachan = 0.0;
	queso = 0.0;
	ganzo = 0.0;
	pachec = 0.0;
	chavez = 0.0;
	famo = 0.0;
	diego = 0.0;
	chichico = 0.0;
	for i in range(n):
		puntos1 = segundaFase();
		puntos1.sort();
		puntos1.reverse();
		o = puntos1[5];
		ne = puntos1[4];
		if (ne == puntos1[3]): #en caso de que el 4to y el 5to tengan la misma cantidad
			lel -= 1;
			continue; #de puntos pues gg
		a,b = simularNPartidos(ne[1], o[1]);
		if (a > b):
			quinto = ne[1];
		else:
			quinto = o[1];
		#if (quinto == "Ganzo"):
		#	ganzo += 1;
		if (quinto == "Queso"):
			queso += 1;
		elif (quinto == "Pachec"):
			pachec += 1;
		elif (quinto == "Chavez"):
			chavez += 1;
		#elif (quinto == "Barbachan"):
		#	barbachan += 1;
		elif (quinto == "FAMO"):
			famo += 1;
		elif (quinto == "Diego"):
			diego += 1;
		else:
			chichico += 1; 
	#ganzo = float((ganzo * 100) / lel);			
	queso = float((queso * 100) / lel);
	#barbachan = float((barbachan * 100) / lel);	
	pachec = float((pachec * 100) / lel);
	chavez = float((chavez * 100) / lel);
	famo = float((famo * 100) / lel);
	diego = float((diego * 100) / lel);
	chichico = float((chichico * 100) / lel);
	print "Posibilidades de acabar quinto: ";
	#print "Ganzo: " + str(ganzo) + "%";
	print "Queso: " + str(queso) + "%";
	#print "Barbachan: " + str(barbachan) + "%";
	print "Pachec: " + str(pachec) + "%";
	print "Chavez: " + str(chavez) + "%";
	print "FAMO: " + str(famo) + "%";
	print "Diego: " + str(diego) + "%";
	print "Chichico: " + str(chichico) + "%";

def cuartoPuesto(n = loopies):
	lel = n;
	barbachan = 0.0;
	queso = 0.0;
	ganzo = 0.0;
	pachec = 0.0;
	chavez = 0.0;
	famo = 0.0;
	diego = 0.0;
	chichico = 0.0;
	for i in range(n):
		puntos1 = segundaFase();
		puntos1.sort();
		puntos1.reverse();
		m = puntos1[3];
		if (m == puntos1[4]): #en caso de que el 4to y el 5to tengan la misma cantidad
			lel -= 1;
			continue; #de puntos pues gg
		l = puntos1[2];
		if (l == puntos1[1]):
			lel -= 1;
			continue;
		a,b = simularNPartidos(l[1], m[1]);
		if (a > b):
			cuarto = m[1];
		else:
			cuarto = l[1];
		#if (cuarto == "Ganzo"):
		#	ganzo += 1;
		if (cuarto == "Queso"):
			queso += 1;
		elif (cuarto == "Pachec"):
			pachec += 1;
		elif (cuarto == "Chavez"):
			chavez += 1;
		#elif (cuarto == "Barbachan"):
		#	barbachan += 1;
		elif (cuarto == "FAMO"):
			famo += 1;
		elif (cuarto == "Diego"):
			diego += 1;
		else:
			chichico += 1; 
	#ganzo = float((ganzo * 100) / lel);			
	queso = float((queso * 100) / lel);
	#barbachan = float((barbachan * 100) / lel);	
	pachec = float((pachec * 100) / lel);
	chavez = float((chavez * 100) / lel);
	famo = float((famo * 100) / lel);
	diego = float((diego * 100) / lel);
	chichico = float((chichico * 100) / lel);
	print "Posibilidades de acabar cuarto: ";
	#print "Ganzo: " + str(ganzo) + "%";
	print "Queso: " + str(queso) + "%";
	#print "Barbachan: " + str(barbachan) + "%";
	print "Pachec: " + str(pachec) + "%";
	print "Chavez: " + str(chavez) + "%";
	print "FAMO: " + str(famo) + "%";
	print "Diego: " + str(diego) + "%";
	print "Chichico: " + str(chichico) + "%";

def tercerPuesto(n = loopies):
	lel = n;
	barbachan = 0.0;
	queso = 0.0;
	ganzo = 0.0;
	pachec = 0.0;
	chavez = 0.0;
	famo = 0.0;
	diego = 0.0;
	chichico = 0.0;
	for i in range(n):
		puntos1 = segundaFase();
		puntos1.sort();
		puntos1.reverse();
		m = puntos1[3];
		if (m == puntos1[4]): #en caso de que el 4to y el 5to tengan la misma cantidad
			lel -= 1;
			continue; #de puntos pues gg
		l = puntos1[2];
		if (l == puntos1[1]):
			lel -= 1;
			continue;
		a,b = simularNPartidos(l[1], m[1]);
		if (a > b):
			tercero = l[1];
		else:
			tercero = m[1];
		#if (tercero == "Ganzo"):
		#	ganzo += 1;
		if (tercero == "Queso"):
			queso += 1;
		elif (tercero == "Pachec"):
			pachec += 1;
		elif (tercero == "Chavez"):
			chavez += 1;
		#elif (tercero == "Barbachan"):
		#	barbachan += 1;
		elif (tercero == "FAMO"):
			famo += 1;
		elif (tercero == "Diego"):
			diego += 1;
		else:
			chichico += 1; 
	#ganzo = float((ganzo * 100) / lel);			
	queso = float((queso * 100) / lel);
	#barbachan = float((barbachan * 100) / lel);	
	pachec = float((pachec * 100) / lel);
	chavez = float((chavez * 100) / lel);
	famo = float((famo * 100) / lel);
	diego = float((diego * 100) / lel);
	chichico = float((chichico * 100) / lel);
	print "Posibilidades de acabar tercero: ";
	#print "Ganzo: " + str(ganzo) + "%";
	print "Queso: " + str(queso) + "%";
	#print "Barbachan: " + str(barbachan) + "%";
	print "Pachec: " + str(pachec) + "%";
	print "Chavez: " + str(chavez) + "%";
	print "FAMO: " + str(famo) + "%";
	print "Diego: " + str(diego) + "%";
	print "Chichico: " + str(chichico) + "%";

def segundoPuesto(n = loopies):
	lel = n;
	barbachan = 0.0;
	queso = 0.0;
	ganzo = 0.0;
	pachec = 0.0;
	chavez = 0.0;
	famo = 0.0;
	diego = 0.0;
	chichico = 0.0;
	for i in range(n):
		puntos1 = segundaFase();
		puntos1.sort();
		puntos1.reverse();
		k = puntos1[1];
		if (k == puntos1[2]): #en caso de que el 2do y el 3ro tengan la misma cantidad
			lel -= 1;
			continue; #de puntos pues gg
		j = puntos1[0];
		a,b = simularNPartidos(j[1], k[1]);
		if (a > b):
			segundo = k[1];
		else:
			segundo = j[1];
		#if (segundo == "Ganzo"):
		#	ganzo += 1;
		if (segundo == "Queso"):
			queso += 1;
		elif (segundo == "Pachec"):
			pachec += 1;
		elif (segundo == "Chavez"):
			chavez += 1;
		#elif (segundo == "Barbachan"):
		#	barbachan += 1;
		elif (segundo == "FAMO"):
			famo += 1;
		elif (segundo == "Diego"):
			diego += 1;
		else:
			chichico += 1; 
	#ganzo = float((ganzo * 100) / lel);			
	queso = float((queso * 100) / lel);
	#barbachan = float((barbachan * 100) / lel);	
	pachec = float((pachec * 100) / lel);
	chavez = float((chavez * 100) / lel);
	famo = float((famo * 100) / lel);
	diego = float((diego * 100) / lel);
	chichico = float((chichico * 100) / lel);
	print "Posibilidades de acabar como subcampeon: ";
	#print "Ganzo: " + str(ganzo) + "%";
	print "Queso: " + str(queso) + "%";
	#print "Barbachan: " + str(barbachan) + "%";
	print "Pachec: " + str(pachec) + "%";
	print "Chavez: " + str(chavez) + "%";
	print "FAMO: " + str(famo) + "%";
	print "Diego: " + str(diego) + "%";
	print "Chichico: " + str(chichico) + "%";

def campeon(n = loopies):
	lel = n;
	barbachan = 0.0;
	queso = 0.0;
	ganzo = 0.0;
	pachec = 0.0;
	chavez = 0.0;
	famo = 0.0;
	diego = 0.0;
	chichico = 0.0;
	for i in range(n):
		puntos1 = segundaFase();
		puntos1.sort();
		puntos1.reverse();
		k = puntos1[1];
		if (k == puntos1[2]): #en caso de que el 2do y el 3ro tengan la misma cantidad
			lel -= 1;
			continue; #de puntos pues gg
		j = puntos1[0];
		a,b = simularNPartidos(j[1], k[1]);
		if (a > b):
			campeon = j[1];
		else:
			campeon = k[1];
		#if (campeon == "Ganzo"):
		#	ganzo += 1;
		if (campeon == "Queso"):
			queso += 1;
		elif (campeon == "Pachec"):
			pachec += 1;
		elif (campeon == "Chavez"):
			chavez += 1;
		#elif (campeon == "Barbachan"):
		#	barbachan += 1;
		elif (campeon == "FAMO"):
			famo += 1;
		elif (campeon == "Diego"):
			diego += 1;
		else:
			chichico += 1; 
	#ganzo = float((ganzo * 100) / lel);			
	queso = float((queso * 100) / lel);
	#barbachan = float((barbachan * 100) / lel);	
	pachec = float((pachec * 100) / lel);
	chavez = float((chavez * 100) / lel);
	famo = float((famo * 100) / lel);
	diego = float((diego * 100) / lel);
	chichico = float((chichico * 100) / lel);
	print "Posibilidades de acabar como campeon: ";
	#print "Ganzo: " + str(ganzo) + "%";
	print "Queso: " + str(queso) + "%";
	#print "Barbachan: " + str(barbachan) + "%";
	print "Pachec: " + str(pachec) + "%";
	print "Chavez: " + str(chavez) + "%";
	print "FAMO: " + str(famo) + "%";
	print "Diego: " + str(diego) + "%";
	print "Chichico: " + str(chichico) + "%";

##############MAIN#####################

sacandoRating();
#novenoPuesto();
#octavoPuesto();
#septimoPuesto();
#pasaRepechaje();
sextoPuesto();
quintoPuesto();
cuartoPuesto();
tercerPuesto();
segundoPuesto();
campeon();
