#Temps reel
set output "TAS.pdf"
set title "Le temps de construction d'un tas" 
set ylabel "Temps d'exécution en seconde"
set xlabel "Taille de liste"
set style data lines
plot "100.dat" using 1:2 with lines title "tas", "100.dat" using 1:3 with lines title "arbre"
set term postscript 
set output "TAS.pdf"
replot 
