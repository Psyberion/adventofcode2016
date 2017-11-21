#!/usr/bin/env python

import os
import sys

def extractDirections(fileName):
	data = ""
	with open(fileName) as f:
		data = f.read().strip().split(", ")
	return data

def getDistance(data):
	y=0
	x=0
	directions=[(1,0),	# North
				(0,1),	# East
				(-1,0),	# South
				(0,-1)]	# West
	d=0
	for item in data:
		turn = item[0]
		steps = int(item[1:])
		if turn is "L":
			d = (d+1)%4
		elif turn is "R":
			d = (d-1)%4
		y = y+(steps*directions[d][0])
		x = x+(steps*directions[d][1])
	return x,y


def main():
	if len(sys.argv) != 2:
		print "Usage: {} FILE".format(sys.argv[0])
		sys.exit(1)
	if not os.path.isfile(sys.argv[1]): 
		print "File not found: {}".format(sys.argv[1])
		sys.exit(1)
	x,y = getDistance(extractDirections(sys.argv[1]))
	print "X: " + str(x)
	print "Y: " + str(y)
	print "{} blocks away".format(x+y)

if __name__ == '__main__':
	main()
