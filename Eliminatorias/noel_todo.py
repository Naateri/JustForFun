import ratings;
import puestos;

games = list();
ratings.guardarPartidos(games);
ratings = ratings.sacandoRating(games);

print ratings;

#puestos.decimoPuesto(ratings);
#puestos.novenoPuesto(ratings);
#puestos.octavoPuesto(ratings);
puestos.septimoPuesto(ratings);
#puestos.sextoPuesto(ratings);
#puestos.quintoPuesto(ratings);
#puestos.cuartoPuesto(ratings);
#puestos.tercerPuesto(ratings);
#puestos.segundoPuesto(ratings);
#puestos.primerPuesto(ratings);

