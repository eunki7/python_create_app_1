from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# HTML 가져오기
base = "https://search.naver.com/search.naver?where=image&query="
quote = rep.quote_plus("사자")
url = base + quote

res = req.urlopen(url)
savePath ="C:\\imagedown\\"
try:
    if not(os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("Failed to create directory!!!!!")
        raise

soup = BeautifulSoup(res, "html.parser")

li_list = soup.select("div.img_area._item > a.thumb._thumb > img")
for i, div in enumerate(li_list,1):
  print("div =", div['data-source'])
  fullfilename = os.path.join(savePath, savePath+str(i)+'.jpg')
  print(fullfilename)
  req.urlretrieve(div['data-source'],fullfilename)
  print(i)
