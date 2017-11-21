#!/usr/bin/env python

import sys
import md5

def getPassword(door):
	password = ""
	i=0;
	while len(password) < 8:
		tmp = door + str(i)
		m = md5.new()
		m.update(tmp)
		hash = m.hexdigest()
		if hash[:5] == '00000':
			password += hash[5]
		i += 1
	return password


def main():
	if len(sys.argv) > 2:
		print "Usage: {} STRING".format(sys.argv[0])
		sys.exit(1)
	print getPassword(sys.argv[1])

if __name__ == '__main__':
	main()
