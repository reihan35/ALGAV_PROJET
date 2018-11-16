#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 14:18:43 2018

@author: 3535008
"""
from collections import deque
#une file binomiale est juste une liste (on utilisera un deque) de tournois

class Tournoi:
                    
    #Cree un tournoi de taille 1 (reduit à 1 noeud)
    def __init__(self, cle):
        self.cle = cle
        #Les fils de la racine d'un tournoi sont des tournois
        self.fils = []
    
def Degre(T):
    return len(T.fils)
    
    
    
def EstVideTournoi(T):
    return T == None

def Union2Tid(T1, T2):
    if T1.cle < T2.cle:
        T1.fils.append(T2)
        return T1
    else:
        T2.fils.append(T1)
        return T2

def Decapite(T):
    return T.fils

def File(T):
    f = deque()
    f.append(T)
    return f

a = Tournoi(1)
b = File(a)
print (b)

def EstVideFile(F):
    return F == deque()

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

def UFret(F1 , F2 , T):
    """ FileB ∗ FileB ∗ TournoiB − > FileB
    Renvoie la file binomiale union de deux files et d’un tournoi ."""
    if EstVideTournoi (T): #pas de tournoi en retenue
        if EstVideFile (F1 ):
            print("aa")
            return F2
        if EstVideFile (F2 ):
            print("bb")
            return F1
        T1 = MinDeg (F1)
        T2 = MinDeg (F2)
        if Degre (T1) < Degre (T2 ):
            print("cc")
            return AjoutMin (T1 , UnionFile ( Reste (F1), F2 ))
        if Degre (T2) < Degre (T1 ):
            print("dd")
            return AjoutMin (T2 , UnionFile ( Reste (F2), F1 ))
        if Degre (T1) == Degre (T2 ):
            print("ee")
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
        print (F)

    return F

def SupprMin(F):
    cmin = F[0].cle
    for i in range (0, len(F)):
        if F[i].cle < cmin:
            cmin = F[i].cle
    F.remove(cmin)

f = ConsIter([1, 2, 3, 4, 5, 6])
print (Degre(f[0]))
print(Degre(f[1]))