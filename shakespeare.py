#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 12:30:38 2018

@author: 3535008
"""

import os
import abr
folder = "Shakespeare/"


a = abr.ABR()
for f in os.listdir(folder):
    f = open(folder + f, "r")
    for line in f:
        print ("")
        
