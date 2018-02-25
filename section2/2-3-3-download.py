import urllib.request
import urllib.parse
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

API = "http://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"

values = {
    'ctxCd': '1001'
}
params = urllib.parse.urlencode(values)

url = API + "?" + params
print("url=", url)

data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)
