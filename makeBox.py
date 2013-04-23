#!/usr/bin/env python

import codecs
import sys

xForward = 0
yForward = 0

space = 0
newLine = 0

def makeBox():
    
    myFile = codecs.open("a.txt")
    for line in myFile:
        words = line.split()
        for word in words:
            findBound(word)
            
        newLine += newLine
        space = 0   


def findBound(word):
    
    xp = []
    xm = []
    yp = []
    xm = []
    
    for char in word:
        xp.append(xplist[char])
        yp.append(yplist[char])
        xm.append(xmlist[char])
        ym.append(yplist[char])
        
    addBox( max(xp), max(yp), max(xm), max(ym) )
    

def addBox(xp, yp, xm, ym):
    pass
    
    
    
    
    
    
    
