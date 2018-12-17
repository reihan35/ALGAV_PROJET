set title "Le temps de union pour file" 
set ylabel "Temps d'exécution en seconde"
set xlabel "Taille de liste"
set style data lines
plot "file_union2.dat" using 1:2 with lines title "",
set term postscript 
set output "file_union.pdf"
replot 