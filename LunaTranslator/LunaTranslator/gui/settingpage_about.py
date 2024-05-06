from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QWidget, QLabel, QProgressBar
from gui.usefulwidget import getsimpleswitch, getsimplecombobox
from myutils.config import globalconfig, _TR, static_data
from myutils.wrapper import threader
import platform, winsharedutils, sys
from myutils.utils import makehtml
from functools import partial
from myutils.githubupdate import updatemethod, getvesionmethod


@threader
def getversion(self):
    version = winsharedutils.queryversion(sys.argv[0])
    if version is None:
        return
    versionstring = f"v{version[0]}.{version[1]}.{version[2]}"
    self.versiontextsignal.emit(
        ("当前版本") + ":" + versionstring + "  " + ("最新版本") + ":" + ("获取中")
    )  # ,'',url,url))
    _version = getvesionmethod()

    if _version is None:
        sversion = _TR("获取失败")
    else:
        sversion = _version
    self.versiontextsignal.emit(
        (
            "{}:{}  {}  {}:{}".format(
                _TR("当前版本"),
                versionstring,
                platform.architecture()[0],
                _TR("最新版本"),
                sversion,
            )
        )
    )
    if _version is not None and versionstring < _version:
        if globalconfig["autoupdate"]:
            updatemethod(_version, self.progresssignal.emit)


def updateprogress(self, text, val):
    self.downloadprogress.setValue(val)
    self.downloadprogress.setFormat(text)


def setTab_about_dicrect(self):

    self.versionlabel = QLabel()
    self.versionlabel.setOpenExternalLinks(True)
    self.versionlabel.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
    self.versiontextsignal.connect(lambda x: self.versionlabel.setText(x))
    self.downloadprogress = QProgressBar()

    self.downloadprogress.setRange(0, 10000)

    self.downloadprogress.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
    self.progresssignal.connect(lambda text, val: updateprogress(self, text, val))
    getversion(self)


def setTab_about(self):
    self.tabadd_lazy(self.tab_widget, ("其他设置"), lambda: setTab_aboutlazy(self))


def double_(self, grid):
    return self.makescroll(self.makegrid(grid))


def resourcegrid(self):
    titles = []
    makewidgetsfunctions = []
    for sourcetype in static_data["aboutsource"]:
        titles.append(sourcetype["name"])
        sources = sourcetype["sources"]
        grid = []
        for source in sources:
            name = source["name"]
            link = source["link"]
            if type(link) == list:
                for i, _link in enumerate(link):
                    grid.append(
                        [
                            (_TR(name) if i == 0 else "", 1, ""),
                            (makehtml(_link, True), 2, "link"),
                        ]
                    )
            else:
                if link[-8:] == "releases":
                    __ = False
                elif link[-1] == "/":
                    __ = False
                else:
                    __ = True
                grid.append([(_TR(name), 1, ""), (makehtml(link, __), 2, "link")])
        makewidgetsfunctions.append(partial(double_, self, grid))
    return self.makesubtab_lazy(titles, makewidgetsfunctions)


def setTab_aboutlazy(self):

    grid2 = [
        [
            ("自动下载更新(需要连接github)", 5),
            (
                getsimpleswitch(
                    globalconfig, "autoupdate", callback=lambda x: getversion(self)
                ),
                1,
            ),
            ("", 10),
        ],
        [(self.versionlabel, 10)],
        [(self.downloadprogress, 10)],
        [],
        [("Internet", 5)],
        [(getsimplecombobox(["winhttp", "libcurl"], globalconfig, "network"), 5)],
        [("WebView", 5)],
        [(getsimplecombobox(["IEFrame", "WebView2"], globalconfig, "usewebview"), 5)],
    ]

    shuominggrid = [
        [
            "项目网站",
            (makehtml("https://github.com/HIllya51/LunaTranslator"), 3, "link"),
        ],
        [
            "问题反馈",
            (makehtml("https://github.com/HIllya51/LunaTranslator/issues"), 3, "link"),
        ],
    ]
    if globalconfig["languageuse"] == 0:
        shuominggrid += [
            [
                "交流群",
                (makehtml("https://qm.qq.com/q/qE32v9NYBO", show=912525396), 3, "link"),
            ],
            [],
            [("如果你感觉该软件对你有帮助，欢迎微信扫码赞助，谢谢~", 4)],
        ]
    else:
        shuominggrid += [
            [],
            [
                (
                    "If you feel that the software is helpful to you, ",
                    4,
                    "link",
                )
            ],
            [
                (
                    'welcome to become my <a href="https://patreon.com/HIllya51">sponsor. Thank you ~ ',
                    4,
                    "link",
                )
            ],
        ]
    tab = self.makesubtab_lazy(
        ["相关说明", "其他设置", "资源下载"],
        [
            lambda: self.makevbox(
                [
                    self.makegrid(shuominggrid),
                    (
                        imgwidget("./files/zan.jpg")
                        if globalconfig["languageuse"] == 0
                        else QLabel()
                    ),
                ]
            ),
            lambda: self.makescroll(self.makegrid(grid2)),
            lambda: resourcegrid(self),
        ],
    )
    return tab


class imgwidget(QWidget):
    def __init__(self, src) -> None:
        super().__init__()
        self.lb = QLabel(self)

        self.img = QPixmap.fromImage(QImage(src))

    def paintEvent(self, a0) -> None:
        self.lb.resize(self.size())
        self.lb.setPixmap(
            self.img.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        )
        return super().paintEvent(a0)
