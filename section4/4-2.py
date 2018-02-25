from bs4 import BeautifulSoup
import urllib.request as req
import os.path
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
savename = "C:/section4/forecast.xml"
if not os.path.exists(savename):
    req.urlretrieve(url, savename)

# BeautifulSoup로 분석하기
xml = open(savename, "r", encoding="utf-8").read()
soup = BeautifulSoup(xml, 'html.parser')

# 지역 확인
info = {}
for location in soup.find_all("location"):
    loc = location.find('city').string
    weather = location.find_all('tmn')
    #print(weather)
    if not (loc in info):
        info[loc] = []
    for tmn in weather:
        info[loc].append(tmn.string)

#print(info)

# 각 지역의 날씨 출력
with open('C:/section4/forecast.txt', "wt", encoding="utf-8") as f:
    for loc in sorted(info.keys()):
        print("+", loc)
        f.write(str(loc)+'\n')
        for name in info[loc]:
            print(" - ", name)
            f.write('\t'+str(name)+'\n')
