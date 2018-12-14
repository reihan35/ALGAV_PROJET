#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 11:06:30 2018

@author: 3522144
"""

import math
import time

#parser un fichier de clef
def parse_file (fic):    
    parsed = []
    fic1=open(fic,'r')
    for line in fic1:
        parsed.append(int(line, 16))
    return parsed

#Pas besoin de traitement differentiel pour les grands entiers en python
#q1.1
def inf(c1, c2):
    return c1 < c2

#q1.2
def eg (c1, c2):
    return c1 == c2

#on enleve la racine et on reinsere le dernier element p
def supprmin(tas):
    tas[0] = tas[len(tas-1)]
    del tas[len(tas-1)]
    percolateDown(0, tas);
    
#on ajoute en fin et on fait remonter l'element pour conserver l'integrite du tas
def ajout(tas,elem):
    tas.append(elem)
    i=len(tas)-1
    percolateUp(i, tas)

#echange deux elements du tableau
def switch(a, b, tas):
    tmp = tas[a]
    tas[a] = tas[b]
    tas[b] = tmp
    
#fait remonter un pere(reajustement a l'insertion)
def percolateUp(i, tas):
    #on fait remonter le noeud tant qu'il est inferieur a son pere
    while((i-1)/2 >= 0 and tas[(i-1)/2]>tas[i]):
        switch(i, (i-1)/2, tas)
        i=(i-1)/2

#Fait descendre un pere (reajustement a la construction ou a la suppression)
def percolateDown(pere, tas):
    #si la condition n'est pas verifiee, le noeud est une feuille et on peut s'arreter
    while 2*pere+1 < len(tas):
        #recuperer le fils minimum
        f_g = 2*pere+1
        
        f_d = 2*pere+2

        f_min = 0
        #attention a ne pas faire de depassement d'indice
        if f_d >= len(tas):
            f_min = tas [f_g]     
        else:
            f_min = min(tas[f_g], tas[f_d])
        if(tas[pere] <  f_min):
            break
        
        #on fait descendre le pere a gauche
        if f_d >= len(tas) or tas[f_g] < tas[f_d]:
            switch(f_g, pere, tas)
            pere = f_g
        #a droite
        else:
            switch(f_d, pere, tas)
            pere = f_d

#cf. rapport pour analyse de complexite
def ConsIter(l):
    tas = list(l)
    n = len(l)
    h = int(math.log(n, 2)) - 1
    i = int(pow(2, h)-1)
    nxt_lvl = 2*i+1
    while h >= 0:
        #parcours d'un niveau
        while (i < nxt_lvl):
            percolateDown(i, tas)
            i = i+1
        h = h - 1
        i = int(pow(2, h)-1)
        nxt_lvl = 2*i+1
    #print (cpt)
    return tas

def Union(t1, t2):
    return ConsIter(t1+t2)

l1=['cles_alea/jeu_1_nb_cles_100.txt','cles_alea/jeu_2_nb_cles_100.txt','cles_alea/jeu_3_nb_cles_100.txt','cles_alea/jeu_4_nb_cles_100.txt','cles_alea/jeu_5_nb_cles_100.txt']

l2=['cles_alea/jeu_1_nb_cles_200.txt','cles_alea/jeu_2_nb_cles_200.txt','cles_alea/jeu_3_nb_cles_200.txt','cles_alea/jeu_4_nb_cles_200.txt','cles_alea/jeu_5_nb_cles_200.txt']

l3=['cles_alea/jeu_1_nb_cles_500.txt','cles_alea/jeu_2_nb_cles_500.txt','cles_alea/jeu_3_nb_cles_500.txt','cles_alea/jeu_4_nb_cles_500.txt','cles_alea/jeu_5_nb_cles_500.txt']

l4=['cles_alea/jeu_1_nb_cles_1000.txt','cles_alea/jeu_2_nb_cles_1000.txt','cles_alea/jeu_3_nb_cles_1000.txt','cles_alea/jeu_4_nb_cles_1000.txt','cles_alea/jeu_5_nb_cles_1000.txt']


l5=['cles_alea/jeu_1_nb_cles_5000.txt','cles_alea/jeu_2_nb_cles_5000.txt','cles_alea/jeu_3_nb_cles_5000.txt','cles_alea/jeu_4_nb_cles_5000.txt','cles_alea/jeu_5_nb_cles_5000.txt']

l6=['cles_alea/jeu_1_nb_cles_10000.txt','cles_alea/jeu_2_nb_cles_10000.txt','cles_alea/jeu_3_nb_cles_10000.txt','cles_alea/jeu_4_nb_cles_10000.txt','cles_alea/jeu_5_nb_cles_10000.txt']

l7=['cles_alea/jeu_1_nb_cles_20000.txt','cles_alea/jeu_2_nb_cles_20000.txt','cles_alea/jeu_3_nb_cles_20000.txt','cles_alea/jeu_4_nb_cles_20000.txt','cles_alea/jeu_5_nb_cles_20000.txt']

l8=['cles_alea/jeu_1_nb_cles_50000.txt','cles_alea/jeu_2_nb_cles_50000.txt','cles_alea/jeu_3_nb_cles_50000.txt','cles_alea/jeu_4_nb_cles_50000.txt','cles_alea/jeu_5_nb_cles_50000.txt']

lt = [l1,l2,l3,l4,l5,l6,l7,l8]

t_m = 0
cpt = 1

for l in lt:
	for i in l:
		start_time = time.time()
		ConsIter(parse_file(i))
		t_m = t_m + (time.time() - start_time)
	file = open("tas_tab" + str(cpt) + ".txt","w") 
	file.write(str(t_m/5))
	file.close
	cpt = cpt + 1

