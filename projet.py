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
    i=0
    while(2*i+1<len(tas)):
        print("val i :" + str(i))
        tas[i]=min(tas[2*i+1],tas[2*i+2])
        if(tas[i]==tas[2*i+1]):
            i=2*i+1
        else:
            i=2*i+2
    del tas[i]
    
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

def percolateDown(pere, tas, cpt):
    while 2*pere+1 < len(tas):
        cpt = cpt +1
        #recuperer le fils minimum
        f_g = 2*pere+1
        f_d = 2*pere+2

        f_min = min(tas[f_g], tas[f_d])
        if(tas[pere] <  f_min):
            break
        #on fait descendre le pere a gauche
        if tas[f_g] < tas[f_d]:
            switch(f_g, pere, tas)
            pere = f_g
        #a droite
        else:
            switch(f_d, pere, tas)
            pere = f_d
    return cpt
    
int(2.6)
def ConsIter(l):
    tas = list(l)
    n = len(l)
    h = int(math.log(n, 2)) - 1
    i = int(pow(2, h)-1)
    nxt_lvl = 2*i+1
    cpt = 0
    while h >= 0:
        print h
        #parcours d'un niveau
        while (i < nxt_lvl):
            cpt = percolateDown(i, tas, cpt)
            i = i+1
        h = h - 1
        i = int(pow(2, h)-1)
        nxt_lvl = 2*i+1
    print cpt
    return tas

print ConsIter([9, 8, 7, 6, 5, 4, 3])

def union(tas1,tas2):
    l = tas1 +  tas2 
    ConsIter(l)

class Noeud:

    def __init__(self,p,g,d,cle): 
        self.d = d
        self.g = g
        self.p = p
        self.cle = cle

    def print_arbre(self):
        print(self.cle)
        if self.g:
            self.g.print_arbre()
        if self.d:
            self.d.print_arbre()

    def remonte_elem(self):
        if self.p is None:
            self         
        else:
            if self.cle<self.p.cle:
                tmp=self.cle
                self.cle=self.p.cle
                self.p.cle=tmp
            self.p.remonte_elem()

    def ajout(self,cle):
        if self.g is None or self.d is None :
            if self.g is None:
                self.g = Noeud(self,None,None,cle)
                self.g.remonte_elem()
            else:
                self.d = Noeud(self,None,None,cle)
                self.d.remonte_elem()
        else:
            self.g.ajout(cle)

'''
    def traverse(self,rootnode,cle):
        thislevel = [rootnode]
        while thislevel:
            nextlevel = list()
            for n in thislevel:
               # print n.value,
                if n.g: nextlevel.append(n.g)
                if n.d: nextlevel.append(n.d)
                else :
                    if n.left is None: 
                        self.g = Noeud(self,None,None,cle)
                        self.g.remonte_elem()
                    else: 
                         self.d = Noeud(self,None,None,cle)
                         self.d.remonte_elem()
            print
        thislevel = nextlevel


def traverse3(a,rootnode,cle):
        thislevel = [rootnode]
        while thislevel:
            nextlevel = list()
            for n in thislevel:
               # print n.value,
                if n.g: nextlevel.append(n.g)
                if n.d: nextlevel.append(n.d)
                else :
                    if n.left is None: 
                        a.g = Noeud(a,None,None,cle)
                        a.g.remonte_elem()
                    else: 
                         a.d = Noeud(a,None,None,cle)
                         a.d.remonte_elem()
            print
        thislevel = nextlevel'''


def traverse2(rootnode):
  thislevel = [rootnode]
  while thislevel:
    nextlevel = list()
    for n in thislevel:
      print n.cle,
      if n.g: nextlevel.append(n.g)
      if n.d: nextlevel.append(n.d)
    print
    thislevel = nextlevel 



def main():
    fic = "cles_alea/jeu_5_nb_cles_50000.txt"
    content = parse_file(fic)
    #print(content)
    #print(len(content))
    #print(eg(content[0], content[2]))
    #print(inf(content[4], content[0]))
    
    tas = [2,5,6,10,13,8, 7]
    tas2=ConsIter([1,5,3,0,8,2])
    #print(tas2)
    
    root = Noeud(None,None,None,7)
    #root.traverse(,2)
    root.ajout(19)
    root.ajout(25)
    root.ajout(100)
    root.ajout(3)
    root.ajout(1)
    root.ajout(36)
    root.ajout(17)

    traverse2(root)
    
    #root.print_arbre()
    
    #root.remonte_elem(Noeud(3))
    
    #root.print_arbre()
    #root.ajout(6)
    

    #root.print_arbre()
    
#main()
