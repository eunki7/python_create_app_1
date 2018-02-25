from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

fp = open("food-list.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

print("1",soup.select_one("li:nth-of-type(8)").string)
print("2",soup.select_one("#fd-list > li:nth-of-type(4)").string)
print("3",soup.select("#ac-list > li[data-lo='ko']")[1].string) 
print("4",soup.select("#fd-list > li.food.hot")[1].string)

cond1 = {"data-lo":"jp", "class":"food"}
cond2 = {"data-lo":"ko", "class":"alcohol"}

print("5",soup.find("li", cond1).string)

print("6",soup.find(id="ac-list")
           .find("li", cond2).string)

for ac in soup.find_all("li"):
    if ac['data-lo'] == 'us':
        print('data-lo == us',ac.string)
