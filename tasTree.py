#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 10:52:41 2018

@author: 3535008
"""

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

    def make_tas(self):
        if self.g != None:
            self.g.make_tas()
            if self.d != None:    
                self.d.make_tas()
            self.descendre_elem()
             
                        
                    
class Arbre:
        
                
    def __init__(self):
        self.rac = None
        self.nb_nds = 0;
        
    def make_tas_a(self,l):
        self.constr_arbre(l)
        self.rac.make_tas()
        
    def ajout(self, cle):
        self.nb_nds = self.nb_nds + 1
        pere = self.rac
        #fini
        bits = deque(list(format(self.nb_nds, 'b')))
        bits.popleft()
        #on vire le premier bit de poids fort
        for i in range(len(bits)-1):
            b = bits.popleft()
            if b == '0':
                pere = pere.g
            else:
                pere = pere.d
         
        print("cle " + str(cle) + str(bits))
        if self.rac is None:
            self.rac = Noeud(None, None, None, cle)
            self.rac.remonte_elem()
            self.lastAjout = self.rac
        else:
            b = bits.popleft()
            if b == '0':
                pere.g = Noeud(pere, None, None, cle)
                pere.g.remonte_elem()
                self.lastAjout = pere.g
            else:
                pere.d = Noeud(pere, None, None, cle)
                pere.d.remonte_elem()
                self.lastAjout = pere.d
    
    def constr_arbre(self, l):
        n = len(l)
        self.nb_nds = n
        self.rac = self.constr_arbre_rec(None, l, 0, n)
    
    def constr_arbre_rec (self, pere, l, i, n):
        rac = Noeud(pere, None, None, l[i])
        if 2*i+1 >= n:
            rac.g = None
        else:
            rac.g = self.constr_arbre_rec(rac, l, 2*i+1, n)
            
            if 2*i+2 >= n:
                rac.d = None
            else:
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
        bits = deque(list(format(self.nb_nds, 'b')))
        bits.popleft()
        #on vire le premier bit de poids fort
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
            del pere.g
            pere.g = None
            
        #nb impair: le dernier element est un fils droit
        else:
            cle = pere.d.cle
            del pere.d
            pere.d = None
        self.rac.cle = cle
        self.rac.descendre_elem()
        self.nb_nds = self.nb_nds - 1
         



a = Arbre()
#a.constr_arbre([5, 4, 3, 2, 1])
a.make_tas_a([5, 4, 3, 2, 1])
a.print_arbre()

print("cc")
a.supprmin()
a.print_arbre()
"""
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
        thislevel = nextlevel

    def descendre_elem(self):
        print ("a")
        if not (self.g is None):
            if not (self.d is None):
                if self.g.cle > self.d.cle:
                    if self.d.cle < self.cle:
                        self.switch(self.d.cle, self.cle)
                        
                        tmp=self.cle
                        self.cle=self.d.cle
                        self.d.cle=tmp
                        
                        self.d.descendre_elem()
            else:
                if self.g.cle < self.cle:
                    self.switch(self.g.cle, self.cle)

                        tmp=self.cle
                        self.cle=self.g.cle
                        self.g.cle=tmp

                    self.g.descendre_elem()


def traverse2(rootnode):
  thislevel = [root2(rootnode):
  thislevel = [rootnode]
  while thislevel:
    nextlevel = list()
    for n in thislevel:
      print n.cle,
      if n.g: nextlevel.append(n.g)
      if n.d: nextlevel.append(n.d)
    printnode]
  while thislevel:
    nextlevel = list()
    for n in thislevel:
      print n.cle,
      if n.g: nextlevel.append(n.g)
      if n.d: nextlevel.append(n.d)
    print
    thislevel = nextlevel 
"""
print(list(format(2, 'b')))

def aj_succ(tab, a):
    for el in tab:
        a.ajout(el)

"""
def main():
    fic = "cles_alea/jeu_5_nb_cles_50000.txt"
    content = parse_file(fic)
    #print(content)
    #print(len(content))
    #print(eg(content[0], content[2]))
    #print(inf(content[4], content[0]))
    
    tas = [2,5,6,10,13,8, 7]
    tas2=ConsIter([1,5,3,0,8,2])a.ajout(8)
    a.ajout(5)
    a.ajout(6)
    a.ajout(7)
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

    #traverse2(root)
    
    root.print_arbre()
    
    #root.remonte_elem(Noeud(3))
    
    #root.print_arbre()
    #root.ajout(6)
    

    #root.print_arbre()
"""

def main():
    a = Arbre()
    aj_succ([9, 8, 7, 6, 5, 4, 3, 2, 1], a)
    
    a.supprmin()
    a.print_arbre()
    print ("salut")
    
#main()