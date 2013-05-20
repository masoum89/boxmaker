#!/usr/bin/env python

import codecs
import sys
import bound

length = 0

def fix():
    
    inFile = codecs.open(sys.argv[1], "r","utf-8")
    outFile = codecs.open("out.txt", "w","utf-8")
    global length
    temp=0
    
    for line in inFile:
        for word in line.split():
            if( calc_length(word) < 1300 ):
                outFile.write(word+' ')
                temp=length

            else:
                outFile.write('\n'+ word +' ')
                length=length-temp			


def calc_length(word):

	for ch in word:
		global length
		length = length + bound.lengthList[ch][2]
	return length


def main():
	fix()
        
if __name__ == '__main__':
    main()
