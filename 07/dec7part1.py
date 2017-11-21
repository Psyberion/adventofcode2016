#!/usr/bin/env python

import sys

def getData(fileName):
	data = []
	with open(fileName) as f:
		for line in f.readlines():
			line = line.strip()
			hypernets = []
			parts = []
			try:
				while line.index("["):
					delim1 = line.index("[")
					parts.append(line[:delim1])
					line = line[delim1+1:]
					delim2 = line.index("]")
					hypernets.append(line[:delim2])
					line = line[delim2+1:]
			except:
				parts.append(line)
			data.append({"hypernets":hypernets,"addr":parts})
	return data

def hasABBA(string):
	for i in range(0,len(string)):
		tmp = string[i:i+2]
		tmp += tmp[::-1]
		if len(tmp) < 4 or tmp[0] == tmp[1]:
			continue
		if string[i:i+4] == tmp:
			return True
	return False


def nrSupportTLS(data):
	nrABBA = 0
	for item in data:
		abba = False
		for net in item["hypernets"]:
			abba = abba or hasABBA(net)
		if not abba:
			for a in item["addr"]:
				if hasABBA(a):
					nrABBA += 1
					break				
	return nrABBA

def main():
	if len(sys.argv) < 2:
		print "Usage: {} FILE".format(sys.argv[0])

	print nrSupportTLS(getData(sys.argv[1]))
	return 0

if __name__ == '__main__':
	main()