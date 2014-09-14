'''
	Job fetcher
	by Jeb <1@wa.vg> 2014-09-10
'''
import os
import urllib
import urllib2
import time 
import json
JOB_URL="http://192.168.1.233/api/get.php?server=0"
START='./test'
from threading import Thread    
running = False
def start(args):
	global running,START
	running = True
	print time.time()
	f = os.popen(START)
	print f.read()
	print time.time()
	running = False
    
while 1:
	req = urllib2.urlopen(urllib2.Request(JOB_URL))
	j = req.read()
	if 'START' in j:
		t1 = Thread(target=start,args=(5,))
		t1.start()
	if 'STOP' in j:
		t1 = Thread(target=start,args=(5,))
		t1.stop()
	print j
	time.sleep(5)
t2 = Thread(target=watchdog,args=(5,))
t2.start() 
print running