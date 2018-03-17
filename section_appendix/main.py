# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QUrl
from lib.extractWordLayout import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from bs4 import BeautifulSoup
import urllib.request as request
import urllib.error as err
import urllib.parse as parse
import datetime
import codecs
import time
import sys
import io
import os

#아래 코드는 Atom 에디터에서 실행시에 한글 검색 결과가 있는 삽입해야 함.
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        #초기화
        self.setupUi(self)
        #시그널 초기화
        self.initSignal()
        #초기 셋팅
        self.initSetting()

    #초기 셋팅
    def initSetting(self):
        self.swordEdit.setFocus(True)

    #시그널 초기화
    def initSignal(self):
        #시작 버튼 클릭 시
        self.startSearchWordButton.clicked.connect(self.extractWordStart)
        #초기화 버튼 클릭 시
        self.initButton.clicked.connect(self.initAllComponent)
        #종료 버튼 클릭 시
        self.exitButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        #엔터키 입력 시
        self.swordEdit.returnPressed.connect(self.extractWordStart)
        #검색어 리스트 클릭 시
        self.listWidget_3.itemClicked.connect(self.setTextFotWord)
        #검색어 리스트 더블 클릭 시
        self.listWidget_3.itemDoubleClicked.connect(self.extractWordStart)
        #검색어 리스트 더블 클릭 시
        self.listWidget_1.itemDoubleClicked.connect(self.extractWordStart2th)
        #검색어 리스트 더블 클릭 시
        self.listWidget_2.itemDoubleClicked.connect(self.extractWordAgain)
        #저장 버튼 클릭 시
        self.saveResultWord.clicked.connect(self.saveAllDataToText)


    #추출 시작
    def extractWordStart(self):

        #기본 URL(변동 가능성이 있으므로, 항시 확인)
        base_url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query="

        #텍스트 데이터 검색어 및 유효성 검사
        s_word = self.swordEdit.text().strip()
        if s_word is None or s_word == '' or not s_word:
            QMessageBox.about(self,"검색오류","검색어를 입력하세요.")
            self.swordEdit.setFocus(True)
            return None

        #한글 검색어 인코딩
        req_param = parse.quote_plus(s_word)
        #웹뷰 미리보기 로드
        self.webView.load(QUrl(base_url+req_param))
        #1차 검색어 결과 초기화
        self.listWidget_1.clear()
        #요청 및 예외처리
        try:
            conn = request.urlopen(base_url+req_param)
        except err.HTTPError as e:
            print('HTTPError: {}'.format(e.code))
        except err.URLError as e:
            print('URLError: {}'.format(e.reason))
        else:
            #print('Status Code : ',conn.getcode()) #상태코드
            soup = BeautifulSoup(conn.read(), "html.parser")
            for i,e in enumerate(soup.select("dd.lst_relate > ul > li"),1):
                self.listWidget_1.addItem(e.select_one('a').string)

        self.listWidget_3.addItem(s_word)

        #재 요청 시 초기화 작업
        self.swordEdit.clear()
        self.swordEdit.setFocus(True)

    #추출 시작(1차와 2차를 공통함수로 코딩할 수 있으나, 이해하기 쉽게 분리해서 작성한다.)
    def extractWordStart2th(self):
        #기본 URL(변동 가능성이 있으므로, 항시 확인)
        base_url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query="
        #텍스트 데이터 검색어 및 유효성 검사
        s_word = self.listWidget_1.currentItem().text().strip()
        #한글 검색어 인코딩
        req_param = parse.quote_plus(s_word)
        #웹뷰 미리보기 로드
        self.webView.load(QUrl(base_url+req_param))
        #1차 검색어 결과 초기화
        self.listWidget_2.clear()
        #요청 및 예외처리
        try:
            conn = request.urlopen(base_url+req_param)
        except err.HTTPError as e:
            print('HTTPError: {}'.format(e.code))
        except err.URLError as e:
            print('URLError: {}'.format(e.reason))
        else:
            print('Status Code : ',conn.getcode())
            soup = BeautifulSoup(conn.read(), "html.parser")
            for i,e in enumerate(soup.select("dd.lst_relate > ul > li"),1):
                self.listWidget_2.addItem(e.select_one('a').string)

        self.listWidget_3.addItem(s_word)

        #재 요청 시 초기화 작업
        self.swordEdit.clear()
        self.swordEdit.setFocus(True)

    #초기화 버튼 클릭 시
    def initAllComponent(self):
        self.swordEdit.clear()
        self.listWidget_1.clear()
        self.listWidget_2.clear()
        self.listWidget_3.clear()
        self.webView.load(QUrl('about:blank'))
        self.swordEdit.setFocus(True)

    #검색어 리스트 텍스트 클릭 시
    def setTextFotWord(self):
        #print('CurrentIdx : ',self.listWidget_3.currentRow()) #현재 인덱스
        self.swordEdit.setFocus(True)
        self.swordEdit.setText(self.listWidget_3.currentItem().text().strip())

    #2차 검색어에서 더블 클릭 후 재 실행 시
    def extractWordAgain(self):
        self.swordEdit.setText(self.listWidget_2.currentItem().text().strip())
        self.extractWordStart()

    #텍스트 파일 저장
    def saveAllDataToText(self):
        #저장 할 데이터가 없을 경우
        if self.listWidget_1.count() == 0 and self.listWidget_2.count() == 0 :
            QMessageBox.about(self,"저장","저장할 데이터가 없습니다.")
            return None
        #텍스트 파일 파일명 & 내용 날짜 선언
        now = datetime.datetime.now()
        nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
        nowDateFileName = now.strftime('%Y%m%d%H%M%S')
        #저장 상대 경로 설정
        fileSavePath = os.path.dirname(__file__)
        with codecs.open(fileSavePath+'\\log\\'+nowDateFileName+'.txt','w', encoding='utf8') as f:
            f.write('===== '+ nowDatetime + ' =====\n\n')
            if self.listWidget_1.count() > 0:
                f.write("1차 결과 ===== \n\n")
                for i in range(self.listWidget_1.count()):
                    f.write(self.listWidget_1.item(i).text()+'\n')
            if self.listWidget_2.count() > 0:
                f.write("\n\n2차 결과 ===== \n\n")
                for i in range(self.listWidget_2.count()):
                    f.write(self.listWidget_2.item(i).text()+'\n')
        #저장 완료 메시지
        QMessageBox.about(self,"저장","저장 완료")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    extractWord = Main()
    extractWord.show()
    app.exec_()
