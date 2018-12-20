set terminal postscript eps enhanced
set title "Le temps d'exécution d'union pour tas"
set output "tas_union_arbre.eps" 
set ylabel "Temps d'exécution en seconde"
set xlabel "Taille de liste"
set style data lines
plot "tas_tab_union.dat" using 1:2 with lines title "tableau", "tas_tree_union.dat" using 1:2 with lines title "arbre"
