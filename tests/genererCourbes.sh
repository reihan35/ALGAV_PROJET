FichierTmp=""
ListeRep="$(find * -type d -prune)"   # liste des repertoires sans leurs sous-repertoires
for Rep in ${ListeRep}; do
    cd ${Rep} && "$(gnuplot *.gnu)"
    cd ..
done
