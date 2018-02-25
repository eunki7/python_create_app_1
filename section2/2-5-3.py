from bs4 import BeautifulSoup
html = """
<html><body>
  <ul>
    <li><a href="http://www.naver.com">naver</a></li>
    <li><a href="http://www.daum.net">daum</a></li>
    <li><a href="https://www.google.com">google</a></li>
    <li><a href="https://www.tistory.com">tistory</a></li>
  </ul>
</body></html>
"""
soup = BeautifulSoup(html, 'html.parser')
print('prettify',soup.prettify())
a = soup.find_all("a", string="daum")
b = soup.find_all(string=["naver", "daum"])
c = soup.find_all("a", limit=2)
print('a',a)
print('b',b)
print('c',c)
links = soup.find_all("a")
print('links',links)
# 출력
for a in links:
    print('a',type(a),a)
    href = a.attrs['href']
    text = a.string
    print(text, ">", href)
