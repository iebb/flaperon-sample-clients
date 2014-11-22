Windows sample client in Python 2.7, with nothing but streaming.

Need unicurses lib to work.

change config.json to use. strings MUST be QUOTED!

## RESOLUTION
### resolution used in avconv
e.g. : "640x480"
You can use 320x240, 640x480, 800x600, 1600x1200, or ANY RESOLUTION you want!

## SERVER_ADDR
### Flaperon server address. used for communicating.
e.g. : "127.0.0.1", "localhost"

## BROADCAST_ID
### predefined broadcast ID in Flaperon server. used for communicating.
e.g. : "1","2"

## STREAM_NAME
### predefined stream name in Flaperon server.
e.g. : "broadcast"
rtmp://SERVER_ADDR:1935/live/STREAM_NAME will be the final rtmp URL.
