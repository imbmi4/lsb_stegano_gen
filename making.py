import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PIL import Image
from manual import manualWindow

making_ui = uic.loadUiType("making.ui")[0]

class makingWindow(QDialog, QWidget, making_ui):
    color = ['Red', 'Green', 'Blue']
    HiddenImageName = ''
    CoverImageName = ''

    def __init__(self):
        super(makingWindow, self).__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.setWindowIcon(QIcon('owl.png'))
        self.home.clicked.connect(self.Home)
        self.load_hidden.clicked.connect(self.LoadHiddenImage)
        self.load_cover.clicked.connect(self.LoadCoverImage)
        self.make_btn.clicked.connect(self.Steg)
        self.manual.clicked.connect(self.showmanual)

    def LoadHiddenImage(self):
        global HiddenImageName
        self.HiddenImageName = QFileDialog.getOpenFileName(self)

        if '.bmp' not in self.HiddenImageName[0]:
            self.srcimage.setText("Hidden image must be bmp file!")
            return

        qPixmapVar = QPixmap()
        qPixmapVar.load(self.HiddenImageName[0])
        makingWindow.HiddenImage = Image.open(self.HiddenImageName[0])
        global hidden_width, hidden_height
        hidden_width, hidden_height = makingWindow.HiddenImage.size
        self.hidden_info.setText("Width : {}\nHeight : {}".format(hidden_width, hidden_height))
        self.srcimage.setPixmap(qPixmapVar)
        self.hidden_scroll.setWidgetResizable(True)
        self.hidden_scroll.setWidget(self.srcimage)

    def LoadCoverImage(self):
        self.CoverImageName = QFileDialog.getOpenFileName(self)
        qPixmapVar = QPixmap()
        qPixmapVar.load(self.CoverImageName[0])
        makingWindow.CoverImage = Image.open(self.CoverImageName[0])
        global cover_width, cover_height
        cover_width, cover_height = makingWindow.CoverImage.size
        self.cover_info.setText("Width : {}\nHeight : {}".format(cover_width, cover_height))
        self.dstimage.setPixmap(qPixmapVar)
        self.cover_scroll.setWidgetResizable(True)
        self.cover_scroll.setWidget(self.dstimage)

    def Steg(self):
        if self.HiddenImageName == '':
            self.srcimage.setText("Hidden image must be loaded!")
            return

        if self.CoverImageName == '':
            self.dstimage.setText("Cover image must be loaded!")
            return

        if hidden_height > cover_height or hidden_width > cover_width:
            self.caution.setText("Cover image should be larger than hidden image!")
            return

        target_color = self.color_combo.currentText()
        target_plane = int(self.plane_combo.currentText()[6])
        for y in range(hidden_height):
            for x in range(hidden_width):
                cover_rgb = self.CoverImage.getpixel((x, y))
                hidden_rgb = self.HiddenImage.getpixel((x, y))

                target = cover_rgb[makingWindow.color.index(target_color)]

                cvr_r, cvr_g, cvr_b = cover_rgb
                hid_r, hid_g, hid_b = hidden_rgb
                if hid_r == 0 and hid_g == 0 and hid_b == 0:
                    target -= target & (2 ** target_plane)
                else:
                    target = target | (2 ** target_plane)

                if target_color == 'Red':
                    self.CoverImage.putpixel((x, y), (target, cvr_g, cvr_b))
                elif target_color == 'Green':
                    self.CoverImage.putpixel((x, y), (cvr_r , target, cvr_b))
                else:
                    self.CoverImage.putpixel((x, y), (cvr_r, cvr_g, target))
        self.CoverImage.save("result.png", "png")
        self.caution.setText("Steg Complete!! Result saved in 'result.png'")

    def showmanual(self):
        self.manual = manualWindow()

    def Home(self):
        self.close()