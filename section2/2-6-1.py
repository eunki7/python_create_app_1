from bs4 import BeautifulSoup
import re
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html><body>
  <ul>
    <li id="naver"><a href="http://www.naver.com">naver</a></li>
    <li><a href="http://www.daum.net">daum</a></li>
    <li><a href="https://www.google.com">google</a></li>
    <li><a href="https://www.tistory.com">tistory</a></li>
  </ul>
</body></html>
"""
soup = BeautifulSoup(html, "html.parser")
naver = soup.find(id="naver")
print("id:naver >> " + naver.string)

li = soup.find_all(href=re.compile(r"^https://"))
for e in li:
    print(e.attrs['href'])
