from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTabWidget, QTextBrowser, QAction, QMenu, QFileDialog
from PyQt5.QtCore import Qt, pyqtSignal
import qtawesome, functools

from gui.usefulwidget import closeashidewindow
from myutils.config import globalconfig, _TR


class transhist(closeashidewindow):

    getnewsentencesignal = pyqtSignal(str)
    getnewtranssignal = pyqtSignal(str, str)

    def __init__(self, parent):
        super(transhist, self).__init__(parent, globalconfig, "hist_geo")
        self.setupUi()
        # self.setWindowFlags(self.windowFlags()&~Qt.WindowMinimizeButtonHint)
        self.getnewsentencesignal.connect(self.getnewsentence)
        self.getnewtranssignal.connect(self.getnewtrans)
        self.hiderawflag = False
        self.hideapiflag = False

        self.setWindowTitle(_TR("历史翻译"))

    def setupUi(self):
        self.setWindowIcon(qtawesome.icon("fa.rotate-left"))

        def gettb(_type):
            textOutput = QTextBrowser()
            textOutput.setContextMenuPolicy(Qt.CustomContextMenu)
            textOutput.customContextMenuRequested.connect(
                functools.partial(self.showmenu, textOutput, _type)
            )
            textOutput.setUndoRedoEnabled(False)
            textOutput.setReadOnly(True)
            textOutput.setObjectName("textOutput")
            return textOutput

        self.textOutput = gettb(1)
        self.setCentralWidget(self.textOutput)

        self.hiding = True

    def showmenu(self, tb, flag, p):
        menu = QMenu(self)
        qingkong = QAction(_TR("清空"))
        baocun = QAction(_TR("保存"))
        hideshowraw = QAction(_TR("显示原文" if self.hiderawflag else "不显示原文"))
        hideshowapi = QAction(_TR("显示api" if self.hideapiflag else "不显示api"))
        menu.addAction(qingkong)
        menu.addAction(baocun)
        if flag == 1:
            menu.addAction(hideshowraw)
            menu.addAction(hideshowapi)

        action = menu.exec(self.mapToGlobal(p))
        if action == qingkong:
            tb.clear()
        elif action == baocun:
            ff = QFileDialog.getSaveFileName(self, directory="save.txt")
            if ff[0] == "":
                return
            with open(ff[0], "w", encoding="utf8") as ff:
                ff.write(tb.toPlainText())
        elif action == hideshowraw:

            self.hiderawflag = not self.hiderawflag
        elif action == hideshowapi:

            self.hideapiflag = not self.hideapiflag

    def getnewsentence(self, sentence):

        sentence = "<hr>" if globalconfig["hist_split"] else "\n" + sentence
        if self.hiderawflag:
            sentence = ""
        self.textOutput.append(sentence)

    def getnewtrans(self, api, sentence):
        if self.hideapiflag:
            res = sentence
        else:
            res = api + "  " + sentence
        self.textOutput.append(res)
