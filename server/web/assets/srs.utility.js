function padding(t,e,a){return(t+"").length>=e?t+"":padding(a+t,e,a)}function parse_query_string(){var t={}
t.host=window.location.host,t.hostname=window.location.hostname,t.http_port=""==window.location.port?80:window.location.port,t.pathname=window.location.pathname,t.pathname.lastIndexOf("/")<=0?(t.dir="/",t.filename=""):(t.dir=t.pathname.substr(0,t.pathname.lastIndexOf("/")),t.filename=t.pathname.substr(t.pathname.lastIndexOf("/"))),t.user_query={}
var e=(window.location.search+"").replace(" ","").split("?")[1]
if(void 0==e)return t
var a=e.split("&")
return $(a).each(function(){var e=this.split("=")
t[e[0]]=e[1],t.user_query[e[0]]=e[1]}),t}function srs_parse_rtmp_url(t){var e=document.createElement("a")
e.href=t.replace("rtmp://","http://")
var a=e.hostname,n=""==e.port?"1935":e.port,r=e.pathname.substr(1,e.pathname.lastIndexOf("/")-1),s=e.pathname.substr(e.pathname.lastIndexOf("/")+1)
if(r=r.replace("...vhost...","?vhost="),r.indexOf("?")>=0){var o=r.substr(r.indexOf("?"))
r=r.substr(0,r.indexOf("?")),o.indexOf("vhost=")>0&&(a=o.substr(o.indexOf("vhost=")+"vhost=".length),a.indexOf("&")>0&&(a=a.substr(0,a.indexOf("&"))))}var i={server:e.hostname,port:n,vhost:a,app:r,stream:s}
return i}