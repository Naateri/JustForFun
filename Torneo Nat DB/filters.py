### File for filtering
### Only filtering related stuff here
### Copyright Nateri (C) 2017 because swag
### Most cringy opening to a file since 1969

def wannafilter():
	a = raw_input("Desea filtrar por algun criterio? (por mostrarse) (s/n) ")
	a = a.lower()
	if a == "s":
		return True
	elif a == 'n':
		return False
	else:
		wannafilter()

def filterMenu():
	print "1. Por torneos"
	print "2. #SOON"
	print "3. Seguir"
	a = input("Ingrese el numero segun lo que desee filtrar: ")
	if a == 1:
		return 't'
	elif a == 2:
		filterMenu()
	elif a == 3:
		return True
	else: 
		filterMenu()

######################## TORNEOS ####################################

def getTorneos(games): #games = list
	torns = list()
	i = 1
	for game in games:
		if game["torneo"] not in torns:
			torns.append(game["torneo"])
	#print torns
	for torny in torns:
		print str(i) + ". " + torny
		i += 1
	return torns

def filterByMultTorneos():
	a = raw_input("Quiere agregar torneos? (s/n) ")
	a = a.lower()
	if a == 's':
		return True
	elif a == 'n':
		return False
	else:
		filterbyMultTorneos()
	
def lookTorneo(games, torny):
	final = list()		
	for game in games:
		if game["torneo"] == torny:
			final.append(game)
	return final
	
def filterByTorneos(games):
	final = list()	
	torns = getTorneos(games)
	counter = 1 #to see if all tornies have been selected
	fil = True
	while fil:# or counter == len(torns):
		a = input("Ingrese el numero del torneo que quiera incluir: ")
		#final.append(torns[a-1])
		temp = lookTorneo(games, torns[a-1]) #new list with that torny
		counter += 1
		final = final + temp #concatenating both lists
		if counter < len(torns): 
			fil = filterByMultTorneos()
		else:
			fil = False
	return final
	
#########################################################################

