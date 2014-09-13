#!/bin/bash
git clone https://github.com/winlinvip/simple-rtmp-server
cd simple-rtmp-server/trunk
./configure && make
mv ./objs/srs /bin/srs
mkdir /var/srs/
mv ./conf/srs.conf /var/srs/srs.conf
srs -c /var/srs/srs.conf