#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import sys

import arabic_reshaper
from bidi.algorithm import get_display

xForward = 0
yForward = 0

space = 3#pixel
newLine = 15#pixel

lengthList = {
    u'ا' : [14,0,2],
    u'ب' : [8, 5, 17]
}


def makeBox():
    
    textFile = codecs.open(sys.argv[1], "r")
    for line in textFile:
        words = get_display(arabic_reshaper.reshape(line)).split()
        for word in words:
            findBound(word)
            
        newLine += newLine
        space = 0   


def findBound(word):
        
    top = []
    bottom = []
    
    for char in word:
        length += lengthList[char][0]
        bottom.append(lengthList[char][1])
        top.append(lengthList[char][2])
        
    addBox( max(bottom), length, max(top), word )
    

def addBox(bottom, length, top, word):
    
    outFile = sys.argv[1].split(".txt")[0] + ".exp%s"%sys.argv[2] + ".box"
    boxFile = codecs.open(outFile, "w")
    boxFile.write(word, xForward, bottom, xForward+length, top, 0)
    

def main():
    if len(sys.argv) != 3:
        sys.exit( "file %s not found" % sys.argv[0] )
    else:
        makeBox()
    
    
if __name__ == '__main__':
    main()
    
    
    
    
