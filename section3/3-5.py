import sys
import io
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#요청 URL
URL = 'https://www.wishket.com/accounts/login/'

#Fake User-Agent 생성
ua = UserAgent()

#print(ua.ie)
#print(ua.chrome)
#print(ua.random)

with requests.Session() as s:
    #URL연결
    s.get(URL)
    #Login 정보 Payload
    LOGIN_INFO = {
        'identification': '아이디',
        'password': '비밀번호',
        'csrfmiddlewaretoken': s.cookies['csrftoken']
    }
    #요청
    response = s.post(URL,data=LOGIN_INFO,headers={'User-Agent':str(ua.chrome), 'Referer':'https://www.wishket.com/accounts/login/'})
    #HTML 결과 확인
    #print('response',response.text)
    if response.status_code == 200 and response.ok:
        soup = BeautifulSoup(response.text,'html.parser')
        projectList = soup.select("table.table-responsive > tbody > tr")
        for i in projectList:
            print(i.find('th').string,i.find('td').text)