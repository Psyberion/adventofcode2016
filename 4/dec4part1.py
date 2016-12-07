#!/usr/bin/env python

import sys
import collections

def extractData(fileName):
	data = []
	with open(fileName) as f:
		for line in f.readlines():
			delim = line.rfind("-")
			name = ''.join(line[:delim].split("-"))
			ident = int(line[delim+1:delim+4])
			checksum = line[delim+5:delim+10]
			data.append({"name":name,"id":ident,"checksum":checksum})
	return data

def getTrueRooms(rooms):
	trueRooms = []
	for room in rooms:
		counter = collections.Counter(room["name"])
		tmp = sorted(counter, key=lambda char: (-counter[char], char))
		checksum = ''.join(tmp[:5])
		if checksum == room["checksum"]:
			trueRooms.append(room)
	return trueRooms

def main():
	if len(sys.argv) > 2:
		print "Usage: {} FILE".format(sys.argv[0])
		sys.exit(1)
	ids = [d['id'] for d in getTrueRooms(extractData(sys.argv[1]))]
	print sum(ids)

if __name__ == '__main__':
	main()
