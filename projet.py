#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 11:06:30 2018

@author: 3522144
"""

import math

#parser un fichier de clef
def parse_file (fic):    
    parsed = []
    fic1=open(fic,'r')
    for line in fic1:
        parsed.append(int(line, 16))
    return parsed
        
#q1.1
def inf(c1, c2):
    return c1 < c2

#q1.2
def eg (c1, c2):
    return c1 == c2


def supprmin(tas):
    tas[0] = tas[len(tas-1)]
    del tas[len(tas-1)]
    percolateDown(0, tas);
    
def ajout(tas,elem):
    tas.append(elem)
    i=len(tas)-1
    percolateUp(i, tas)

def switch(a, b, tas):
    tmp = tas[a]
    tas[a] = tas[b]
    tas[b] = tmp
    
def percolateUp(i, tas):
    while((i-1)/2 >= 0 and tas[(i-1)/2]>tas[i]):
        switch(i, (i-1)/2, tas)
        i=(i-1)/2

def percolateDown(pere, tas):
    while 2*pere+1 < len(tas):
        #recuperer le fils minimum
        f_g = 2*pere+1
        
        f_d = 2*pere+2

        f_min = 0
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
    
int(2.6)
def ConsIter(l):
    tas = list(l)
    n = len(l)
    h = int(math.log(n, 2)) - 1
    i = int(pow(2, h)-1)
    nxt_lvl = 2*i+1
    cpt = 0
    while h >= 0:
        print(h)
        #parcours d'un niveau
        while (i < nxt_lvl):
            cpt = percolateDown(i, tas)
            i = i+1
        h = h - 1
        i = int(pow(2, h)-1)
        nxt_lvl = 2*i+1
    print (cpt)
    return tas

print (ConsIter([9, 8, 7, 6, 5, 4, 3]))

