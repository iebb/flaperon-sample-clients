'''
	Broadcast Client for pcDuino / other ubuntu systems
	by Jeb <1@wa.vg> 2014-09-10
'''
STREAM_URL="rtmp://192.168.1.233:1935/live/stream1" # url prefix for streaming
REPORT_URL="http://192.168.1.233/api/update.php?r=0&c=" # url prefix for status report
import os,urllib,urllib2
os.system('killall avconv')
f1,f2,f = os.popen3('avconv -f video4linux2 -s 800x600 -i /dev/video0 -c:a copy -f flv '+STREAM_URL)
v=u=''
while 1:
	k=u+f.read(256).replace('\r','\n')
	if not k:
		break
	lines = k.split('\n')
	for k0 in lines:
		if len(k0)>10:
			v=u
			u=k0
	url = REPORT_URL+urllib.quote(v)
	req = urllib2.urlopen(urllib2.Request(url))