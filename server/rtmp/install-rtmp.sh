#!/bin/sh
sudo apt-get install build-essential libpcre3 libpcre3-dev libssl-dev
wget http://nginx.org/download/nginx-1.5.2.tar.gz
wget https://github.com/arut/nginx-rtmp-module/archive/master.zip
tar -zxvf nginx-1.5.2.tar.gz
unzip master.zip
cd nginx-1.5.2
./configure --with-http_ssl_module --add-module=../nginx-rtmp-module-master
make
sudo make install
rm /etc/init.d/nginx
mv ./nginx /etc/init.d/nginx
rm /usr/local/nginx/conf/nginx.conf
mv ./nginx.conf /usr/local/nginx/conf/nginx.conf