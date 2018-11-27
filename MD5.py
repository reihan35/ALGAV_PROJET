#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 11:30:32 2018

@author: 3535008
"""
import math
import binascii


# Rotate left: 0b1001 --> 0b0011
def left_rotate (val, r_bits, max_bits):
    return (val << r_bits%max_bits) & (2**max_bits-1) | ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))


add = 2**32

def MD5(m):
    k = []
    r = []
    r[0:15] = [7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22]
    r[16:31] = [5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20]
    r[32:47] = [4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23]
    r[48:63] = [6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21]
    print(r)
    
    for i in range(64):
        k.append(int(math.floor(abs(math.sin(i+1)) * 2**32)))

    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    
    #On convertit le message en nombre binaire
    m = list(''.join(format(ord(x), 'b') for x in m))
    #Taille du message
    print (m)
    n = len(m)
    m.append('1')
    print (n)
    
    i = (n+1) %512
    while i != 448:
        m.append('0')
        i = (i + 1)%512
    
    print (len(m))
    
    
    #attention, little endian a check?
    n_bin = list(format(n, '064b'))
    n_bin.reverse()
    #print(n_bin)
    m = m + list(n_bin)
    #print (m)

    #print (len(m))
    nb_iter = int(len(m)/512)
    #On decoupe en blocs de 512
    for b in range (nb_iter):
        print("salut")
        bloc = m[b*512:(b+1)*512]
        
        print bloc
        w = []
        #On decoupe en 16 mots de 32 bits
        for i in range (16):
            w.append(bloc[i*32:(i+1)*32])
            print i
            print w[i]
        a = h0
        b = h1
        c = h2
        d = h3
        
        for i in range(64):
            if i <= 15:
                f = (b & c) | ((~b) & d)
                g = i
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
            """
            print "wf = "
            """
            #print w[g]
            w_g = int("".join(w[g]), 2)
            #print ("g = " + str(g) + " " + str(w_g))
            #c'est sans doute ici que ca foire, dans les 3 lignes suivantes
            #p-e pad et rajouter des 0 si le nombre n'atteint pas 32 bits?
            tmp2 =  (a + f + k[i] + w_g) %add
            print(len(bin(tmp2))-2)
            b = (left_rotate(tmp2, r[i], 32) + b) % add
            a = tmp
        
        h0 = (h0 + a) %add
        h1 = (h1 + b) %add
        h2 = (h2 + c) %add
        h3 = (h3 + d) %add
    
    hashed = hex(h0 + h1 + h2 + h3)
    #print (hashed)
    print r
    print (str(hex(h0))+ '\n' + str(hex(h1))+'\n' + str(hex(h2))+ '\n' + str(hex(h3)) )
        

    

print(left_rotate(1, 32, 32))


print (len ("d6aa97d33d459ea3670056e737c99a3d"))
MD5("Wikipedia, l'encyclopedie libre et gratuite")


print(len(bin(2)))