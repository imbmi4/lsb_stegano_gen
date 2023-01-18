import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from detection import detectionWindow
from making import makingWindow
from crawling import crawlingWindow
from PyQt5.QtGui import *

form_main = uic.loadUiType("main.ui")[0] #ui 파일 불러오기

#test에 바로 실행시킬 파일명을 입력하면 됨

class MainWindow(QMainWindow,QWidget,form_main):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.setWindowIcon(QIcon('owl.png'))
        self.detection.clicked.connect(self.detectionbuttonClicked)  # 버튼 클릭시 연결되는 함수
        self.making.clicked.connect(self.makingbuttonClicked)
        self.sec_issue.clicked.connect(self.issuebuttonClicked)
        self.exit_btn.clicked.connect(self.exitbuttonClicked)


    def detectionbuttonClicked(self): #pushButton 클릭되었을때 text상자에 출력해주는 소스
       	self.hide() #한번만
        self.detection = detectionWindow()
        self.detection.exec()
        self.show()

    def makingbuttonClicked(self): #pushButton 클릭되었을때 text상자에 출력해주는 소스
        self.hide()  # 한번만
        self.making = makingWindow()
        self.making.exec()
        self.show()

    def issuebuttonClicked(self): #pushButton 클릭되었을때 text상자에 출력해주는 소스
        self.hide()  # 한번만
        self.crawling = crawlingWindow()
        self.crawling.exec()
        self.show()

    def exitbuttonClicked(self): #pushButton 클릭되었을때 text상자에 출력해주는 소스
       	self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
    if os.path.isfile('./tmp.png'):
        os.remove('./tmp.png')
    else:
        print("No file")