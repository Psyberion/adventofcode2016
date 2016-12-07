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
	directions=[(0,1),	# North
				(1,0),	# East
				(0,-1),	# South
				(-1,0)]	# West
	d=0
	visited=set()
	for item in data:
		steps = int(item[1:])
		if item[0] is "L":
			d = (d+1)%4
		elif item[0] is "R":
			d = (d-1)%4
		for i in range(steps):
			visited.add((x,y))
			x += 1*directions[d][0]
			y += 1*directions[d][1]
			if (x,y) in visited:
				return x,y
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
	print "{} blocks away".format(abs(x)+abs(y))

if __name__ == '__main__':
	main()
