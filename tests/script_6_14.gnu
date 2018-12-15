set terminal postscript eps enhanced
set output "6_14.eps"
set title "Operations " 
set ylabel "Temps d'exécution en seconde"
set xlabel "Operation"
set xrange[1:4]
set yrange[0:0.2]
set xtics 1
set style line 1 \
    linecolor rgb '#0060ad' \
    linetype 1 linewidth 2 \
    pointtype 7 pointsize 1.5
set style line 2 \
    linecolor rgb '#0060ad' \
    linetype 2 linewidth 3 \
    pointtype 7 pointsize 1.5
plot "const_shak.dat" using 1:2 with linespoints linestyle 1 title "Tas","const_shak.dat" using 1:3 with linespoints linestyle 2 title "File"
set term postscript 
set output "TAS.eps"
replot
quit
