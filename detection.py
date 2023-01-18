import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PIL import Image

detection_ui = uic.loadUiType("detection.ui")[0]

class detectionWindow(QDialog, QWidget, detection_ui):
    case = 0
    color = ['Red', 'Green', 'Blue']
    global original_img
    global result_img
    fname = ''

    def __init__(self):
        super(detectionWindow, self).__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.setWindowIcon(QIcon('owl.png'))
        self.home.clicked.connect(self.Home)
        self.load_btn.clicked.connect(self.LoadImage)
        self.next.clicked.connect(self.nextImage)
        self.previous.clicked.connect(self.previousImage)

    def LoadImage(self):
        self.fname = QFileDialog.getOpenFileName(self)
        qPixmapVar = QPixmap()
        qPixmapVar.load(self.fname[0])
        detectionWindow.original_img = Image.open(self.fname[0])
        detectionWindow.result_img = Image.open(self.fname[0])
        self.img_area.setPixmap(qPixmapVar)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.img_area)

    def Detect(self, case):
        if self.fname == '':
            self.img_area.setText("Image must be loaded!")
            return
        self.status.setText("Detection Ongoing...")
        self.result_img.save("tmp.png", "png")
        width, height = detectionWindow.original_img.size

        cmpr_idx = 2 - ((23-case) // 8)

        for y in range(height):
            for x in range(width):
                rgb = detectionWindow.original_img.getpixel((x, y))

                cmpr_bit = rgb[cmpr_idx]

                if cmpr_bit & (2 ** (case % 8)) == 0:  # 검은색
                    self.result_img.putpixel((x, y), (0, 0, 0))

                else:  # 하얀색
                    self.result_img.putpixel((x, y), (255, 255, 255))

        self.result_img.save("tmp.png", "png")
        qPixmapVar = QPixmap()
        qPixmapVar.load("tmp.png")
        self.img_area.setPixmap(qPixmapVar)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.img_area)
        self.status.setText('{} plane {}'.format(self.color[cmpr_idx], case % 8))

    def nextImage(self):
        self.Detect(detectionWindow.case)
        detectionWindow.case = (detectionWindow.case + 1) % 24

    def previousImage(self):
        if detectionWindow.case == 0:
            detectionWindow.case = 24
        detectionWindow.case -= 1
        self.Detect(detectionWindow.case)

    def Home(self):
        self.close()