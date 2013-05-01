#!/usr/bin/env python

import codecs


def fix():
    
    inFile = codecs.open("in.txt", "r")
    outFile = codes.open("out.txt", "w")
    
    for line in inFile:
        for word in line.split():
            if( calc_length(word) < screen ):
                outFile.write(word)
            else
                outFile.write('\n'+word)              


def calc_length(word):
    length = 0
    for ch in word:
        length = length + xList(ch)
        
    return length


def main():
    pass
    
        
if __name__ == '__main__':
    main()
