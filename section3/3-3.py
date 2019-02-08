import sys
import io
import requests, json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# Rest API GET, POST, DELETE, PUT:UPDATE, REPLACE (FETCH : UPDATE, MODIFY)
# https://jsonplaceholder.typicode.com/posts

r = requests.get('https://api.github.com/events')
r.raise_for_status()
print(r.text)

jar = requests.cookies.RequestsCookieJar()
jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')

r = requests.get('http://httpbin.org/cookies', cookies=jar)

print(r.text)
print(r.cookies)

r = requests.get('https://github.com', timeout=5)
print(r.text)

r = requests.post('http://httpbin.org/post', data={'kim': 'stellar'}, cookies=jar)
print(r.text)
print(r.headers)

payload = {'key1': 'value1', 'key2': 'value2'}
payload = (('key1', 'value1'), ('key1', 'value2'))

r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)

url = 'http://httpbin.org/post'
payload = {'some': 'data'}

r = requests.post(url, data=json.dumps(payload))
print(r.text)

r = requests.put('http://httpbin.org/put', data={'key': 'value'})
print(r.text)

r = requests.delete('http://httpbin.org/delete')
print(r.text)

payload = (('key1', 'value1'), ('key1', 'value2'))
r = requests.put('https://jsonplaceholder.typicode.com/posts/1', data=payload)
print(r.text)

r = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
print(r.text)

r = requests.get('https://jsonplaceholder.typicode.com/albums')
print(r.text)
