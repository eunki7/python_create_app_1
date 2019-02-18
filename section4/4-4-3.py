import urllib.request as req
import os.path, random
import simplejson as json

#URL
url = "https://api.github.com/repositories"

#경로 & 파일명
savename = "c:/section4/repo.json"

if not os.path.exists(url):
    req.urlretrieve(url, savename)

items = json.load(open(savename, "r", encoding="utf-8"))
#items = json.loads(open(savename, "r", encoding="utf-8").read())

# 출력
for item in items:
    print(item["full_name"] + " - " + item["owner"]["url"])