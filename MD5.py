#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 11:30:32 2018

@author: 3535008
"""
import math
import binascii

def MD5(m):
    entier = []
    k = []
    r = [7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22]
    r[16:31] = [5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20]
    r[32:47] = [4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23]
    r[48:63] = [6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21]
    print(r)
    
    for i in range(64):
        k.append(math.floor(abs(math.sin(i+1)) * 2**32))

    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    
    m = list(' '.join(format(ord(x), 'b') for x in m))
    #Taille du message
    n = len(m)
    print m
    m.append('1')
    print m
    
    i = (n+1) %512
    while i != 448:
        m.append('0')
        i = (i + 1)%512
    
    
    #attention, little endian a check?
    n_bin = list(format(n, '064b'))
    n_bin.reverse()
    print(n_bin)
    m = m + list(n_bin)
    print (m)
    
    
    nb_iter = m/512
    #On decoupe en blocs de 512
    for b in range (nb_iter):
        bloc = m[b*512:(b+1)*512]
        w = []
        #On decoupe en 16 mots de 32 bits
        for i in range (16):
            w.append(m[i:(i+1)*16])
        
        a = h0
        b = h1
        c = h2
        d = h3
        
        for i in range(64):
            if i <= 15:
                f = (b & c) | ((~b) & d)
            elif i <= 31:
                f = (d & b) | ((~d) & c)
                g = (5*i + 1) %16 
            elif i <= 47:
                f = b ^ c ^ d
                g = (3*i + 5) % 16
            elif i <= 63:
                f = c ^ (b | (~d))
                g = (7*i) % 16
            
            tmp = d
            d = c
            c = b
            b = ((a + f + k[i] + w[g]) << r[i]) + b
            a = tmp
        
        h0 = h0 +a
        h1 = h1 + b
        h2 = h2 + c
        h3 = h3 + d
        

    


MD5("salut")