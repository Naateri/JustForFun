from random import random;
from ratings import getIndex;

def simularPartido(jug1, jug2, ratings): #basado en probabilidades (ratings)
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

def simularNPartidosD(jug1, jug2, ratings, n = 70): #Simulando partidos empate incluido
	ganaJug1 = 0;
	ganaJug2 = 0;
	for i in range(n):
		resultado = simularPartido(jug1, jug2, ratings);
		if (resultado == jug1):
			ganaJug1 += 1;
		else:
			ganaJug2 += 1;
	return ganaJug1, ganaJug2;

