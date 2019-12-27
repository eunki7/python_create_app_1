from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import os
import sys
import io
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

savePath ="C:\\imagedown\\"
url = "https://www.inflearn.com/courses"

res = req.urlopen(url).read()

soup = BeautifulSoup(res,"html.parser")

recommand = soup.select("div.course_card_item")

try:
    if not(os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("Failed to create directory!!!!!")
        raise


for i,e in enumerate(recommand,1):
    with open(savePath+"title_"+str(i)+".txt", "wt") as f:
        f.write(e.select_one("div.course_title").string)
    fullfilename = os.path.join(savePath, savePath+'img_'+str(i)+'.png')
    time.sleep(0.5)
    req.urlretrieve('https://cdn.inflearn.com/' + req.quote(e.select_one("figure.is_thumbnail > img")['src'][25:]),fullfilename)

print("강좌 정보 텍스트 출력 및 이미지 다운 완료!")
