#!/usr/bin/env python

import sys
import md5
import signal
import threading
from random import randint

password = [None]*8
lock = threading.Lock()
class myThread (threading.Thread):
	def __init__(self, _threadID, _name, _startVal, _increment, _code):
		threading.Thread.__init__(self)
		self.threadID	= _threadID
		self.name		= _name
		self.startVal	= _startVal
		self.increment	= _increment
		self.code		= _code
		self.digest		= md5.new()
		
	def run(self):
		global password
		global lock
		i=self.startVal;
		while None in password:
			self.digest.update(self.code + str(i))
			hash = self.digest.hexdigest()
			if hash[:5] == '00000':
				index = hash[5]
				if index not in "01234567":
					continue
				lock.acquire()
				if password[int(index)] == None:
					password[int(index)] = hash[6]
				sys.stdout.write("\r")
				for c in password:
					if c == None:
						c = "_"
					sys.stdout.write(" " + c)
				lock.release()
			i += self.increment

def signalHandler(signo, frame):
	print "\033[F\033[2KTERMINATED\n\033[2K"
	sys.exit(1)

def main():
	signal.signal(signal.SIGINT,signalHandler)
	if len(sys.argv) > 2:
		print "Usage: {} STRING".format(sys.argv[0])
		sys.exit(1)
	
	for c in password:
		if c == None:
			c = "_"
		sys.stdout.write(" " + c)

	threads = []
	nrThreads = 512
	for i in range(0,nrThreads):
		threads.append(myThread(i+1,"Thread-"+str(i+1),i,nrThreads,sys.argv[1]))
		threads[i].start()

	for t in threads:
		t.join()
	return 0

if __name__ == '__main__':
	main()
