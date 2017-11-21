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
		['-1','-1', '1','-1','-1'],
		['-1', '2', '3', '4','-1'],
		[ '5', '6', '7', '8', '9'],
		['-1', 'A', 'B', 'C','-1'],
		['-1','-1', 'D','-1','-1']
	]
	code = ""
	coord = (0,2)
	for line in data:
		for c in line:
			xTmp = coord[0]+dirs[c][0]
			yTmp = coord[1]+dirs[c][1]
			x = coord[0]
			y = coord[1]
			if 0 <= xTmp and xTmp <= 4:
				x = xTmp
			if 0 <= yTmp and yTmp <= 4:
				y = yTmp
			if pad[x][y] == '-1':
				x = coord[0]
				y = coord[1]
			coord = (x,y)
		code += str(pad[coord[1]][coord[0]])
	return code

def main():
	if len(sys.argv) > 2:
		print "Usage: {} FILE".format(sys.argv[0])
		sys.exit(1)
	
	print getCode(getData(sys.argv[1]))

if __name__ == '__main__':
	main()
