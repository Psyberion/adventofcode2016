#!/usr/bin/env python

import sys
import collections

def getData(fileName):
	data = []
	with open(fileName) as f:
		for line in f.readlines():
			for i,c in enumerate(line.strip()):
				if i > len(data)-1:
					data.append("")
				data[i] += c
	print data
	return data

def getMessage(data):
	message = ""
	for item in data:
		counter = collections.Counter(item)
		message += counter.most_common()[-1][0]
	return message

def main():
	if len(sys.argv) < 2:
		print "Usage: {} FILE".format(sys.argv[0])
		sys.exit(1)
	print getMessage(getData(sys.argv[1]))
	return 0

if __name__ == '__main__':
	main()