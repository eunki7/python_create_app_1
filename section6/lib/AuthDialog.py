import sys
from PyQt5.QtWidgets import *

class AuthDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

        self.user_id = None
        self.user_pw = None

    def setupUI(self):
        self.setGeometry(300,1800,300,100)
        self.setWindowTitle("Sign In")
        self.setFixedSize(300,100)

        label1 = QLabel("ID:")
        label2 = QLabel("Password:")

        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.lineEdit2.setEchoMode(QLineEdit().Password)

        self.pushButton = QPushButton("로그인")
        self.pushButton.clicked.connect(self.submitLogin)

        layout = QGridLayout()
        layout.addWidget(label1,0,0)
        layout.addWidget(self.lineEdit1,0,1)
        layout.addWidget(self.pushButton,0,2)
        layout.addWidget(label2,1,0)
        layout.addWidget(self.lineEdit2,1,1)

        self.setLayout(layout)

    def submitLogin(self):
        self.user_id = self.lineEdit1.text()
        self.user_pw = self.lineEdit2.text()
        #print(self.user_id,self.user_pw)

        if self.user_id is None or self.user_id == '' or not self.user_id:
            QMessageBox.about(self,"인증오류","ID를 입력하세요.")
            self.lineEdit1.setFocus(True)
            return None

        if self.user_pw is None or self.user_pw == '' or not self.user_pw:
            QMessageBox.about(self,"인증오류","PW를 입력하세요.")
            self.lineEdit2.setFocus(True)
            return None

        # 이 부분에서 필요한 경우 실제 로컬 DB 또는 서버 연동 후
        # 유저 정보 및 사용 유효기간을 체크하는 코드를 넣어주세요.
        # code
        # code

        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    loginDialog = AuthDialog()
    loginDialog.show()
    app.exec_()
