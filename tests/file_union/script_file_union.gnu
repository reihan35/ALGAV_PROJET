set terminal postscript eps enhanced
set output "file_union.eps"
set title "Le temps d'exécution d'union pour une file binomiale" 
set ylabel "Temps d'exécution en seconde"
set xlabel "Taille de liste"
set style data lines
plot "file_union.dat" using 1:2 with lines title "",
