#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 10:52:41 2018

@author: 3535008
"""
import time
from collections import deque

class Noeud:
    
    def __init__(self,p,g,d,cle): 
        self.d = d
        self.g = g
        self.p = p
        self.cle = cle

    def print_arbre(self):
        print(self.cle)
        if self.g:
            print ("fils gauche de " + str(self.cle))
            self.g.print_arbre()
        if self.d:
            print ("fils droit de " + str(self.cle))
            self.d.print_arbre()

    #fais remonter l'element (pour l'insertion dans un tas)
    def remonte_elem(self):
        if self.p is None:
            self         
        else:
            if self.cle<self.p.cle:
                tmp=self.cle
                self.cle=self.p.cle
                self.p.cle=tmp
                self.p.remonte_elem()
    
    #Echange un noeud avec son fils gauche
    def switchG(self):
        tmp = self.cle
        self.cle = self.g.cle
        self.g.cle = tmp
    
    #Echange un noeud avec son fils droit
    def switchD(self):
        tmp = self.cle
        self.cle = self.d.cle
        self.d.cle = tmp
    
    #fais descendre l'element courant pour conserver la propriete de tas si les deux fils sont des tas
    def descendre_elem(self):
        if not (self.g is None):
            if not (self.d is None):
                
                if self.g.cle > self.d.cle:
                    if self.d.cle < self.cle:
                        self.switchD()
                        self.d.descendre_elem()
            if self.g.cle < self.cle:
                self.switchG()
                self.g.descendre_elem()

    #transformation de l'arbre en tas en partant de la racine
    #on descend au dernier niveau puis construction du tas par couches successives
    def make_tas(self):
        if self.g != None:
            self.g.make_tas()
            if self.d != None:    
                self.d.make_tas()
            self.descendre_elem()

#version legerement plus efficace
#attention, on ne peut pas mettre une initialisation par defaut de t car sinon, il reutilise le meme tableau sur des appels successifs. bizarre?

def lister_elem(nod, t,i=0):
    if not(nod is None):
        lister_elem(nod.g, t, i+1)
        lister_elem(nod.d, t, i+1)
        t.append(nod.cle)
        if i==0:
            #print "t vaut " + str(t)
            return t

#plus clair mais moins efficace (concatenation des listes plus couteuse)
def lister_elemv2(nod):
    if nod is None:
        return []
    a = lister_elemv2(nod.g) + lister_elemv2(nod.d)
    a.append(nod.cle)
    return a

             
                        
                    
class Arbre:
        
                
    def __init__(self):
        self.rac = None
        self.nb_nds = 0;
        
    #fonction qui construit un tas a partir d'une liste en 2 etapes: construit l'arbre puis le transforme en tas
    def ConstIter(self,l):
        self.constr_arbre(l)
        self.rac.make_tas()
        
    def ajout(self, cle):
        self.nb_nds = self.nb_nds + 1
        pere = self.rac
        #fini
        bits = deque(list(format(self.nb_nds, 'b')))
        #on enleve le premier bit de poids fort
        bits.popleft()
        #on insere a la bonne place en se guidant avec la decomposition binaire
        for i in range(len(bits)-1):
            b = bits.popleft()
            if b == '0':
                pere = pere.g
            else:
                pere = pere.d
         
        print("cle " + str(cle) + str(bits))
        #si il n'y a pas encore d'elements, alors on est en train d'inserer la racine
        if self.rac is None:
            self.rac = Noeud(None, None, None, cle)
            self.rac.remonte_elem()
        else:
            b = bits.popleft()
            if b == '0':
                pere.g = Noeud(pere, None, None, cle)
                pere.g.remonte_elem()
            else:
                pere.d = Noeud(pere, None, None, cle)
                pere.d.remonte_elem()
    
    #fonction couverture de constr_arbre_rec
    def constr_arbre(self, l):
        n = len(l)
        self.nb_nds = n
        self.rac = self.constr_arbre_rec(None, l, 0, n)
    
    #construit un arbre qui n'est pas un tas, il faut ensuite le transformer en tas
    def constr_arbre_rec (self, pere, l, i, n):
        if i>= n:
            return None
        rac = Noeud(pere, None, None, l[i])
        #On utilise les memes indices que dans le tableau, ca facilite le code
        rac.g = self.constr_arbre_rec(rac, l, 2*i+1, n)
        rac.d = self.constr_arbre_rec(rac, l, 2*i+2, n)
        return rac
        

    def print_arbre(self):
        print(self.rac)
        if self.rac != None:
            self.rac.print_arbre()
            
    def supprmin(self):
        pere = self.rac
        cle = 0
        #fini
        bits = deque(format(self.nb_nds, 'b'))
        #on enleve le premier bit de poids fort qui ne sert pas
        bits.popleft()
        for i in range(len(bits)-1):
            b = bits.popleft()
            if b == '0':
                pere = pere.g
            else:
                pere = pere.d
        
        b = bits.popleft()
        
        #cas où le tas contient un unique element
        if b == []:
            del pere
            return
        #nombre pair d'elements: le dernier element est donc un fils gauche
        if b == '0':
            cle = pere.g.cle
            #on enleve bien le fils gauche
            del pere.g
            pere.g = None
            
        #nb impair: le dernier element est un fils droit
        else:
            cle = pere.d.cle
            del pere.d
            pere.d = None
        self.rac.cle = cle
        #on fait descendre la nouvevlle racine pour retrouver la propriete de tas
        self.rac.descendre_elem()
        self.nb_nds = self.nb_nds - 1
         

def Union(t1, t2):
    l1 = lister_elem(t1.rac, [])
    l2 = lister_elem(t2.rac, [])
    l = l1+l2
    a = Arbre()
    a.ConstIter(l)
    return a

a = Arbre()
a.constr_arbre(range(5))

start_time = time.time()
print(lister_elem(a.rac, []))
t_m = (time.time() - start_time)
#print "tm vaut " + str(t_m)
a.ConstIter([5, 4, 3, 2, 1])
b=Arbre()

#tm vaut 0.0337061882019
#tm vaut 0.0440330505371

b.ConstIter([6 ,7, 8, 9, 10])
#print(lister_elem(a.rac))
c = Union(a, b)
c.print_arbre()
#a.print_arbre()

#print("cc")
a.supprmin()
#a.print_arbre()

print(list(format(2, 'b')))

def aj_succ(tab, a):
    for el in tab:
        a.ajout(el)



l1=['../cles_alea/jeu_1_nb_cles_100.txt','../cles_alea/jeu_2_nb_cles_100.txt','../cles_alea/jeu_3_nb_cles_100.txt','../cles_alea/jeu_4_nb_cles_100.txt','../cles_alea/jeu_5_nb_cles_100.txt']

l2=['../cles_alea/jeu_1_nb_cles_200.txt','../cles_alea/jeu_2_nb_cles_200.txt','../cles_alea/jeu_3_nb_cles_200.txt','../cles_alea/jeu_4_nb_cles_200.txt','../cles_alea/jeu_5_nb_cles_200.txt']

l3=['../cles_alea/jeu_1_nb_cles_500.txt','../cles_alea/jeu_2_nb_cles_500.txt','../cles_alea/jeu_3_nb_cles_500.txt','../cles_alea/jeu_4_nb_cles_500.txt','../cles_alea/jeu_5_nb_cles_500.txt']

l4=['../cles_alea/jeu_1_nb_cles_1000.txt','../cles_alea/jeu_2_nb_cles_1000.txt','../cles_alea/jeu_3_nb_cles_1000.txt','../cles_alea/jeu_4_nb_cles_1000.txt','../cles_alea/jeu_5_nb_cles_1000.txt']


l5=['../cles_alea/jeu_1_nb_cles_5000.txt','../cles_alea/jeu_2_nb_cles_5000.txt','../cles_alea/jeu_3_nb_cles_5000.txt','../cles_alea/jeu_4_nb_cles_5000.txt','../cles_alea/jeu_5_nb_cles_5000.txt']

l6=['../cles_alea/jeu_1_nb_cles_10000.txt','../cles_alea/jeu_2_nb_cles_10000.txt','../cles_alea/jeu_3_nb_cles_10000.txt','../cles_alea/jeu_4_nb_cles_10000.txt','../cles_alea/jeu_5_nb_cles_10000.txt']

l7=['../cles_alea/jeu_1_nb_cles_20000.txt','../cles_alea/jeu_2_nb_cles_20000.txt','../cles_alea/jeu_3_nb_cles_20000.txt','../cles_alea/jeu_4_nb_cles_20000.txt','../cles_alea/jeu_5_nb_cles_20000.txt']

l8=['../cles_alea/jeu_1_nb_cles_50000.txt','../cles_alea/jeu_2_nb_cles_50000.txt','../cles_alea/jeu_3_nb_cles_50000.txt','../cles_alea/jeu_4_nb_cles_50000.txt','../cles_alea/jeu_5_nb_cles_50000.txt']


lt = [l1,l2,l3,l4,l5,l6,l7,l8]
absc = [100, 200, 500, 1000, 5000, 10000, 20000, 50000]
t_m = 0
cpt = 1

def parse_file (fic):    
    parsed = []
    fic1=open(fic,'r')
    for line in fic1:
        parsed.append(int(line, 16))
    return parsed


#file = open("../tests/constIter_tas/tas_tab.txt",'r+') 
file2 = open("../tests/constIter_tas/tas_tree.dat","w") 

s = []
g = []
cpt=0
for l in lt:
    z = []
    t_m = 0
    for i in l:
        start_time = time.time()
        a = Arbre()
        a.ConstIter(parse_file(i))
        z.append(a)
        t_m = t_m + (time.time() - start_time)
    g.append(z)
    file2.write(str(absc[cpt]) + ", " + str(t_m/5) + "\n")
    cpt+=1


file = open("../tests/union_tas/tas_tree_union.dat","w") 


import copy
cpt=0
for x in g:
    t_m = 0
    for i in range(0,5):
        y = copy.deepcopy(x[i])
        z = copy.deepcopy(x[(i+1)%5])
        start_time = time.time()
        Union(y,z)
        t_m = t_m + (time.time() - start_time)
    file.write(str(2*absc[cpt]) + ", " + str(t_m/5) + "\n")
    cpt+=1

file.close()


