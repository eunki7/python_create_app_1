import urllib.request
from urllib.parse import urlparse
import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://www.encar.com/"

mem = urllib.request.urlopen(url)

print(type(mem))
print("geturl :",mem.geturl())
print("status :",mem.status)
print("headers :",mem.getheaders())
print("info :",mem.info(),"\n")
print("getcode :",mem.getcode())
print("read :",mem.read(10).decode('utf-8'))
print(urlparse('http://www.encar.co.kr?test=test').query)
