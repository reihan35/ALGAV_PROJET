set title "Le temps de union pour tas avce tableau" 
set terminal postscript eps enhanced
set ylabel "Temps d'exécution en seconde"
set xlabel "Taille de liste"
set style data lines
plot "tas_tab_union.dat" using 1:2 with lines title "",
set term postscript 
set output "tas_union_tab.eps"
replot 
