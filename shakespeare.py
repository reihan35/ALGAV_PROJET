#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 12:30:38 2018

@author: 3535008
"""
import re
import os
import abr
import MD5
import projet

from collections import defaultdict

folder = "Shakespeare/"

'''Q6.12'''

'''
a = abr.ABR()
for f in os.listdir(folder):
    f = open(folder + f, "r")
    for line in f:
    	a.insert((MD5.md5(line.rstrip("\n\r"))))

'''
m = []
for f in os.listdir(folder):
    f = open(folder + f, "r")
    for line in f:
    	if line.rstrip("\n\r") not in m:
    		m.append(line.rstrip("\n\r"))


'''Q6.13'''

'''

d = defaultdict(list)
for f in os.listdir(folder):
	f = open(folder + f, "r")
	for line in f:
		h = MD5.md5(line.rstrip("\n\r"))
		if line.rstrip("\n\r") not in d[h]:
			d[h].append(line.rstrip("\n\r"))

#d = defaultdict(list)

for key, value in d.items():
	if len(value) == 2:	
		print(value)
'''
projet.ajout(m[0])
projet.ConsIter(m)
projet.supprmin(m)

#print(m)
#a.print_arbre()

#Q6.14
