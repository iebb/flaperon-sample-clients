'''
	Client - Fetch Job / Run Job / Submit Result
	by Jeb <1@wa.vg> 2014-09-18
'''
import os
import urllib
import urllib2
import time 
import json
JOB_URL="http://192.168.1.233/api/get.php?server=0"
CLEAR_URL="http://192.168.1.233/api/done.php?server=0"
from threading import Thread    
running = {}
def start(k):
	global running
	id=int(k['id'])
	try:
		if running[id] == True: 
			print 'Err: job is doing'
			return False
	except:
		pass
	running[id] = True
	print '======================================='
	if os.path.isfile(k['command']):
		f = os.popen('./'+k['command'])
		data = f.read()
		try:
			x=json.loads(data)
			try:
				u=x['value']
			except:
				u=0
			print 'command id:',k['id']
			print 'value:',u
			print 'raw:',data
		except:
			print 'no valid format detected'
	else:
		print 'Err: no file named',k['command'],'found'
	print '======================================='
	running[id] = False
	return True
    
while 1:
	req = urllib2.urlopen(urllib2.Request(JOB_URL))
	j = req.read()
	k = json.loads(j)
	print running
	if k:
		if start(k):
			req = urllib2.urlopen(urllib2.Request(CLEAR_URL))
			print 'sleeping',k['interval'],'milliseconds'
			time.sleep(0.001*float(k['interval']))
		else:
			print 'Cannot Start?'
	else:
		print 'No job, wait 5 seconds'
		time.sleep(5) # to avoid super-fast requests
	time.sleep(0.1) # to avoid super-fast requests
	print j