from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *

manual_ui = uic.loadUiType("manual.ui")[0]

class manualWindow(QDialog, QWidget, manual_ui):
    def __init__(self):
        super(manualWindow, self).__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.setWindowIcon(QIcon('owl.png'))
        self.close_btn.clicked.connect(self.quit)

    def quit(self):
        self.close()