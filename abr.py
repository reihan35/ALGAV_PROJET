class Noeud:
    
    def __init__(self,g,d,cle): 
        self.d = d
        self.g = g
        self.cle = cle

    def print_arbre(self):
        print(self.cle)
        if self.g:
            print ("fils gauche de " + str(self.cle))
            self.g.print_arbre()
        if self.d:
            print ("fils droit de " + str(self.cle))
            self.d.print_arbre()

class ABR:
	def __init__(self):
		self.rac = None
	
	def set_rac(self, cle):
		self.rac = Noeud(None,None,cle)
	
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
				currentNoeud.g = Noeud(None,None,cle)
		elif(cle > currentNoeud.cle):
			if(currentNoeud.d):
				self.insert_noeud(currentNoeud.d, cle)
			else:
				currentNoeud.d = Noeud(None,None,cle)
	
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

a = ABR()
a.insert(5)
a.insert(7)
a.insert(20)
a.insert(33)
a.insert(25)
a.insert(36)
a.insert(12)

a.print_arbre()
print(a.recherche(2))

