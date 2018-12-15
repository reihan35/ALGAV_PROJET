set title "Le temps de construction d'une file binomiale" 
set ylabel "Temps d'exécution en seconde"
set xlabel "Taille de liste"
set style data lines
plot "file.dat" using 1:2 with lines title "",
set term postscript 
set output "FILE.pdf"
replot 
