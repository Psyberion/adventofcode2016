#!/usr/bin/env python

import os
import sys

def getData(fileName):
	lines=[]
	with open(fileName) as f:
		for line in f.readlines():
			lines.append(line.strip())
	return lines

def getCode(data):
	dirs = {'U':(0,-1),
			'D':(0,1),
			'L':(-1,0),
			'R':(1,0)
			}
	pad = [
		[1,2,3],
		[4,5,6],
		[7,8,9]
	]
	code = ""
	coord = (1,1)
	for line in data:
		for c in line:
			x = coord[0]+dirs[c][0]
			y = coord[1]+dirs[c][1]
			if x < 0 or 2 < x:
				x = coord[0]
			if y < 0 or 2 < y:
				y = coord[1]
			coord = (x,y)
		code += str(pad[coord[1]][coord[0]])
	return code

def main():
	if len(sys.argv) > 2:
		print "Usage: {} FILE".format(sys.argv[0])
	
	code=getCode(getData(sys.argv[1]))
	print code

if __name__ == '__main__':
	main()
