import requests
from bs4 import BeautifulSoup
import urllib.parse as rep
import urllib.request as req
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


# 로그인 유저정보
LOGIN_INFO = {
    'log': '아이디',
    'pwd': '비밀번호',
    'user-submit': rep.quote_plus("로그인"),
    'user-cookie':1
}

# Session 생성, with 구문 안에서 유지
with requests.Session() as s:

    login_req = s.post('https://www.inflearn.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.inflearn.com%2F', data=LOGIN_INFO)
    # HTML 소스 확인
    #print('login_req',login_req.text)
    # HTTP Header 확인
    #print('login_req',login_req.headers)

    # Response 정상 확인
    if login_req.status_code == 200 and login_req.ok:
        #권한이 필요한 게시판 게시글 가져오기
        post_one = s.get('https://www.inflearn.com/members/outsider7224/')
        #예외 발생
        post_one.raise_for_status()
        #print(post_one.text)
        #BeautifulSoup 선언
        soup = BeautifulSoup(post_one.text,'html.parser')
        #print(soup.prettify())
        badges = soup.select("div.badges > ul > li > a > img")
        #이미지 쓰기(Badges)
        for i,z in enumerate(badges,1):
            fullFileName = os.path.join("c:/", str(i)+'.jpg')
            req.urlretrieve(z['src'],fullFileName)
