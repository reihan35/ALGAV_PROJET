set terminal postscript eps enhanced
set output "TAS_shaks.eps"
set title "ConstIter" 
set ylabel "Temps d'exécution en seconde"
set xlabel "Taille de liste"
set style data lines
plot "const_shaks.dat" using 1:2 with lines title "tas", "const_shakes.dat" using 1:3 with lines title "file"
set term postscript 
replot
quit
