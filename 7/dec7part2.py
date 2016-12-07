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

def hasABA(supernets,hypernets):
	for sNet in supernets:
		for i in range(0,len(sNet)):
			aba = sNet[i:i+2]
			aba += aba[0]
			bab = aba[1]+aba[0]+aba[1]
			if len(aba) < 3 or aba[0] == aba[1]:
				continue
			if sNet[i:i+3] == aba:
				for hNet in hypernets:
					if bab in hNet:
						return True
	return False


def nrSupportSSL(data):
	nrABA = 0
	for item in data:
		if hasABA(item["addr"],item["hypernets"]):
			nrABA += 1
	return nrABA

def main():
	if len(sys.argv) < 2:
		print "Usage: {} FILE".format(sys.argv[0])

	print nrSupportSSL(getData(sys.argv[1]))
	return 0

if __name__ == '__main__':
	main()