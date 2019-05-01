import urllib
import urllib2
import time
import datetime
from hashlib import sha512

url = "http://wargame.kr:8080/pyc_decompile/"
opener = urllib2.build_opener(urllib2.HTTPHandler)
request = urllib2.Request(url)
request.add_header(
    'User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36')
request.add_header(
    'Cookie', 'PHPSESSID=v49q7ovgd3dh0bbu5dotlauac0; chat_id=zairo')
request.get_method = lambda: 'GET'
response = opener.open(request)
response = str(response.read())

server_time = response[response.find('<h1>')+4:response.find('</h1>')]
server_time = datetime.datetime.strptime(server_time, '%Y/%m/%d %H:%M:%S')

seed = server_time.strftime('%m/%d/HJEJSH')
hs = sha512(seed).hexdigest()
start = server_time.hour % 3 + 1
end = start * (server_time.minute % 30 + 10)
ok = hs[start:end]

url = "http://wargame.kr:8080/pyc_decompile/?flag="+ok
opener = urllib2.build_opener(urllib2.HTTPHandler)
request = urllib2.Request(url)
request.add_header(
    'User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36')
request.add_header(
    'Cookie', 'PHPSESSID=v49q7ovgd3dh0bbu5dotlauac0; chat_id=zairo')
request.get_method = lambda: 'GET'
response = opener.open(request)
response = str(response.read())

print(response)
