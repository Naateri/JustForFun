from sim_partidos import simularNPartidosD;
import ratings;

#def fecha1(puntos, ratings):
#	res1, res2 = simularNPartidosD("Bolivia", "Chile", ratings);
#	if (res1 > res2):
#		puntos[5][0] += 3;
#	elif (res1 < res2):
#		puntos[6][0] += 3;
#	else:
#		puntos[5][0] += 1;
#		puntos[6][0] += 1;
#	res1, res2 = simularNPartidosD("Ecuador", "Peru", ratings);
#	if (res1 > res2):
#		puntos[3][0] += 3;
#	elif (res1 < res2):
#		puntos[4][0] += 3;
#	else:
#		puntos[3][0] += 1;
#		puntos[4][0] += 1;
#	res1, res2 = simularNPartidosD("Colombia", "Brasil", ratings);
#	if (res1 > res2):
#		puntos[9][0] += 3;
#	elif (res1 < res2):
#		puntos[2][0] += 3;
#	else:
#		puntos[9][0] += 1;
#		puntos[2][0] += 1;
#	res1, res2 = simularNPartidosD("Argentina", "Venezuela", ratings);
#	if (res1 > res2):
#		puntos[1][0] += 3;
#	elif (res1 < res2):
#		puntos[8][0] += 3;
#	else:
#		puntos[1][0] += 1;
#		puntos[8][0] += 1;
#	res1, res2 = simularNPartidosD("Paraguay", "Uruguay", ratings);
#	if (res1 > res2):
#		puntos[7][0] += 3;
#	elif (res1 < res2):
#		puntos[0][0] += 3;
#	else:
#		puntos[7][0] += 1;
#		puntos[0][0] += 1;
#
def fecha2(puntos, ratings):
	res1, res2 = simularNPartidosD("Bolivia", "Brasil", ratings);
	if (res1 > res2):
		puntos[5][0] += 3;
	elif (res1 < res2):
		puntos[2][0] += 3;
	else:
		puntos[5][0] += 1;
		puntos[2][0] += 1;
	res1, res2 = simularNPartidosD("Argentina", "Peru", ratings);
	if (res1 > res2):
		puntos[1][0] += 3;
	elif (res1 < res2):
		puntos[4][0] += 3;
	else:
		puntos[1][0] += 1;
		puntos[4][0] += 1;
	res1, res2 = simularNPartidosD("Venezuela", "Uruguay", ratings);
	if (res1 > res2):
		puntos[8][0] += 3;
	elif (res1 < res2):
		puntos[0][0] += 3;
	else:
		puntos[0][0] += 1;
		puntos[8][0] += 1;
	res1, res2 = simularNPartidosD("Chile", "Ecuador", ratings);
	if (res1 > res2):
		puntos[6][0] += 3;
	elif (res1 < res2):
		puntos[3][0] += 3;
	else:
		puntos[6][0] += 1;
		puntos[3][0] += 1;
	res1, res2 = simularNPartidosD("Colombia", "Paraguay", ratings);
	if (res1 > res2):
		puntos[9][0] += 3;
	elif (res1 < res2):
		puntos[7][0] += 3;
	else:
		puntos[7][0] += 1;
		puntos[9][0] += 1;

def fecha3(puntos, ratings):
	res1, res2 = simularNPartidosD("Brasil", "Chile", ratings);
	if (res1 > res2):
		puntos[2][0] += 3;
	elif (res1 < res2):
		puntos[6][0] += 3;
	else:
		puntos[2][0] += 1;
		puntos[6][0] += 1;
	res1, res2 = simularNPartidosD("Paraguay", "Venezuela", ratings);
	if (res1 > res2):
		puntos[7][0] += 3;
	elif (res1 < res2):
		puntos[8][0] += 3;
	else:
		puntos[7][0] += 1;
		puntos[8][0] += 1;
	res1, res2 = simularNPartidosD("Uruguay", "Bolivia", ratings);
	if (res1 > res2):
		puntos[0][0] += 3;
	elif (res1 < res2):
		puntos[5][0] += 3;
	else:
		puntos[0][0] += 1;
		puntos[5][0] += 1;
	res1, res2 = simularNPartidosD("Peru", "Colombia", ratings);
	if (res1 > res2):
		puntos[4][0] += 3;
	elif (res1 < res2):
		puntos[9][0] += 3;
	else:
		puntos[4][0] += 1;
		puntos[9][0] += 1;
	res1, res2 = simularNPartidosD("Ecuador", "Argentina", ratings);
	if (res1 > res2):
		puntos[3][0] += 3;
	elif (res1 < res2):
		puntos[1][0] += 3;
	else:
		puntos[3][0] += 1;
		puntos[1][0] += 1;

def simuFechas(ratings):
	puntos = [[74, "Uruguay"], [24, "Argentina"], [37, "Brasil"], [20, "Ecuador"], [24, "Peru"], [13, "Bolivia"], [23, "Chile"], [21, "Paraguay"], [8, "Venezuela"], [26, "Colombia"]];
	#fecha1(puntos, ratings);
	fecha2(puntos, ratings);
	fecha3(puntos, ratings);
	return puntos;

#games = list();
#ratngs = list();
#ratings.guardarPartidos(games);
#ratngs = ratings.sacandoRating(games);

#print ratngs;
