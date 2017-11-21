#!/usr/bin/env python

import sys
import collections
from string import ascii_lowercase as ascii

def extractData(fileName):
	data = []
	with open(fileName) as f:
		for line in f.readlines():
			delim = line.rfind("-")
			rawName = line[:delim]
			name = ''.join(line[:delim].split("-"))
			ident = int(line[delim+1:delim+4])
			checksum = line[delim+5:delim+10]
			data.append({"raw":rawName,"name":name,"id":ident,"checksum":checksum})
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

def decrypt(rooms):
	for room in rooms:
		name=""
		for c in room["raw"]:
			if c == '-':
				name += ' '
			elif c in ascii:
				i = (ascii.index(c)+room["id"])%len(ascii)
				name += ascii[i]
		if name == "northpole object storage":
			return room["id"]

def main():
	if len(sys.argv) > 2:
		print "Usage: {} FILE".format(sys.argv[0])
		sys.exit(1)
	print decrypt(getTrueRooms(extractData(sys.argv[1])))

if __name__ == '__main__':
	main()
