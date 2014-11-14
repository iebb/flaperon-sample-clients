'''
	A Simple Python Client for Flaperon System
	by Jeb <1@wa.vg> 
	2014-09-10 v1
	2014-09-18 v1.4
	2014-10-12 v1.41
	2014-10-16 v1.414
	2014-11-11 v2
	2014-11-12 v2 Windows Port
'''
import thread
import os
import urllib
import urllib2
import time 
import json
import unicurses
import re
from unicurses import *
# -----modify this part------
SERVER_ADDR="10.1.2.177"
STREAM_NAME="test"
BROADCAST_ID="1"
RESOLUTION="320x240"
# -----end-----

STREAM_URL="rtmp://"+SERVER_ADDR+":1935/live/"+STREAM_NAME
VIDEO_DEVICE="dummy"
VIDEO_DEVICES=[]
try:
	x,y,z=os.popen3("avconv.exe -f dshow -list_devices true -i dummy")
	d = z.read()
	k = d.find("DirectShow video devices")
	l = d.find("DirectShow audio devices")
	d = d[k:l]
	u = d.split('\n')[1:-1]
	for i in u:
		i=i.split('"')[1]
		VIDEO_DEVICES.append(i)
except:
	pass
if len(VIDEO_DEVICES):
	WIDTH = 30
	HEIGHT = 10
	startx = 0
	starty = 0

	choices = VIDEO_DEVICES
	n_choices = len(choices)

	choice = chosen = 1
	c = 0
			
	def print_menu(menu_win, highlight):
		x = 2
		y = 2
		for i in range(0, n_choices):
			if (highlight == i + 1):
				wattron(menu_win, A_REVERSE)
				mvwaddstr(menu_win, y, x, choices[i])
				wattroff(menu_win, A_REVERSE)
			else:
				mvwaddstr(menu_win, y, x, choices[i])
			y += 1
		wrefresh(menu_win)

	def report_choice(mouse_x, mouse_y):
		i = startx + 2
		j = starty + 3
		for choice in range(0, n_choices):
			if (mouse_y == j + choice) and (mouse_x >= i) and (mouse_x <= i + len(choices[choice])):
				return choice + 1
				break

	stdscr = unicurses.initscr()
	clear()
	noecho()
	cbreak()
	curs_set(0)
	startx = int((80 - WIDTH) / 2)
	starty = int((24 - HEIGHT) / 2)

	menu_win = newwin(HEIGHT, WIDTH, starty, startx)
	keypad(menu_win, True)
	refresh()
	print_menu(menu_win, 1)
	mouseinterval(0)
	mousemask(ALL_MOUSE_EVENTS)

	while True:
		c = wgetch(menu_win)
		
		if c == KEY_UP:
			if choice == 1:
				choice = n_choices
			else:
				choice -= 1
			chosen = choice
			print_menu(menu_win, chosen)
		elif c == KEY_DOWN:
			if choice == n_choices:
				choice = 1
			else:
				choice += 1
			chosen = choice
			print_menu(menu_win, chosen)
		elif c == 10:
			VIDEO_DEVICE=VIDEO_DEVICES[choice-1]
			break
		elif c == KEY_MOUSE:
			id, x, y, z, bstate = getmouse()
			if bstate & BUTTON1_PRESSED:
				choice = chosen = report_choice(x + 1, y + 1)
				refresh()
				print_menu(menu_win, chosen)

	endwin()

unicurses.start_color()
unicurses.init_pair(1, 8+unicurses.COLOR_GREEN, unicurses.COLOR_BLACK)
unicurses.init_pair(2, 8+unicurses.COLOR_CYAN, unicurses.COLOR_BLACK)
unicurses.init_pair(3, 8+unicurses.COLOR_RED, unicurses.COLOR_BLACK)




def listen():
	mvaddstr(9,10, 'Thread LISTEN Started!',  unicurses.color_pair(2))
	'''
	GET_URL="http://"+SERVER_ADDR+"/web/getcommand.php?r="+BROADCAST_ID
	DONE_URL="http://"+SERVER_ADDR+"/web/donecommand.php?r="+BROADCAST_ID+"&data="
	COUNT_PROCESSED=0
	COUNT_QUEUED=0
	while 1:
		try:
			req = urllib2.urlopen(urllib2.Request(GET_URL), data=None, timeout=3)
			j = req.read()
			k = json.loads(j)
			mvaddstr(17,0, "Commands Processed: "+str(COUNT_PROCESSED) + " / Queued: "+str(len(k))+"		  ",  unicurses.color_pair(2))
			if len(k)>0:
				COUNT_PROCESSED += 1
				k1 = k[0]
				f = os.popen('./'+k1['command'])
				data = f.read()
				mvaddstr(9,10, data,  unicurses.color_pair(2))
				DONE_SURL=DONE_URL+urllib.quote(data)+"&id="+k1['id']
				#print DONE_SURL
				_req = urllib2.urlopen(urllib2.Request(DONE_SURL), data=None, timeout=3)
				_ = _req.read()
		except:
			pass
		time.sleep(1)
	'''
	
def getdata():
	mvaddstr(10,10, 'Thread GETDATA Started!',  unicurses.color_pair(2))
	'''
	SEND_URL="http://"+SERVER_ADDR+"/web/senddata.php?r="+BROADCAST_ID+"&data="
	while 1:
		try:
			f = os.popen('./GETDATA')
			data = f.read()
			mvaddstr(10,10, data,  unicurses.color_pair(2))
			SURL=SEND_URL+urllib.quote(data)
			req = urllib2.urlopen(urllib2.Request(SURL), data=None, timeout=3)
			j = req.read()
			time.sleep(1)
			#print j
		except:
			pass
	'''
	
def streaming():
	global COUNT_DROPS,COUNT_FRAMES,DPR,VIDEO_DEVICE,choice
	mvaddstr(11,10, 'Thread STREAMING Started!',  unicurses.color_pair(2))
	cmd = 'avconv.exe -f dshow -s '+RESOLUTION+' -i video="'+VIDEO_DEVICE+'" -f flv "'+STREAM_URL+'"'
	mvaddstr(23,0, cmd,  unicurses.color_pair(2))
	
	while 1:
		COUNT_DROPS=0
		COUNT_FRAMES=1
		DPR = 0
		r1 = re.compile(r'drop=(\d+)')
		r2 = re.compile(r'frame=\s*(\d+)')
		try:
			flag = 1
			a,b,c = os.popen3('killall avconv')
			f1,f2,f = os.popen3(cmd)
			v=u=''
			while flag:
				k=u+f.read(256).replace('\r','\n')
				if not k:
					break
				lines = k.split('\n')
				for k0 in lines:
					if len(k0)>10:
						v=u
						mvaddstr(11,10, v[:70],  unicurses.color_pair(2))
						clrtoeol()
						_=r1.findall(v)
						if len(_):
							COUNT_DROPS=int(_[0])
							DPR = 100.0 * COUNT_DROPS / COUNT_FRAMES
							if (DPR>20):
								flag = 0
						_=r2.findall(v)
						if len(_):
							COUNT_FRAMES=int(_[0])+COUNT_DROPS
							DPR = 100.0 * COUNT_DROPS / COUNT_FRAMES
							mvaddstr(16,0, "Video: frames: "+str(COUNT_FRAMES) + " / drops: "+str(COUNT_DROPS) + " / dropping rate: "+("%.4f %%" % DPR),  unicurses.color_pair(2))
							clrtoeol()
						if 'Input/output error' in v:
							flag = 0
						u=k0
		except:
			pass
	

start_time = time.time()
thread.start_new_thread(getdata,())
thread.start_new_thread(streaming,())
thread.start_new_thread(listen,())

clear()
noecho()

mvaddstr(0,0, "+-------------------------------------------------+",  unicurses.color_pair(1))
mvaddstr(1,0, "|        Flaperon Daemon v2.0     b20141111       |",  unicurses.color_pair(1))
mvaddstr(2,0, "+-------------------------------------------------+",  unicurses.color_pair(1))

mvaddstr(3,0, ">>> Server Address: "+str(SERVER_ADDR),  unicurses.color_pair(3))
mvaddstr(4,0, ">>> Screen Resolution: "+str(RESOLUTION),  unicurses.color_pair(3))
mvaddstr(5,0, ">>> RTMP Stream: "+str(STREAM_URL),  unicurses.color_pair(3))
mvaddstr(6,0, ">>> Video Device: "+str(VIDEO_DEVICE),  unicurses.color_pair(3))
mvaddstr(7,0, ">>> Broadcast ID: "+str(BROADCAST_ID),  unicurses.color_pair(3))

mvaddstr(9,0, "Commands :",  unicurses.color_pair(1))
mvaddstr(10,0, "Data	 :",  unicurses.color_pair(1))
mvaddstr(11,0, "Streaming:",  unicurses.color_pair(1))


mvaddstr(13,0, "Flaperon System is Up for ",  unicurses.color_pair(3))
mvaddstr(15,0, "\n",  unicurses.color_pair(1))
refresh()
while 1:
	diff = time.time()-start_time
	mvaddstr(13,27, "%d days, %d hours, %d minutes and %.3f seconds" % (int(diff/86400),(int(diff)%86400)/3600 ,(int(diff)%3600)/60 ,diff - int(diff/60)*60),  unicurses.color_pair(2))
	clrtoeol()
	refresh()
	time.sleep(0.1)