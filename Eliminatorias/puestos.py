from fechas import simuFechas;

puntos = [[24, "Uruguay"], [23, "Argentina"], [36, "Brasil"], [20, "Ecuador"], [21, "Peru"], [10, "Bolivia"], [23, "Chile"], [21, "Paraguay"], [7, "Venezuela"], [25, "Colombia"]];

loopies = 10000;

def decimoPuesto(ratings, n = loopies):
	brasil = 0.0;
	colombia = 0.0;
	uruguay = 0.0;
	chile = 0.0;
	argentina = 0.0;
	peru = 0.0;
	paraguay = 0.0;
	ecuador = 0.0;
	bolivia = 0.0;
	venezuela = 0.0;
	lel = n;
	for i in range(n):
		puntos1 = simuFechas(ratings);
		puntos1.sort();
		puntos1.reverse();
		if (puntos[8][0] == puntos[9][0]): #9no y 10mo empatados
			lel -= 1;
			continue;
		lal = puntos[9][1];
		if (lal == "Venezuela"):
			venezuela += 1;
		elif (lal == "Bolivia"):
			bolivia += 1;
		elif (lal == "Ecuador"):
			ecuador += 1;
		elif (lal == "Paraguay"):
			paraguay += 1;
		elif (lal == "Peru"):
			peru += 1;
		elif (lal == "Argentina"):
			argentina += 1;
		elif (lal == "Chile"):
			chile += 1;
		elif (lal == "Uruguay"):
			uruguay += 1;
		elif (lal == "Colombia"):
			colombia += 1;
		else:
			brasil += 1;
	brasil = (brasil*100)/lel;
	colombia = (colombia*100)/lel;
	uruguay = (uruguay*100)/lel;
	chile = (chile*100)/lel;
	argentina = (argentina*100)/lel;
	peru = (peru*100)/lel;
	paraguay = (paraguay*100)/lel;
	ecuador = (ecuador*100)/lel;
	bolivia = (bolivia*100)/lel;
	venezuela = (venezuela*100)/lel;
	print "Posibilidades de acabar decimo:";
	print "Brasil: " + str(brasil) + "%";
	print "Colombia: " + str(colombia) + "%";
	print "Uruguay: " + str(uruguay) + "%";
	print "Chile: " + str(chile) + "%";
	print "Argentina: " + str(argentina) + "%";
	print "Peru: " + str(peru) + "%";
	print "Paraguay: " + str(paraguay) + "%";
	print "Ecuador: " + str(ecuador) + "%";
	print "Bolivia: " + str(bolivia) + "%";
	print "Venezuela: " + str(venezuela) + "%";
	
def novenoPuesto(ratings, n = loopies):
	brasil = 0.0;
	colombia = 0.0;
	uruguay = 0.0;
	chile = 0.0;
	argentina = 0.0;
	peru = 0.0;
	paraguay = 0.0;
	ecuador = 0.0;
	bolivia = 0.0;
	venezuela = 0.0;
	lel = n;
	for i in range(n):
		puntos1 = simuFechas(ratings);
		puntos1.sort();
		puntos1.reverse();
		if (puntos[7][0] == puntos[8][0] or puntos[9][0] == puntos[8][0]): #8vo y 9no empatados o 10mo y 9no
			lel -= 1;
			continue;
		lal = puntos[8][1];
		if (lal == "Venezuela"):
			venezuela += 1;
		elif (lal == "Bolivia"):
			bolivia += 1;
		elif (lal == "Ecuador"):
			ecuador += 1;
		elif (lal == "Paraguay"):
			paraguay += 1;
		elif (lal == "Peru"):
			peru += 1;
		elif (lal == "Argentina"):
			argentina += 1;
		elif (lal == "Chile"):
			chile += 1;
		elif (lal == "Uruguay"):
			uruguay += 1;
		elif (lal == "Colombia"):
			colombia += 1;
		else:
			brasil += 1;
	brasil = (brasil*100)/lel;
	colombia = (colombia*100)/lel;
	uruguay = (uruguay*100)/lel;
	chile = (chile*100)/lel;
	argentina = (argentina*100)/lel;
	peru = (peru*100)/lel;
	paraguay = (paraguay*100)/lel;
	ecuador = (ecuador*100)/lel;
	bolivia = (bolivia*100)/lel;
	venezuela = (venezuela*100)/lel;
	print "Posibilidades de acabar noveno:";
	print "Brasil: " + str(brasil) + "%";
	print "Colombia: " + str(colombia) + "%";
	print "Uruguay: " + str(uruguay) + "%";
	print "Chile: " + str(chile) + "%";
	print "Argentina: " + str(argentina) + "%";
	print "Peru: " + str(peru) + "%";
	print "Paraguay: " + str(paraguay) + "%";
	print "Ecuador: " + str(ecuador) + "%";
	print "Bolivia: " + str(bolivia) + "%";
	print "Venezuela: " + str(venezuela) + "%";

def octavoPuesto(ratings, n = loopies):
	brasil = 0.0;
	colombia = 0.0;
	uruguay = 0.0;
	chile = 0.0;
	argentina = 0.0;
	peru = 0.0;
	paraguay = 0.0;
	ecuador = 0.0;
	bolivia = 0.0;
	venezuela = 0.0;
	lel = n;
	for i in range(n):
		puntos1 = simuFechas(ratings);
		puntos1.sort();
		puntos1.reverse();
		if (puntos[7][0] == puntos[8][0] or puntos[6][0] == puntos[7][0]): #8vo y 9no empatados o 7mo y 8vo
			lel -= 1;
			continue;
		lal = puntos[7][1];
		if (lal == "Venezuela"):
			venezuela += 1;
		elif (lal == "Bolivia"):
			bolivia += 1;
		elif (lal == "Ecuador"):
			ecuador += 1;
		elif (lal == "Paraguay"):
			paraguay += 1;
		elif (lal == "Peru"):
			peru += 1;
		elif (lal == "Argentina"):
			argentina += 1;
		elif (lal == "Chile"):
			chile += 1;
		elif (lal == "Uruguay"):
			uruguay += 1;
		elif (lal == "Colombia"):
			colombia += 1;
		else:
			brasil += 1;
	brasil = (brasil*100)/lel;
	colombia = (colombia*100)/lel;
	uruguay = (uruguay*100)/lel;
	chile = (chile*100)/lel;
	argentina = (argentina*100)/lel;
	peru = (peru*100)/lel;
	paraguay = (paraguay*100)/lel;
	ecuador = (ecuador*100)/lel;
	bolivia = (bolivia*100)/lel;
	venezuela = (venezuela*100)/lel;
	print "Posibilidades de acabar octavo:";
	print "Brasil: " + str(brasil) + "%";
	print "Colombia: " + str(colombia) + "%";
	print "Uruguay: " + str(uruguay) + "%";
	print "Chile: " + str(chile) + "%";
	print "Argentina: " + str(argentina) + "%";
	print "Peru: " + str(peru) + "%";
	print "Paraguay: " + str(paraguay) + "%";
	print "Ecuador: " + str(ecuador) + "%";
	print "Bolivia: " + str(bolivia) + "%";
	print "Venezuela: " + str(venezuela) + "%";

def septimoPuesto(ratings, n = loopies):
	brasil = 0.0;
	colombia = 0.0;
	uruguay = 0.0;
	chile = 0.0;
	argentina = 0.0;
	peru = 0.0;
	paraguay = 0.0;
	ecuador = 0.0;
	bolivia = 0.0;
	venezuela = 0.0;
	lel = n;
	for i in range(n):
		puntos1 = simuFechas(ratings);
		puntos1.sort();
		puntos1.reverse();
		if (puntos[5][0] == puntos[6][0] or puntos[6][0] == puntos[7][0]): #6to y 7mo empatados o 7mo y 8vo
			lel -= 1;
			continue;
		lal = puntos[6][1];
		print puntos;
		print "lal: " + lal;
		if (lal == "Venezuela"):
			venezuela += 1;
		elif (lal == "Bolivia"):
			bolivia += 1;
		elif (lal == "Ecuador"):
			ecuador += 1;
		elif (lal == "Paraguay"):
			paraguay += 1;
		elif (lal == "Peru"):
			peru += 1;
		elif (lal == "Argentina"):
			argentina += 1;
		elif (lal == "Chile"):
			chile += 1;
		elif (lal == "Uruguay"):
			uruguay += 1;
		elif (lal == "Colombia"):
			colombia += 1;
		else:
			brasil += 1;
	brasil = (brasil*100)/lel;
	colombia = (colombia*100)/lel;
	uruguay = (uruguay*100)/lel;
	chile = (chile*100)/lel;
	argentina = (argentina*100)/lel;
	peru = (peru*100)/lel;
	paraguay = (paraguay*100)/lel;
	ecuador = (ecuador*100)/lel;
	bolivia = (bolivia*100)/lel;
	venezuela = (venezuela*100)/lel;
	print "Posibilidades de acabar septimo:";
	print "Brasil: " + str(brasil) + "%";
	print "Colombia: " + str(colombia) + "%";
	print "Uruguay: " + str(uruguay) + "%";
	print "Chile: " + str(chile) + "%";
	print "Argentina: " + str(argentina) + "%";
	print "Peru: " + str(peru) + "%";
	print "Paraguay: " + str(paraguay) + "%";
	print "Ecuador: " + str(ecuador) + "%";
	print "Bolivia: " + str(bolivia) + "%";
	print "Venezuela: " + str(venezuela) + "%";

def sextoPuesto(ratings, n = loopies):
	brasil = 0.0;
	colombia = 0.0;
	uruguay = 0.0;
	chile = 0.0;
	argentina = 0.0;
	peru = 0.0;
	paraguay = 0.0;
	ecuador = 0.0;
	bolivia = 0.0;
	venezuela = 0.0;
	lel = n;
	for i in range(n):
		puntos1 = simuFechas(ratings);
		puntos1.sort();
		puntos1.reverse();
		if (puntos[5][0] == puntos[6][0] or puntos[4][0] == puntos[5][0]): #6to y 7mo empatados o 5to y 6to
			lel -= 1;
			continue;
		lal = puntos[5][1];
		if (lal == "Venezuela"):
			venezuela += 1;
		elif (lal == "Bolivia"):
			bolivia += 1;
		elif (lal == "Ecuador"):
			ecuador += 1;
		elif (lal == "Paraguay"):
			paraguay += 1;
		elif (lal == "Peru"):
			peru += 1;
		elif (lal == "Argentina"):
			argentina += 1;
		elif (lal == "Chile"):
			chile += 1;
		elif (lal == "Uruguay"):
			uruguay += 1;
		elif (lal == "Colombia"):
			colombia += 1;
		else:
			brasil += 1;
	brasil = (brasil*100)/lel;
	colombia = (colombia*100)/lel;
	uruguay = (uruguay*100)/lel;
	chile = (chile*100)/lel;
	argentina = (argentina*100)/lel;
	peru = (peru*100)/lel;
	paraguay = (paraguay*100)/lel;
	ecuador = (ecuador*100)/lel;
	bolivia = (bolivia*100)/lel;
	venezuela = (venezuela*100)/lel;
	print "Posibilidades de acabar sexto:";
	print "Brasil: " + str(brasil) + "%";
	print "Colombia: " + str(colombia) + "%";
	print "Uruguay: " + str(uruguay) + "%";
	print "Chile: " + str(chile) + "%";
	print "Argentina: " + str(argentina) + "%";
	print "Peru: " + str(peru) + "%";
	print "Paraguay: " + str(paraguay) + "%";
	print "Ecuador: " + str(ecuador) + "%";
	print "Bolivia: " + str(bolivia) + "%";
	print "Venezuela: " + str(venezuela) + "%";

def quintoPuesto(ratings, n = loopies):
	brasil = 0.0;
	colombia = 0.0;
	uruguay = 0.0;
	chile = 0.0;
	argentina = 0.0;
	peru = 0.0;
	paraguay = 0.0;
	ecuador = 0.0;
	bolivia = 0.0;
	venezuela = 0.0;
	lel = n;
	for i in range(n):
		puntos1 = simuFechas(ratings);
		puntos1.sort();
		puntos1.reverse();
		if (puntos[3][0] == puntos[4][0] or puntos[4][0] == puntos[5][0]): #4to y 5to empatados o 5to y 6to
			lel -= 1;
			continue;
		print puntos1;
		lal = puntos[4][1];
		if (lal == "Venezuela"):
			venezuela += 1;
		elif (lal == "Bolivia"):
			bolivia += 1;
		elif (lal == "Ecuador"):
			ecuador += 1;
		elif (lal == "Paraguay"):
			paraguay += 1;
		elif (lal == "Peru"):
			peru += 1;
		elif (lal == "Argentina"):
			argentina += 1;
		elif (lal == "Chile"):
			chile += 1;
		elif (lal == "Uruguay"):
			uruguay += 1;
		elif (lal == "Colombia"):
			colombia += 1;
		else:
			brasil += 1;
	brasil = (brasil*100)/lel;
	colombia = (colombia*100)/lel;
	uruguay = (uruguay*100)/lel;
	chile = (chile*100)/lel;
	argentina = (argentina*100)/lel;
	peru = (peru*100)/lel;
	paraguay = (paraguay*100)/lel;
	ecuador = (ecuador*100)/lel;
	bolivia = (bolivia*100)/lel;
	venezuela = (venezuela*100)/lel;
	print "Posibilidades de acabar quinto:";
	print "Brasil: " + str(brasil) + "%";
	print "Colombia: " + str(colombia) + "%";
	print "Uruguay: " + str(uruguay) + "%";
	print "Chile: " + str(chile) + "%";
	print "Argentina: " + str(argentina) + "%";
	print "Peru: " + str(peru) + "%";
	print "Paraguay: " + str(paraguay) + "%";
	print "Ecuador: " + str(ecuador) + "%";
	print "Bolivia: " + str(bolivia) + "%";
	print "Venezuela: " + str(venezuela) + "%";

def cuartoPuesto(ratings, n = loopies):
	brasil = 0.0;
	colombia = 0.0;
	uruguay = 0.0;
	chile = 0.0;
	argentina = 0.0;
	peru = 0.0;
	paraguay = 0.0;
	ecuador = 0.0;
	bolivia = 0.0;
	venezuela = 0.0;
	lel = n;
	for i in range(n):
		puntos1 = simuFechas(ratings);
		puntos1.sort();
		puntos1.reverse();
		if (puntos[3][0] == puntos[4][0] or puntos[2][0] == puntos[3][0]): #4to y 5to empatados o 3ro y 4to
			lel -= 1;
			continue;
		lal = puntos[3][1];
		if (lal == "Venezuela"):
			venezuela += 1;
		elif (lal == "Bolivia"):
			bolivia += 1;
		elif (lal == "Ecuador"):
			ecuador += 1;
		elif (lal == "Paraguay"):
			paraguay += 1;
		elif (lal == "Peru"):
			peru += 1;
		elif (lal == "Argentina"):
			argentina += 1;
		elif (lal == "Chile"):
			chile += 1;
		elif (lal == "Uruguay"):
			uruguay += 1;
		elif (lal == "Colombia"):
			colombia += 1;
		else:
			brasil += 1;
	brasil = (brasil*100)/lel;
	colombia = (colombia*100)/lel;
	uruguay = (uruguay*100)/lel;
	chile = (chile*100)/lel;
	argentina = (argentina*100)/lel;
	peru = (peru*100)/lel;
	paraguay = (paraguay*100)/lel;
	ecuador = (ecuador*100)/lel;
	bolivia = (bolivia*100)/lel;
	venezuela = (venezuela*100)/lel;
	print "Posibilidades de acabar cuarto:";
	print "Brasil: " + str(brasil) + "%";
	print "Colombia: " + str(colombia) + "%";
	print "Uruguay: " + str(uruguay) + "%";
	print "Chile: " + str(chile) + "%";
	print "Argentina: " + str(argentina) + "%";
	print "Peru: " + str(peru) + "%";
	print "Paraguay: " + str(paraguay) + "%";
	print "Ecuador: " + str(ecuador) + "%";
	print "Bolivia: " + str(bolivia) + "%";

def tercerPuesto(ratings, n = loopies):
	brasil = 0.0;
	colombia = 0.0;
	uruguay = 0.0;
	chile = 0.0;
	argentina = 0.0;
	peru = 0.0;
	paraguay = 0.0;
	ecuador = 0.0;
	bolivia = 0.0;
	venezuela = 0.0;
	lel = n;
	for i in range(n):
		puntos1 = simuFechas(ratings);
		puntos1.sort();
		puntos1.reverse();
		if (puntos[1][0] == puntos[2][0] or puntos[2][0] == puntos[3][0]): #2do y 3ro empatados o 3ro y 4to
			lel -= 1;
			continue;
		lal = puntos[2][1];
		if (lal == "Venezuela"):
			venezuela += 1;
		elif (lal == "Bolivia"):
			bolivia += 1;
		elif (lal == "Ecuador"):
			ecuador += 1;
		elif (lal == "Paraguay"):
			paraguay += 1;
		elif (lal == "Peru"):
			peru += 1;
		elif (lal == "Argentina"):
			argentina += 1;
		elif (lal == "Chile"):
			chile += 1;
		elif (lal == "Uruguay"):
			uruguay += 1;
		elif (lal == "Colombia"):
			colombia += 1;
		else:
			brasil += 1;
	brasil = (brasil*100)/lel;
	colombia = (colombia*100)/lel;
	uruguay = (uruguay*100)/lel;
	chile = (chile*100)/lel;
	argentina = (argentina*100)/lel;
	peru = (peru*100)/lel;
	paraguay = (paraguay*100)/lel;
	ecuador = (ecuador*100)/lel;
	bolivia = (bolivia*100)/lel;
	venezuela = (venezuela*100)/lel;
	print "Posibilidades de acabar tercero:";
	print "Brasil: " + str(brasil) + "%";
	print "Colombia: " + str(colombia) + "%";
	print "Uruguay: " + str(uruguay) + "%";
	print "Chile: " + str(chile) + "%";
	print "Argentina: " + str(argentina) + "%";
	print "Peru: " + str(peru) + "%";
	print "Paraguay: " + str(paraguay) + "%";
	print "Ecuador: " + str(ecuador) + "%";
	print "Bolivia: " + str(bolivia) + "%";

def segundoPuesto(ratings, n = loopies):
	brasil = 0.0;
	colombia = 0.0;
	uruguay = 0.0;
	chile = 0.0;
	argentina = 0.0;
	peru = 0.0;
	paraguay = 0.0;
	ecuador = 0.0;
	bolivia = 0.0;
	venezuela = 0.0;
	lel = n;
	for i in range(n):
		puntos1 = simuFechas(ratings);
		puntos1.sort();
		puntos1.reverse();
		if (puntos[1][0] == puntos[2][0] or puntos[0][0] == puntos[1][0]): #2do y 3ro empatados o 1ro y 2do
			lel -= 1;
			continue;
		lal = puntos[1][1];
		if (lal == "Venezuela"):
			venezuela += 1;
		elif (lal == "Bolivia"):
			bolivia += 1;
		elif (lal == "Ecuador"):
			ecuador += 1;
		elif (lal == "Paraguay"):
			paraguay += 1;
		elif (lal == "Peru"):
			peru += 1;
		elif (lal == "Argentina"):
			argentina += 1;
		elif (lal == "Chile"):
			chile += 1;
		elif (lal == "Uruguay"):
			uruguay += 1;
		elif (lal == "Colombia"):
			colombia += 1;
		else:
			brasil += 1;
	brasil = (brasil*100)/lel;
	colombia = (colombia*100)/lel;
	uruguay = (uruguay*100)/lel;
	chile = (chile*100)/lel;
	argentina = (argentina*100)/lel;
	peru = (peru*100)/lel;
	paraguay = (paraguay*100)/lel;
	ecuador = (ecuador*100)/lel;
	bolivia = (bolivia*100)/lel;
	venezuela = (venezuela*100)/lel;
	print "Posibilidades de acabar segundo:";
	print "Brasil: " + str(brasil) + "%";
	print "Colombia: " + str(colombia) + "%";
	print "Uruguay: " + str(uruguay) + "%";
	print "Chile: " + str(chile) + "%";
	print "Argentina: " + str(argentina) + "%";
	print "Peru: " + str(peru) + "%";
	print "Paraguay: " + str(paraguay) + "%";
	print "Ecuador: " + str(ecuador) + "%";
	print "Bolivia: " + str(bolivia) + "%";

def primerPuesto(ratings, n = loopies):
	brasil = 0.0;
	colombia = 0.0;
	uruguay = 0.0;
	chile = 0.0;
	argentina = 0.0;
	peru = 0.0;
	paraguay = 0.0;
	ecuador = 0.0;
	bolivia = 0.0;
	venezuela = 0.0;
	lel = n;
	for i in range(n):
		puntos1 = [];
		puntos1 = simuFechas(ratings);
		puntos1.sort();
		puntos1.reverse();
		if (puntos[0][0] == puntos[1][0]): #1ro y 2do
			lel -= 1;
			continue;
		lal = puntos[0][1];
		if (lal == "Venezuela"):
			venezuela += 1;
		elif (lal == "Bolivia"):
			bolivia += 1;
		elif (lal == "Ecuador"):
			ecuador += 1;
		elif (lal == "Paraguay"):
			paraguay += 1;
		elif (lal == "Peru"):
			peru += 1;
		elif (lal == "Argentina"):
			argentina += 1;
		elif (lal == "Chile"):
			chile += 1;
		elif (lal == "Uruguay"):
			uruguay += 1;
		elif (lal == "Colombia"):
			colombia += 1;
		else:
			brasil += 1;
	brasil = (brasil*100)/lel;
	colombia = (colombia*100)/lel;
	uruguay = (uruguay*100)/lel;
	chile = (chile*100)/lel;
	argentina = (argentina*100)/lel;
	peru = (peru*100)/lel;
	paraguay = (paraguay*100)/lel;
	ecuador = (ecuador*100)/lel;
	bolivia = (bolivia*100)/lel;
	venezuela = (venezuela*100)/lel;
	print "Posibilidades de acabar primero:";
	print "Brasil: " + str(brasil) + "%";
	print "Colombia: " + str(colombia) + "%";
	print "Uruguay: " + str(uruguay) + "%";
	print "Chile: " + str(chile) + "%";
	print "Argentina: " + str(argentina) + "%";
	print "Peru: " + str(peru) + "%";
	print "Paraguay: " + str(paraguay) + "%";
	print "Ecuador: " + str(ecuador) + "%";
	print "Bolivia: " + str(bolivia) + "%";
