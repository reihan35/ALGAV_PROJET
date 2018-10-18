#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 11:06:30 2018

@author: 3522144
"""

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
    while((i-1)/2 >= 0 and tas[(i-1)/2]>tas[i]):
        tmp=tas[(i-1)/2]
        tas[(i-1)/2]=tas[i]
        tas[i]=tmp
        i=(i-1)/2
        
def ConsIter(l):
    tas = []
    while(l!=[]):
        ajout(tas,l.pop())
    return tas

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
        #print(self.p.cle)
        if self.p is None:
            #print("hello")
            self         
        else:
            
            #print(n.cle)
            #print(self.cle)
            if self.cle<self.p.cle:
                #print("salut")
                tmp=self.cle
                self.cle=self.p.cle
                self.p.cle=tmp
                #print(self.p.cle)
                self.remonte_elem()
            else:
                #print("saluttttt")
                self

    def ajout_fin(self,cle):
        if self.g is None or self.d is None :
            if self.g is None:
                self.g = Noeud(self,None,None,cle)
                #print("coucou")
               # print(self.g.cle)
                self.g.remonte_elem()
            else:
                self.d = Noeud(self,None,None,cle)
                self.d.remonte_elem()
        else:   
            self.g.ajout_fin(cle)
           # self.d.ajout_fin(cle)


    def ajout(self,cle):
        self.ajout_fin(cle)
        #self.remonte_elem(self.der())
                    
    
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
    
    root = Noeud(None,None,None,6)
    root.ajout_fin(7)
    root.ajout_fin(3)
    root.ajout_fin(12)

    root.remonte_elem()
    
    root.print_arbre()
    
    #root.remonte_elem(Noeud(3))
    
    #root.print_arbre()
    #root.ajout(6)
    

    #root.print_arbre()
    
main()
