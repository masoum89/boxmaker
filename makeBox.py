#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import sys

sys.path.insert(0 , './header')

import arabic_reshaper
from bidi.algorithm import get_display

import bound

xForward = 28
yForward = 561

space = 8#pixel
newLine = 15#pixel

outFile = sys.argv[1].split(".txt")[0] + ".exp%s" %sys.argv[2] + ".box"
boxFile = codecs.open(outFile, "w", "utf-8")


def makeBox():
    
    global newLine
    global xForward
    global yForward
    
    textFile = codecs.open(sys.argv[1], "r","utf-8")

    for line in textFile:
        words = line.split()
        
        for word in words:            
            #findBound( get_display(arabic_reshaper.reshape(word)) )
            findBound( word )
            xForward = xForward + space
        
        newLine += newLine        
        yForward -=28



def findBound(word):
    length=0    
    top = []
    bottom = []    
        
    for char in word:
        length += bound.lengthList[char][2]
        bottom.append(bound.lengthList[char][1])
        top.append(bound.lengthList[char][0])        
  
    addBox(max(bottom),length,max(top),word)
    

def addBox(bottom, length, top, word):
    
    global xForward 
     
    print word, xForward, yForward-bottom, xForward+length, yForward+top ,"0" 
    xForward = xForward + length 
            
    boxFile.write( unicode(word.encode('utf-8'),'utf-8')+" "+str(xForward)+" "+str(yForward-bottom)+" "+ 
        str(xForward+length)+
        " "+str(yForward+top)+"\n"
    )
    

def main():

    if len(sys.argv) != 3:
        sys.exit( "file %s not found" % sys.argv[1] )
    else:
		makeBox()
    
    
if __name__ == '__main__':
    main()
    
    
