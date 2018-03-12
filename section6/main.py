import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import pyqtSlot, QThread
from PyQt5 import QtCore
#두 번째 방법
from lib.YouViewerLayout import Ui_MainWindow
from lib.AuthDialog import AuthDialog
import pytube
import re
import datetime
#pyqt5, pytube 설치

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initSignal()
        self.initAuthLock()

        #로그인 사용자
        self.user_id = None
        self.user_pw = None

        #미리보기 재생 여부
        self.is_play = False

        #Youtube 관련 작업
        self.youtb = None
        self.youtb_fsize = 0

    #기본 UI 비활성화
    def initAuthLock(self):
        self.previewButton.setEnabled(False)
        self.fileNavButton.setEnabled(False)
        self.streamCombobox.setEnabled(False)
        self.startButton.setEnabled(False)
        self.calendarWidget.setEnabled(False)
        self.urlTextEdit.setEnabled(False)
        self.pathTextEdit.setEnabled(False)
        self.showStatusMsg('인증 안됨')

    #기본 UI 활성화
    def initAuthActive(self):
        self.previewButton.setEnabled(True)
        self.fileNavButton.setEnabled(True)
        self.streamCombobox.setEnabled(True)
        self.calendarWidget.setEnabled(True)
        self.urlTextEdit.setEnabled(True)
        self.pathTextEdit.setEnabled(True)
        self.showStatusMsg('인증 완료')

    #시그널 연결
    def initSignal(self):
        self.loginButton.clicked.connect(self.auth_check)
        self.previewButton.clicked.connect(self.load_url)
        self.fileNavButton.clicked.connect(self.select_down_path)
        self.exitButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.startButton.clicked.connect(self.download_youtb)
        self.webView.loadProgress.connect(self.show_progress_browser_loading)
        self.calendarWidget.clicked.connect(self.append_date)

    #상태 메시지 출력
    def showStatusMsg(self, msg):
        self.statusbar.showMessage(msg)

    #Youtube 다운로드 세팅
    def initialYouWork(self, url):
        video_list = pytube.YouTube(url)
        video_list.register_on_progress_callback(self.show_progress_download_loading)
        self.youtb = video_list.streams.all()
        self.streamCombobox.clear()
        for q in self.youtb:
            tmp_list, str_list = [], []

            tmp_list.append(str(q.mime_type or ''))
            tmp_list.append(str(q.res or ''))
            tmp_list.append(str(q.fps or ''))
            tmp_list.append(str(q.abr or ''))

            str_list = [x for x in tmp_list if x != '']
            #str_list = [x for x in tmp_list if x]

            self.streamCombobox.addItem(', '.join(str_list))

    #브라우저 로딩 Progress 표시
    @pyqtSlot(int)
    def show_progress_browser_loading(self,v):
        self.progressBar_1.setValue(v)

    @pyqtSlot()
    def load_url(self):
        url = self.urlTextEdit.toPlainText().strip()
        v = re.compile('^https://www.youtube.com/?')
        if self.is_play:
            self.append_log_msg('Stop Click')
            self.webView.load(QUrl('about:blank'))
            self.previewButton.setText('재생')
            self.is_play = False
            self.urlTextEdit.clear()
            self.urlTextEdit.setFocus(True)
            self.startButton.setEnabled(False)
            self.streamCombobox.clear()
            self.progressBar_2.setValue(0)
            self.showStatusMsg('인증 완료')
        else:
            #Youtube 주소 형식 검사
            if v.match(url) is not None:
                self.append_log_msg('Play Click')
                self.webView.load(QUrl(url))
                self.showStatusMsg(url + " 재생 중")
                self.previewButton.setText('중지')
                self.is_play = True
                self.startButton.setEnabled(True)
                self.initialYouWork(url)
            else:
                QMessageBox.about(self, "URL형식 오류", "Youtube 주소 형식이 아닙니다.")
                self.urlTextEdit.clear()
                self.urlTextEdit.setFocus(True)

    @pyqtSlot()
    def select_down_path(self):

        #파일 선택
        #fname = QFileDialog.getOpenFileName(self)
        #self.pathTextEdit.setText(fname[0])

        #폴더 선택
        fname = QFileDialog.getExistingDirectory(self,'Select directory')
        self.pathTextEdit.setText(fname)

    @pyqtSlot()
    def auth_check(self):
        dlg = AuthDialog()
        dlg.exec_()
        self.user_id = dlg.user_id
        self.user_pw = dlg.user_pw

        # 이 부분에서 필요한 경우 실제 로컬 DB 또는 서버 DB 연동 후
        # Code
        # Code
        # Code
        # 유저 정보 및 사용 유효기간 체크를 하도록 한다.
        # print("id: %s password: %s" % (user_id, user_pw))

        if True:
            self.initAuthActive()
            self.loginButton.setText('인증완료')
            self.loginButton.setEnabled(False)
            self.urlTextEdit.setFocus(True)
            self.append_log_msg('login Success')
        else:
            QMessageBox.about(self, "인증오류", "아이디 또는 비밀번호 인증 오류")
            #qbox = QMessageBox()
            #qbox.setIcon(QMessageBox.Information)
            #qbox.setInformativeText("아이디 또는 비밀번호 인증 오류")
            #qbox.setWindowTitle("인증오류")
            #qbox.exec_()

    @pyqtSlot()
    def download_youtb(self):
        down_dir = self.pathTextEdit.toPlainText().strip()
        if down_dir is None or down_dir == '' or not down_dir:
            QMessageBox.about(self, "경로 선택", "다운받을 경로를 선택하세요.")
            self.pathTextEdit.setFocus(True)
            return None
        self.youtb_fsize = self.youtb[self.streamCombobox.currentIndex()].filesize
        self.youtb[self.streamCombobox.currentIndex()].download(down_dir)
        self.append_log_msg('Download Click')

    def show_progress_download_loading(self,stream, chunk, file_handle, bytes_remaining):
        #전체 사이즈 , 다운로드 바이트 출력
        #print('check_ramains',bytes_remaining, self.youtb_fsize)
        self.progressBar_2.setValue(int(((self.youtb_fsize - bytes_remaining) / self.youtb_fsize) * 100))

    @pyqtSlot()
    def append_date(self):
        cur_date = self.calendarWidget.selectedDate()
        #print('click date',self.calendarWidget.selectedDate().toString())
        print(str(cur_date.year())+'-'+str(cur_date.month())+'-'+str(cur_date.day()))
        self.append_log_msg('Calendar Click')

    #Log 삽입 공통 Func
    def append_log_msg(self, act):
        now = datetime.datetime.now()
        nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
        app_msg = self.user_id + ' : ' + act + ' - (' + nowDatetime + ')'
        #insertPlainText
        self.plainEdit.appendPlainText(app_msg)

        #활동 로그 저장(또는 DB를 사용 추천)
        with open('d:/log.txt', 'a') as f:
            f.write(app_msg+'\n')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    you_viewer_main = Main()
    you_viewer_main.show()
    app.exec_()
