#!/usr/bin/env python

import codecs
import sys
import topList
import bottomList

xForward = 0
yForward = 0

space = 3#pixel
newLine = 15#pixel

lengthList = {}
topList = {}
bottomList = {}

def makeBox():
    
    textFile = codecs.open(sys.argv[1], "r")
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
        bottom.append(bottomList[char][1])
        top.append(topList[char][0])        
        
    addBox( max(bottom), length, max(top), word )
    

def addBox(bottom, length, top, word):
    boxFile = codecs.open(sys.argv[1], "w")
    boxFile.write(word, xForward, bottom, xForward+length, top, 0)
    

def main():
    if len(sys.argv) != 2:
        sys.exit( "file %s not found" % sys.argv[1] )
    else:
        makeBox()
    
    
if __name__ == '__main__':
    main()
    
    
    
    
