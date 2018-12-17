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
import tasTableau
import binomiale
import time

from collections import defaultdict

folder = "../Shakespeare/"

'''Q6.12'''

'''
a = abr.ABR()
for f in os.listdir(folder):
    f = open(folder + f, "r")
    for line in f:
    	a.insert((MD5.md5(line.rstrip("\n\r"))))


m = []
for f in os.listdir(folder):
    f = open(folder + f, "r")
    for line in f:
    	if line.rstrip("\n\r") not in m:
    		m.append(line.rstrip("\n\r"))

'''

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


l = []
for f in os.listdir(folder):
    f = open(folder + f, "r")
    for line in f:
    	if MD5.md5(line.rstrip("\n\r")) not in l:
    		l.append(MD5.md5(line.rstrip("\n\r")))

'''
start_time = time.time()
tas = tasTableau.ConsIter(l)
end_time = (time.time() - start_time)
print(end_time)

tas = tasTableau.ConsIter(l)
start_time = time.time()
tasTableau.ajout(tas,l[1])
end_time = (time.time() - start_time)
print(end_time)

tas = tasTableau.ConsIter(l)
start_time = time.time()
tasTableau.supprmin(tas)
end_time = (time.time() - start_time)


tas = tasTableau.ConsIter(l)
tas2 = tasTableau.ConsIter(l)
start_time = time.time()
tasTableau.Union(tas,tas2)
end_time = (time.time() - start_time)

print(end_time)
'''
'''
file = binomiale.ConsIter(l)
start_time = time.time()
binomiale.Ajout(file,l[1])
end_time = (time.time() - start_time)
print(end_time)

file = binomiale.ConsIter(l)
start_time = time.time()
binomiale.SupprMin(file)
end_time = (time.time() - start_time)
print(end_time)
'''
file = binomiale.ConsIter(l)
file2 = binomiale.ConsIter(l)
start_time = time.time()
binomiale.UnionFile(file,file2)
end_time = (time.time() - start_time)
print(end_time)
'''

'''
#print(m)
#a.print_arbre()

#Q6.14
