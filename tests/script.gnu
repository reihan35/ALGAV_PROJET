set terminal postscript eps enhanced
set output "TAS.eps"
set title "Le temps de construction d'un tas" 
set ylabel "Temps d'exécution en seconde"
set xlabel "Taille de liste"
set style data lines
plot "tas.dat" using 1:2 with lines title "tas", "tas.dat" using 1:3 with lines title "arbre"
set term postscript 
set output "TAS.pdf"
replot
quit

plot "const_shak.dat" using 1:2 with points title "tas", "const_shak.dat" using 1:3 with lines title "file"
