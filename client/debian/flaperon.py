'''
	A Simple Python Client for Flaperon System
	by Jeb <1@wa.vg> 
	2014-09-10 v1
	2014-09-18 v1.4
	2014-10-12 v1.41
	2014-10-16 v1.414
	2014-11-11 v2
'''
import thread
import os
import urllib
import urllib2
import time 
import json
import curses
import re


# -----modify this part------
SERVER_ADDR="10.1.2.177"
STREAM_NAME="pH"
BROADCAST_ID="2"
RESOLUTION="640x480"
FPS="12"
DEVICE="/dev/video0"
# -----end-----

STREAM_URL="rtmp://"+SERVER_ADDR+":1935/live/"+STREAM_NAME

stdscr = curses.initscr()
curses.start_color()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)




def listen():
	stdscr.addstr(9,10, 'Thread LISTEN Started!',  curses.color_pair(1))
	GET_URL="http://"+SERVER_ADDR+"/web/getcommand.php?r="+BROADCAST_ID
	DONE_URL="http://"+SERVER_ADDR+"/web/donecommand.php?r="+BROADCAST_ID+"&data="
	COUNT_PROCESSED=0
	COUNT_QUEUED=0
	while 1:
		try:
			req = urllib2.urlopen(urllib2.Request(GET_URL), data=None, timeout=3)
			j = req.read()
			k = json.loads(j)
			stdscr.addstr(17,0, "Commands Processed: "+str(COUNT_PROCESSED) + " / Queued: "+str(len(k))+"          ",  curses.color_pair(2))
			if len(k)>0:
				COUNT_PROCESSED += 1
				k1 = k[0]
				f = os.popen('./'+k1['command'])
				data = f.read()
				stdscr.addstr(9,10, data,  curses.color_pair(2))
				DONE_SURL=DONE_URL+urllib.quote(data)+"&id="+k1['id']
				#print DONE_SURL
				_req = urllib2.urlopen(urllib2.Request(DONE_SURL), data=None, timeout=3)
				_ = _req.read()
		except:
			pass
		time.sleep(1)
	
def getdata():
	stdscr.addstr(10,10, 'Thread GETDATA Started!',  curses.color_pair(1))
	SEND_URL="http://"+SERVER_ADDR+"/web/senddata.php?r="+BROADCAST_ID+"&data="
	while 1:
		try:
			f = os.popen('./GETDATA')
			data = f.read()
			stdscr.addstr(10,10, data,  curses.color_pair(2))
			stdscr.refresh()
			SURL=SEND_URL+urllib.quote(data)
			req = urllib2.urlopen(urllib2.Request(SURL), data=None, timeout=3)
			j = req.read()
			time.sleep(1)
			#print j
		except:
			pass
	
def streaming():
	global COUNT_DROPS,COUNT_FRAMES,DPR
	stdscr.addstr(11,10, 'Thread STREAMING Started!',  curses.color_pair(1))
	while 1:
		COUNT_DROPS=0
		COUNT_FRAMES=1
		DPR = 0
		r1 = re.compile(r'drop=(\d+)')
		r2 = re.compile(r'frame=\s*(\d+)')
		try:
			flag = 1
			os.popen3('killall avconv')
			f1,f2,f = os.popen3('avconv -r '+FPS+' -f video4linux2 -s '+RESOLUTION+' -i '+DEVICE+' -f flv '+STREAM_URL)
			v=u=''
			while flag:
				k=u+f.read(256).replace('\r','\n')
				if not k:
					break
				lines = k.split('\n')
				for k0 in lines:
					if len(k0)>10:
						v=u
						ouv = v[:80]
						ouv = ouv + " "*(80-len(ouv))
						stdscr.addstr(11,10, ouv,  curses.color_pair(2))
						_=r1.findall(v)
						if len(_):
							COUNT_DROPS=int(_[0])
							if (COUNT_DROPS>200):
								flag = 0
						_=r2.findall(v)
						if len(_):
							COUNT_FRAMES=int(_[0])+COUNT_DROPS
							DPR = 100.0 * COUNT_DROPS / COUNT_FRAMES
							stdscr.addstr(16,0, "Video: frames: "+str(COUNT_FRAMES) + " / drops: "+str(COUNT_DROPS) + " / dropping rate: "+("%.4f %%" % DPR),  curses.color_pair(2))
						stdscr.refresh()
						u=k0
		except:
			pass

start_time = time.time()
thread.start_new_thread(getdata,())
thread.start_new_thread(streaming,())
thread.start_new_thread(listen,())

stdscr.addstr(0,0, "+-------------------------------------------------+",  curses.color_pair(1))
stdscr.addstr(1,0, "|        Flaperon Daemon v2.0     b20141111       |",  curses.color_pair(1))
stdscr.addstr(2,0, "+-------------------------------------------------+",  curses.color_pair(1))

stdscr.addstr(3,0, ">>> Server Address: "+str(SERVER_ADDR),  curses.color_pair(3))
stdscr.addstr(4,0, ">>> Screen Resolution: "+str(RESOLUTION),  curses.color_pair(3))
stdscr.addstr(5,0, ">>> RTMP Stream: "+str(STREAM_URL),  curses.color_pair(3))
stdscr.addstr(6,0, ">>> Video Device: "+str(DEVICE),  curses.color_pair(3))
stdscr.addstr(7,0, ">>> Broadcast ID: "+str(BROADCAST_ID),  curses.color_pair(3))

stdscr.addstr(9,0, "Commands :",  curses.color_pair(1))
stdscr.addstr(10,0, "Data     :",  curses.color_pair(1))
stdscr.addstr(11,0, "Streaming:",  curses.color_pair(1))


stdscr.addstr(13,0, "Flaperon System is Up for ",  curses.color_pair(3))
stdscr.addstr(15,0, "\n",  curses.color_pair(1))
stdscr.refresh()
while 1:
	diff = time.time()-start_time
	stdscr.addstr(13,27, "%d days, %d hours, %d minutes and %.3f seconds            " % (int(diff/86400),(int(diff)%86400)/3600 ,(int(diff)%3600)/60 ,diff - int(diff/60)*60),  curses.color_pair(2))
	stdscr.refresh()
	time.sleep(1)