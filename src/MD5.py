#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 11:30:32 2018

@author: 3535008

"""

# coding: encoding
# coding: utf8
import math
 
r= [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
                  5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20,
                  4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
                  6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]

k = [int(abs(math.sin(i+1)) * 2**32) & 0xFFFFFFFF for i in range(64)]
 
 
def left_rotate(x, amount):
    x &= 0xFFFFFFFF
    return ((x<<amount) | (x>>(32-amount))) & 0xFFFFFFFF
 
def md5(message):
    message = bytearray(message, 'utf-8') #copy our input into a mutable buffer
    #print (message)
    l_msg = (8 * len(message)) & 0xffffffffffffffff
    #vrai car on a que des octets en entree
    message.append(0x80)
    while len(message)%64 != 56:
        message.append(0)
    message += l_msg.to_bytes(8, byteorder='little')
 
    h0 = 0x67452301
    h1 = 0xefcdab89
    h2 = 0x98badcfe
    h3 = 0x10325476
 
    #en octets
    for bloc in range(0, len(message), 64):
        
        a = h0
        b = h1
        c = h2
        d = h3
        w = message[bloc:bloc+64]
        for i in range(64):
            if i < 16:
                f=(b & c) | (~b & d)
                g = i
            elif i < 32:
                f = (d & b) | (~d & c)
                g = (5*i + 1)%16
            elif i < 48:
                f = b ^ c ^ d
                g = (3*i + 5)%16
            elif i < 64:
                f = c ^ (b | ~d)
                g = (7*i)%16
            #print("f vaut " + str(f) + " g vaut " + str(g))
            to_rotate = a + f + k[i] + int.from_bytes(w[4*g:4*g+4], byteorder='little')
            new_b = (b + left_rotate(to_rotate, r[i])) & 0xFFFFFFFF
            a, b, c, d = d, new_b, b, c
        

        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF

    #print( h0)
    #print( h1)
    #print( h2)
    #print( h3)
    #return h0<<32
    
    res=(((((h3<<32) | h2)<<32) | h1)<<32) |h0
    raw = res.to_bytes(16, byteorder='little')
    return hex(int.from_bytes(raw, byteorder='big'))
    #return sum(x<<(32*i) for i, x in enumerate(hash_pieces))
 


 #bytearray("salut", 'utf-8')
#print (len ("d6aa97d33d459ea3670056e737c99a3d"))
print ( md5("Wikipedia, l'encyclopedie libre et gratuite"))
