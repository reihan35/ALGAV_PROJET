#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 10:36:01 2018

@author: 3535008
"""

class Noeud:
    
    def __init__(self,p,g,d,cle): 
        self.d = d
        self.g = g
        self.p = p
        self.cle = cle
        self.prof = 0
        self.fact = 0

    def print_arbre(self):
        print(self.cle)
        if self.g:
            print ("fils gauche de " + str(self.cle))
            self.g.print_arbre()
        if self.d:
            print ("fils droit de " + str(self.cle))
            self.d.print_arbre()
    
    def isRightHeavy(self):
        return fact < 0
    
    def isLeftHeavy(self):
        return fact < 0

class ABR:
    
	def __init__(self):
		self.rac = None
	
	def set_rac(self, cle):
		self.rac = Noeud(None,None,None,cle)
	
	def insert(self, cle):
		if(self.rac is None):
			self.set_rac(cle)
		else:
			self.insert_noeud(self.rac, cle)	
	def insert_noeud(self, currentNoeud, cle):
		if(cle <= currentNoeud.cle):
			if(currentNoeud.g):
				self.insert_noeud(currentNoeud.g, cle)
			else:
				currentNoeud.g = Noeud(currentNoeudNone,None,cle)
                  
		elif(cle > currentNoeud.cle):
			if(currentNoeud.d):
				self.insert_noeud(currentNoeud.d, cle)
			else:
				currentNoeud.d = Noeud(currentNoeud,None,None,cle)
	
	def recherche(self, cle):
		return self.recherche_noeud(self.rac, cle)
	
	def recherche_noeud(self, currentNoeud, cle):
		if(currentNoeud is None):
			return False
		elif(cle == currentNoeud.cle):
			return True
		elif(cle < currentNoeud.cle):
			return self.recherche_noeud(currentNoeud.g, cle)
		else:
			return self.recherche_noeud(currentNoeud.d, cle)

	def print_arbre(self):
		print(self.rac)
		if self.rac != None:
			self.rac.print_arbre()



def rotation_droite(a):
    tmp = a.g
    a.g = a.g.d
    tmp.d= a
    return tmp

def rotation_gauche(a):
    tmp = a.d
    a.d = a.d.g
    tmp.g = a
    return tmp

def rotation_gauche_droite(a):
    

def reequilibrage(a):
    if isRightHeavy(a):
        if isLeftHeavy(a.d):
            double_rotation_gauche(a)
        else:
            rotation_gauche(a)
        elif isLeftHeavy(a):
            if isRightHeavy(a.g):
                double_rotation_droite(a)
            else:
                rotation_droite(a)

a = ABR()
a.insert(20)
a.insert(7)
a.insert(5)
a.insert(33)
a.insert(25)
a.insert(36)
a.insert(12)

a.print_arbre()
print(a.recherche(2))

print "cc" + str(a.rac)
a.rac = rotation_gauche(a.rac)

a.print_arbre()
    