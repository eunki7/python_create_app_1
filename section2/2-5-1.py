from urllib.parse import urljoin
baseUrl = "http://test.com/html/a.html"
print( urljoin(baseUrl, "b.html") )
print( urljoin(baseUrl, "sub/c.html") )
print( urljoin(baseUrl, "../index.html") )
print( urljoin(baseUrl, "../img/hoge.png") )
print( urljoin(baseUrl, "../css/hoge.css") )
