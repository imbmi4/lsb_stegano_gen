import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import requests
from bs4 import BeautifulSoup as bs

crawling_ui = uic.loadUiType("crawling.ui")[0]

class crawlingWindow(QDialog, QWidget, crawling_ui):
    url = 'https://www.boannews.com/media/list.asp?mkind=1'  # 보안 뉴스 Security Tab

    def __init__(self):
        super(crawlingWindow, self).__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.setWindowIcon(QIcon('owl.png'))
        self.Search()
        self.home.clicked.connect(self.Home)

    def Search(self):

        print(self.url)
        page = requests.get(self.url, verify=False)
        soup = bs(page.text, "html.parser")

        self.CreateLink(0, self.article1, soup)
        self.CreateLink(1, self.article2, soup)
        self.CreateLink(2, self.article3, soup)
        self.CreateLink(3, self.article4, soup)
        self.CreateLink(4, self.article5, soup)

        self.boannews.setText('<a href="{}">최근 보안 이슈 보러가기</a>'.format(self.url))
        self.boannews.setStyleSheet("background-color : black; Color : rgb(152,243,6); border:1px solid white")
        self.boannews.setOpenExternalLinks(True)

    def CreateLink(self, index, article, parser):
        topic = parser.select_one('#news_area > div:nth-child({}) > a:nth-child(1) > span'.format(2*(index+4)))
        link = parser.select_one('#news_area > div:nth-child({})'.format(2*(index+4)))
        article.setText('<a href="{}">{}</a>'.format('www.boannews.com' + link.a.attrs['href'], topic))
        article.setOpenExternalLinks(True)
        article.setStyleSheet("background-color : black; Color : rgb(152,243,6); border:1px solid white; text-decoration : none")

    def Home(self):
        self.close()