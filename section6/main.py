import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QUrl, QThread
from PyQt5 import uic
from lib.YouViewerLayout import Ui_MainWindow
from lib.AuthDialog import AuthDialog
from lib.IntroWorker import IntroWorker
import re
import datetime
import pytube
from PyQt5.QtMultimedia import QSound

#form_class = uic.loadUiType("C:/Django/workspace/python-class1/section6/ui/you_viewer_v1.0.ui")[0]
#intro 음악 출처 : https://www.youtube.com/watch?v=qEMeUmN04FA

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        #초기화
        self.setupUi(self)
        #초기 잠금
        self.initAuthLock()
        #시그널 초기화
        self.initSignal()
        #로그인 관련 변수 선언
        self.user_id = None
        self.user_pw = None
        #재생 여부
        self.is_play = False
        #Youtube 관련 작업
        self.youtb = None
        self.youtb_fsize = 0
        #배경음악 Thread 작업 선언
        self.initIntroThread()
        #Qthread 사용 안할 경우
        #QSound.play("C:/Django/workspace/python-class1/section6/resource/intro.wav")


    #기본 UI 비활성화
    def initAuthLock(self):
        self.previewButton.setEnabled(False)
        self.fileNavButton.setEnabled(False)
        self.streamCombobox.setEnabled(False)
        self.startButton.setEnabled(False)
        self.calendarWidget.setEnabled(False)
        self.urlTextEdit.setEnabled(False)
        self.pathTextEdit.setEnabled(False)
        self.showStatusMsg('인증안됨')

    #기본 UI 활성화
    def initAuthActive(self):
        self.previewButton.setEnabled(True)
        self.fileNavButton.setEnabled(True)
        self.streamCombobox.setEnabled(True)
        self.calendarWidget.setEnabled(True)
        self.urlTextEdit.setEnabled(True)
        self.pathTextEdit.setEnabled(True)
        self.showStatusMsg('인증 완료')

    def showStatusMsg(self,msg):
        self.statusbar.showMessage(msg)

    #시그널 초기화
    def initSignal(self):
        self.loginButton.clicked.connect(self.authCheck)
        self.previewButton.clicked.connect(self.load_url)
        self.exitButtion.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.webView.loadProgress.connect(self.showProgressBrowserLoading)
        self.fileNavButton.clicked.connect(self.selectDownPath)
        self.calendarWidget.clicked.connect(self.append_date)
        self.startButton.clicked.connect(self.downloadYoutb)

    #인트로 쓰레드 초기화 및 활성화
    def initIntroThread(self):
        #Worker선언
        self.introObj = IntroWorker()
        #Qthread 선언
        self.introThread = QThread()
        #Worker To thread 전환
        self.introObj.moveToThread(self.introThread)
        #시그널 연결
        self.introObj.startMsg.connect(self.showIntroInfo)
        #Thread 시작 메소드 연결
        self.introThread.started.connect(self.introObj.playBgm)
        #Thread 스타트
        self.introThread.start()

    #인트로 쓰레드 Signal 실행
    def showIntroInfo(self, msg, fileName):
        self.plainTextEdit.appendPlainText("Program Started by : " + msg)
        self.plainTextEdit.appendPlainText("Playing intro infomation is : ")
        self.plainTextEdit.appendPlainText(fileName)

    @pyqtSlot()
    def authCheck(self):
        dlg = AuthDialog()
        dlg.exec_()
        self.user_id = dlg.user_id
        self.user_pw = dlg.user_pw

        # 이 부분에서 필요한 경우 실제 로컬 DB 또는 서버 연동 후
        # 유저 정보 및 사용 유효기간을 체크하는 코드를 넣어주세요.
        # code
        # code
        #print("id: %s password: %s" %(self.user_id,self.user_pw))

        if True:
            self.initAuthActive()
            self.loginButton.setText("인증완료")
            self.loginButton.setEnabled(False)
            self.urlTextEdit.setFocus(True)
            self.append_log_msg("login Success")

        else:
            QMessageBox.about(self, "인증오류", "아이디 또는 비밀번호 인증 오류")


    def load_url(self):
        url = self.urlTextEdit.text().strip()
        v = re.compile('^https://www.youtube.com/?')
        if self.is_play:
            self.append_log_msg('Stop Click')
            self.webView.load(QUrl('about:blank'))
            self.previewButton.setText("재생")
            self.is_play = False
            self.urlTextEdit.clear()
            self.urlTextEdit.setFocus(True)
            self.startButton.setEnabled(False)
            self.streamCombobox.clear()
            self.progressBar_2.setValue(0)
            self.showStatusMsg("인증 완료")
        else:
            if v.match(url) is not None:
                self.append_log_msg('Play Click')
                self.webView.load(QUrl(url))
                self.showStatusMsg(url + "재생 중")
                self.previewButton.setText("중지")
                self.is_play = True
                self.startButton.setEnabled(True)
                self.initialYouWork(url)

            else:
                QMessageBox.about(self,"URL 형식오류","Youtube 주소 형식이 아닙니다.")
                self.urlTextEdit.clear()
                self.urlTextEdit.setFocus(True)

    def initialYouWork(self,url):
        video_list = pytube.YouTube(url)
        #로딩바 계산
        video_list.register_on_progress_callback(self.showProgressDownLoading)
        self.youtb = video_list.streams.all()
        self.streamCombobox.clear()
        for q in self.youtb:
            #print('step1',q.itag,q.mime_type,q.abr)
            tmp_list, str_list = [], []
            tmp_list.append(str(q.mime_type or ''))
            tmp_list.append(str(q.res or ''))
            tmp_list.append(str(q.fps or ''))
            tmp_list.append(str(q.abr or ''))

            #print('step_2',tmp_list)
            str_list = [x for x in tmp_list if x != '']
            #print('step3',str_list)
            print('join',','.join(str_list))
            self.streamCombobox.addItem(','.join(str_list))



    def append_log_msg(self,act):
        now = datetime.datetime.now()
        nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
        app_msg = self.user_id + ' : ' + act + ' - (' + nowDatetime + ')'
        print(app_msg)
        self.plainTextEdit.appendPlainText(app_msg) #insertPlainText

        #활동 로그 저장(또는 DB를 사용 추천)
        with open('txt 저장 경로 입력','a') as f:
            f.write(app_msg+'\n')

    @pyqtSlot(int)
    def showProgressBrowserLoading(self, v):
        self.progressBar.setValue(v)

    @pyqtSlot()
    def selectDownPath(self):
        #파일선택
        #fname = QFileDialog.getOpenFileName(self)
        #self.pathTextEdit.setText(fname[0])

        #경로선택
        fpath = QFileDialog.getExistingDirectory(self,'Select Directory')
        self.pathTextEdit.setText(fpath)

    @pyqtSlot()
    def append_date(self):
        cur_date = self.calendarWidget.selectedDate()
        #print('click date', self.calendarWidget.selectedDate().toString())
        print(str(cur_date.year())+'-'+str(cur_date.month())+'-'+str(cur_date.day()))
        self.append_log_msg('Calendar Click')

    @pyqtSlot()
    def downloadYoutb(self):
        down_dir = self.pathTextEdit.text().strip()
        if down_dir is None or down_dir == '' or not down_dir:
            QMessageBox.about(self,'경로 선택','다운로드 받을 경로를 선택하세요.')
            return None

        self.youtb_fsize = self.youtb[self.streamCombobox.currentIndex()].filesize
        #print('fsize',self.youtb_fsize)
        self.youtb[self.streamCombobox.currentIndex()].download(down_dir)
        self.append_log_msg('Download Click')

    def showProgressDownLoading(self, stream, chunk, finle_handle, bytes_remaining):
        #print(int(self.youtb_fsize - bytes_remaining))
        #print('bytes_remaining',bytes_remaining)
        self.progressBar_2.setValue(int(((self.youtb_fsize - bytes_remaining) / self.youtb_fsize) * 100))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    you_viewer_main = Main()
    you_viewer_main.show()
    app.exec_()
