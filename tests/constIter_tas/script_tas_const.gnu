set terminal postscript eps enhanced
set output "tas_const.eps"
set title "Le temps de construction d'un tas" 
set ylabel "Temps d'exécution en seconde"
set xlabel "Taille de liste"
set style data lines
plot "tas_const.dat" using 1:2 with lines title "tableau", "tas_const.dat" using 1:3 with lines title "arbre"
