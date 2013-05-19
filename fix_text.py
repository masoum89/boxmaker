#!/usr/bin/env python

import codecs
import sys

def fix():
    
    inFile = codecs.open(sys.argv[1], "r")
    outFile = codes.open("out.txt", "w")
    
    for line in inFile:
        for word in line.split():
            if( calc_length(word) < screen ):
                outFile.write(word)
            else:
                outFile.write('\n'+word)              


def calc_length(word):
    length = 0
    for ch in word:
        length = length + lengthList[ch][2]
        
    return length


def main():
    if len(sys.argv) != 3:
        sys.exit( "file %s not found" % sys.argv[0] )
    else:
        fix()
    
        
if __name__ == '__main__':
    main()
