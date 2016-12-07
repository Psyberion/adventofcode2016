#!/usr/bin/env python

import sys
import md5
import signal
from random import randint

def signalHandler(signo, frame):
	print "\033[F\033[2KTERMINATED\n\033[2K"
	sys.exit(1)

def getPassword(door,animate):
	password = ["_"]*8
	h4xx0r = "*+\\/#-_"
	i=0;
	while "_" in password:
		tmp = door + str(i)
		m = md5.new()
		m.update(tmp)
		hash = m.hexdigest()
		if hash[:5] == '00000':
			index = hash[5]
			if index not in "01234567":
				continue
			if password[int(index)] == "_":
				password[int(index)] = hash[6]
		i += 1
		if not animate:
			continue
		print "Testing hash: {}".format(tmp)
		sys.stdout.write("PASSWORD:")
		for c in password:
			if c == "_":
				c = h4xx0r[randint(0,6)]
			sys.stdout.write(" (" + c + ")")
		sys.stdout.write("\033[F\r")
	return ''.join(password)


def main():
	signal.signal(signal.SIGINT,signalHandler)
	if len(sys.argv) > 2:
		print "Usage: {} STRING".format(sys.argv[0])
		sys.exit(1)
	print getPassword(sys.argv[1],False)

if __name__ == '__main__':
	main()
