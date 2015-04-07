
from time import sleep as sleep
import sys
blue = "00274C"
maize = "FFCB05"
length = 20
cols = 30
delay = 0
while True:
	for i in range(length):
		for j in range(cols):
			print 0,
			print i,
			print j,
			if i % 2 == 0:
				print blue
			else:
				print maize
			sys.stdout.flush()
			#sleep(100 / 1000)


#	print delay,
#	print 0,
	#print k,
	#print blue
	#sys.stdout.flush()
	#sleep(delay / 100) 
#
	#print delay,
	#print 0,
	#print l,
	#print maize
	#sys.stdout.flush()
	#sleep(delay / 100) 

#	i = (i + 1) % length
#	j = (j + 1) % length
#	k = (k + 3) % length
#	l = (l - 4) % length
