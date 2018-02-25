from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

base = "https://www.inflearn.com/"
quote = rep.quote_plus("추천-강좌")
url = base + quote
res = req.urlopen(url).read()
soup = BeautifulSoup(res, "html.parser")

recommand = soup.select("ul.slides")[0]

for i,e in enumerate(recommand,1):
    print(i,e.select_one("h4.block_title > a").string)
