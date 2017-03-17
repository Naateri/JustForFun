import csv
import sys
import time
sched = list()
with open("Sched 2017-2.csv", "rU") as f: #importing schedule 
	rows = csv.DictReader(f)
	for r in rows:
		sched.append(r) #saving schedule

monthsDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #dias por mes, empezando en Enero

def askAuto():
	a = raw_input("Se ha detectado la fecha en el ordenador. Desea usar esta fecha? (s/n) ")
	a = a.lower()
	if a == "s":
		return True
	elif a == "n":
		return False
	else:
		print "Ingrese un valor valido."
		askAuto()

def askWeek():
	a = input("Ingrese el numero de la semana que quiera ver: ")
	if a <= 0 or a > 12:
		print "Debe ingresar un numero valido."
		askWeek()
	else:
		return a
def getWeekIfTUE(month, day, week = 0):
	for m8 in sched:
			if int(m8["startsMonth"]) == month and int(m8["startsDay"]) == day:
				week = int(m8["week"])
				break
	if week != 0:
			return week
	else:
		print "Error. Csv no es el de la season actual."
		sys.exit()

def getWeek():
	day = int(time.strftime("%d"))
	dof = int(time.strftime("%w")) #day of week
	month = int(time.strftime("%m"))
	year = int(time.strftime("%y"))
	#week = 0
	if year % 4 == 0: #si es anho bisiesto
		monthsDays[1] = 29 #febrero tiene 29 dias
	if dof == 2: #if it is tuesday
		week = getWeekIfTUE(month, day)	

	elif dof > 2: #if it is wednesday - saturday
		gap = dof - 2
		day -= gap
		if day <= 0:
			if month-2 < 0:
				month = 12
			day += monthsDays[month-1]
	else:
		gap = 2 - dof
		day += gap
		if day >= monthsDays[month-1]:
			if month == 12:
				month = 1
			else:
				month += 1
			day -= monthsDays[month-1] 
	week = getWeekIfTUE(month, day)
	return week

def getEvents(week, maxim):
	if week < 0 or week > 13:
		print "Error. Semana fuera del rango."
		sys.exit()
	else:
		print "Sus eventos para esta semana son: "
		events = sched[week-1]
		curseries = 1
		str_series = "series" + str(curseries)
		while events[str_series] != "-": #or curseries > maxim:
			str_car = "car" + str(curseries)
			str_track = "track" + str(curseries)
			str_laps = "laps-time" + str(curseries)
			str_dttr = "dttr" + str(curseries) #day and time to race
			print "Series: " + events[str_series]
			print "Car: " + events[str_car]
			print "Track: " + events[str_track]
			laps = events[str_laps]
			if len(laps) == 3 and laps[2] == "m":
				laps = "Time: "
			else:
				laps = "Laps: "
			print laps + events[str_laps]
			print "Preferred time to race: " + events[str_dttr]
			print " "
			curseries += 1
			if curseries > maxim:
				break
			else:
				str_series = "series" + str(curseries)

def main():
	print "Fecha de hoy: " + time.strftime("%d/%m")
	if askAuto():
		week = getWeek()
		#print "Estamos en la semana: " + str(week)
	else:
		week = askWeek()
	print "Estamos en la semana: " + str(week)
	getEvents(week, 6)
	while True:
		a = raw_input("Desea continuar? (s)")
		if a.lower() != "s":
			break		
		week = askWeek()
		getEvents(week, 6)
	print "Gracias por usarme. Hasta pronto!"
	sys.exit()

main()
