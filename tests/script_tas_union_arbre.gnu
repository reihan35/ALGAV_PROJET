set terminal postscript eps enhanced
set title "Le temps de union pour tas avce Arbre" 
set ylabel "Temps d'exécution en seconde"
set xlabel "Taille de liste"
set style data lines
plot "tas_union_arbre.dat" using 1:2 with lines title "",
set term postscript 
set output "tas_union_arbre.eps"
replot 
