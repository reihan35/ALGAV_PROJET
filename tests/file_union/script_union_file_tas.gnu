set terminal postscript eps enhanced
set output "file_union_2.eps"
set title "Le temps d'exécution d'union" 
set ylabel "Temps d'exécution en seconde"
set xlabel "Taille de liste"
set style data lines
plot "../union_tas/tas_union.dat" using 1:2 with lines title "tas", "file_union.dat" using 1:2 with lines title "file"
