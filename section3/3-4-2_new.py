# 2019-05-06
# 3-4-2.py 예제 수정
# 로그인 처리 후 -> 개인 대시보드 정보 출력

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
    'email': '본인 아이디(인프런)',
    'password': '본안 비번(인프런)'
}

# Session 생성, with 구문 안에서 유지
with requests.Session() as s:

    login_req = s.post('https://www.inflearn.com/api/signin', data=LOGIN_INFO)
    # HTML 소스 확인
    # print('login_req'.format(login_req.text))
    # HTTP Header 확인
    # print('login_req'.format(login_req.headers))

    # Response 정상 확인
    if login_req.status_code == 200 and login_req.ok:
        # 인프런 개인 대시보드 정보 확인하기
        
        # URL 확인
        # URL 부분의 숫자 부분은 본인의 대시보드 URL 확인 후 수정 한다.
        # 예) https://www.inflearn.com/users/40769/dashboard
        dash_info = s.get('https://www.inflearn.com/users/숫자/dashboard')
        
        # 수신 에러시 예외 발생
        dash_info.raise_for_status()
        
        # 수신 확인
        # print(dash_info.text)
        
        #BeautifulSoup 선언
        soup = BeautifulSoup(dash_info.text,'html.parser')
        
        # 수신 HTML 정리
        # print(soup.prettify())

        statistics = soup.select("div.box.statistics > div.box_content > div > div")
        
        # 확인
        # print(statistics)

        for v in statistics:
            print()
            # 레이블 명
            lable = v.find('div', class_="status_label").text.strip()
            # 통계
            status = v.find('div', class_="status_value").text.strip()
            # 출력
            print('{} : {}'.format(lable, status))