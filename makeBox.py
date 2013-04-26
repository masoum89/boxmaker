#!/usr/bin/env python

import codecs
import sys

xForward = 0
yForward = 0

space = 3#pixel
newLine = 15#pixel

lengthList = {}
topList = {}
bottomList = {}

def makeBox():
    
    textFile = codecs.open("a.txt", "r")
    for line in textFile:
        words = line.split()
        for word in words:
            findBound(word)
            
        newLine += newLine
        space = 0   


def findBound(word):
        
    top = []
    bottom = []
    
    for char in word:
        length += lengthList[char]
        bottom.append(bottomList[char])
        top.append(topList[char])        
        
    addBox( max(bottom), length, max(top), word )
    

def addBox(bottom, length, top, word):
    boxFile = codecs.open("a.txt", "w")
    boxFile.write(word, space, bottom, space+length, top)
    

def main():
    pass
    
    
if __name__ == '__main__':
    pass
    
    
    
    
