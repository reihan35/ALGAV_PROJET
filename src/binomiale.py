#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 14:18:43 2018

@author: 3535008
"""
import time
from collections import deque

import copy

#une file binomiale est juste une liste (on utilisera un deque) de tournois

class Tournoi:
                    
    #Cree un tournoi de taille 1 (reduit à 1 noeud)
    def __init__(self, cle):
        self.cle = cle
        #Les fils de la racine d'un tournoi sont des tournois
        self.fils = deque()
    

def afficherT(T, e):
    print(e + "cle : " + str(T.cle))
    afficherF(T.fils, e + "\t")

def afficherF(F, e):
    for t in F:
        print (e + "Tournoi " + str(Degre(t)))
        afficherT(t, e)
    
#retourne le degre du tournoi donne en parametre
def Degre(T):
    return len(T.fils)   
    
def EstVideTournoi(T):
    return T == None

#fait l'union de deux tournois de meme taille
def Union2Tid(T1, T2):
    if T1.cle < T2.cle:
        T1.fils.append(T2)
        return T1
    else:
        T2.fils.append(T1)
        return T2

#renvoie la liste des fils d'un tournoi (qui est une liste de tournois ==> file binomiale)
def Decapite(T):
    return T.fils

#cree une file binomiale reduite au tournoi binomial T
def File(T):
    f = deque()
    f.append(T)
    return f


a = Tournoi(1)
b = File(a)
#print (b)

def EstVideFile(F):
    #l'operation commentee n'est pas en tps constant
    #return F == deque()
    return len(F) == 0

#On suppose qu'on maintient un ordre sur les tournois dans la file
def MinDeg(F):
    return F[0]

def Reste(F):
    F.popleft()
    return F

def AjoutMin(T, F):
    F.appendleft(T)
    return F

def UnionFile (F1 , F2):
    """ FileB ∗ FileB − > FileB
    Renvoie la file binomiale union des deux files F1 et F2."""
    return UFret(F1 , F2 , None)

#Le nombre d'appels récursifs est clairement logarithmique: cela a été testé sur les instances.
#cependant, la duree d'execution de chaque appel augmente lineairement
        
def UFret(F1 , F2 , T):
    """ FileB ∗ FileB ∗ TournoiB − > FileB
    Renvoie la file binomiale union de deux files et d’un tournoi ."""
    

    if EstVideTournoi (T): #pas de tournoi en retenue


        if EstVideFile (F1 ):
            return F2
        if EstVideFile (F2 ):
            return F1
        T1 = MinDeg (F1)
        T2 = MinDeg (F2)
        if Degre (T1) < Degre (T2 ):
            return AjoutMin (T1 , UnionFile ( Reste (F1), F2 ))
        if Degre (T2) < Degre (T1 ):
            return AjoutMin (T2 , UnionFile ( Reste (F2), F1 ))
        if Degre (T1) == Degre (T2 ):
            return UFret ( Reste (F1), Reste (F2), Union2Tid (T1 ,T2 ))

    else:
        #T tournoi en retenue
        if EstVideFile (F1 ):
            return UnionFile (File(T), F2)
        if EstVideFile (F2 ):
            return UnionFile (File(T), F1)
        T1 = MinDeg (F1)
        T2 = MinDeg (F2)
        if Degre (T) < Degre (T1) and Degre (T) < Degre (T2 ):
            return AjoutMin (T, UnionFile (F1 , F2 ))
        if Degre (T) == Degre (T1) and Degre (T) == Degre (T2 ):
            return AjoutMin (T, UFret ( Reste (F1), Reste (F2), Union2Tid (T1 , T2 )))
        if Degre (T) == Degre (T1) and Degre (T) < Degre (T2 ):
            return UFret ( Reste (F1), F2 , Union2Tid (T1 , T))
        if Degre (T) == Degre (T2) and Degre (T) < Degre (T1 ):
            return UFret ( Reste (F2), F1 , Union2Tid (T2 , T))
        
def Ajout(F, elem):
    return UnionFile(F, File(Tournoi(elem)))

def ConsIter(l):
    F = deque()
    for elem in l:
        F = Ajout(F, elem)
        #print "j'ai ajoute " + str(elem)
        #print (Degre(F[0]))
        #print (F)

    return F

def SupprMin(F):
    cmin = F[0].cle
    bmin = F[0]
    for i in range (0, len(F)):
        if F[i].cle < cmin:
            cmin = F[i].cle
            bmin = F[i]
    fils = Decapite(bmin)
    F.remove(bmin)
    F = UnionFile(F, fils)
    return F

f = ConsIter([1, 2, 3, 4, 5, 6])

f = SupprMin(f)
print (f)
print (Degre(f[0]))
print(Degre(f[1]))
afficherF(f, "")



def parse_file (fic):    
    parsed = []
    fic1=open(fic,'r')
    for line in fic1:
        parsed.append(int(line, 16))
    return parsed


l1=['../cles_alea/jeu_1_nb_cles_100.txt','../cles_alea/jeu_2_nb_cles_100.txt','../cles_alea/jeu_3_nb_cles_100.txt','../cles_alea/jeu_4_nb_cles_100.txt','../cles_alea/jeu_5_nb_cles_100.txt']

l2=['../cles_alea/jeu_1_nb_cles_200.txt','../cles_alea/jeu_2_nb_cles_200.txt','../cles_alea/jeu_3_nb_cles_200.txt','../cles_alea/jeu_4_nb_cles_200.txt','../cles_alea/jeu_5_nb_cles_200.txt']

l3=['../cles_alea/jeu_1_nb_cles_500.txt','../cles_alea/jeu_2_nb_cles_500.txt','../cles_alea/jeu_3_nb_cles_500.txt','../cles_alea/jeu_4_nb_cles_500.txt','../cles_alea/jeu_5_nb_cles_500.txt']

l4=['../cles_alea/jeu_1_nb_cles_1000.txt','../cles_alea/jeu_2_nb_cles_1000.txt','../cles_alea/jeu_3_nb_cles_1000.txt','../cles_alea/jeu_4_nb_cles_1000.txt','../cles_alea/jeu_5_nb_cles_1000.txt']


l5=['../cles_alea/jeu_1_nb_cles_5000.txt','../cles_alea/jeu_2_nb_cles_5000.txt','../cles_alea/jeu_3_nb_cles_5000.txt','../cles_alea/jeu_4_nb_cles_5000.txt','../cles_alea/jeu_5_nb_cles_5000.txt']

l6=['../cles_alea/jeu_1_nb_cles_10000.txt','../cles_alea/jeu_2_nb_cles_10000.txt','../cles_alea/jeu_3_nb_cles_10000.txt','../cles_alea/jeu_4_nb_cles_10000.txt','../cles_alea/jeu_5_nb_cles_10000.txt']

l7=['../cles_alea/jeu_1_nb_cles_20000.txt','../cles_alea/jeu_2_nb_cles_20000.txt','../cles_alea/jeu_3_nb_cles_20000.txt','../cles_alea/jeu_4_nb_cles_20000.txt','../cles_alea/jeu_5_nb_cles_20000.txt']

l8=['../cles_alea/jeu_1_nb_cles_50000.txt','../cles_alea/jeu_2_nb_cles_50000.txt','../cles_alea/jeu_3_nb_cles_50000.txt','../cles_alea/jeu_4_nb_cles_50000.txt','../cles_alea/jeu_5_nb_cles_50000.txt']

lt = [l1,l2,l3,l4,l5,l6,l7,l8]

"""
t_m = 0
cpt = 1

for l in lt:
    for i in l:
        start_time = time.time()
        ConsIter(parse_file(i))
        t_m = t_m + (time.time() - start_time)
    file = open("file_const" + str(cpt) + ".txt","w") 
    file.write(str(t_m/5))
    file.close
    cpt = cpt + 1
"""

file = open("../tests/file_constIter/file_const.dat","w") 

absc = [100, 200, 500, 1000, 5000, 10000, 20000, 50000]

g = []
j = 0
for l in lt:
    t_m = 0
    z = []
    for i in l:
        start_time = time.time()
        z.append(ConsIter(parse_file(i)))
        t_m = t_m + (time.time() - start_time)
    g.append(z)    
    file.write(str(absc[j]) + ", " + str(t_m/5) + "\n")
    j+=1

file.close()

file = open("../tests/file_union/file_union.dat","w") 





j = 0
for x in g:
    t_m_1 = 0
    for i in range(0, 5):
        y = copy.deepcopy(x[i])
        z = copy.deepcopy(x[(i+1)%5])
        start_time = time.time()
        UnionFile(y,z)
        t_m_1 = t_m_1 + (time.time() - start_time)
    print ("la " + str(t_m_1/5))
    file.write(str(2*absc[j]) + ", " + str(t_m_1/5) + "\n")
    j += 1
file.close()





