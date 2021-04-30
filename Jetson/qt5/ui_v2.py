import sys
import time
from PyQt5 import QtCore, QtWidgets, QtGui
# QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QMainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from alpr import alpr
from notif_alert import notif_alert
from datetime import datetime


class NavPage(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.setWindowTitle("COPYRIGHT BLINKAH 2021-2069")
        # self.setWindowIcon(QtGui.QIcon("./graphics/B.png"))

        # Enable borderless windowed
        flags = QtCore.Qt.WindowFlags(
            QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)

        self.bkg_img = self.bkg_img()
        self.bkg_img.setParent(self)

        self.car_num = 0

        self.car_img = self.car_img()
        self.car_img.setParent(self)

        self.hud = self.hud()
        self.hud.setParent(self)

        self.plate_reading = self.plate_reading()
        self.plate_reading.setParent(self)

        self.plate_conf = self.plate_conf()
        self.plate_conf.setParent(self)

        # self.next_btn = self.next_btn()
        # self.next_btn.setParent(self)
        # self.next_btn.pressed.connect(self.press_next)
        # self.next_btn.clicked.connect(self.click_next)
        # self.next_btn.released.connect(self.release_next)

        self.alpr_btn = self.alpr_btn()
        self.alpr_btn.setParent(self)
        self.alpr_btn.pressed.connect(self.press_alpr)
        self.alpr_btn.clicked.connect(self.click_alpr)

        self.go_btn = self.go_btn()
        self.go_btn.setParent(self)
        self.go_btn.pressed.connect(self.press_go)
        self.go_btn.clicked.connect(self.click_go)

        self.rep_btn = self.rep_btn()
        self.rep_btn.setParent(self)
        self.rep_btn.pressed.connect(self.press_rep)
        self.rep_btn.clicked.connect(self.click_rep)
        self.rep_btn.released.connect(self.release_rep)

        self.time_box = self.time_box()
        self.time_box.setParent(self)

        self.rep_text = self.rep_text()
        self.rep_text.setParent(self)

        self.time = self.time()
        self.time.setParent(self)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.setObjectName("Time")
        timer.start(1000)

    #                  #
    #  HUD. Functions  #
    #                  #

    def time_box(self):
        TimeBox = QtWidgets.QLabel('')
        TimeBox.setGeometry(QtCore.QRect(30, 500, 350, 100))
        TimeBox.setObjectName("TimeBox")
        pixmap = QtGui.QPixmap('graphics/timebox_trans.png')
        pixmap = pixmap.scaled(350, 100)
        TimeBox.setPixmap(pixmap)
        return TimeBox

    def time(self):
        Time = QtWidgets.QLabel('')

        Time.setGeometry(QtCore.QRect(112, 500, 350, 100))
        font = QtGui.QFont()
        font.setFamily("Ani")
        font.setPointSize(32)
        Time.setFont(font)
        Time.setStyleSheet(
            "color: red;"
            "background-color: rgba(255, 255, 255, 0);"
            "border: 0px;"
            "border-color: rgba(255, 255, 255, 0);"
        )
        return Time

    def showTime(self):
        current_time = QtCore.QTime.currentTime()
        label_time = current_time.toString('hh:mm:ss')
        self.time.setText(label_time)

    def bkg_img(self):
        BkgImg = QtWidgets.QLabel('')
        BkgImg.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        BkgImg.setObjectName("BkgImg")
        BkgImg.setText(graphic_text('graphics/nav/gradient_home.png'))
        return BkgImg

    def car_img(self):
        CarImg = QtWidgets.QLabel('Hello')
        CarImg.setGeometry(QtCore.QRect(74, 93, 473, 253))
        CarImg.setObjectName("PlateImg")
        # CarImg.setPixmap(pixmap)

        # CarImg.setText(graphic_text('graphics/vis.png'))
        self.roundImage(CarImg, 'graphics/vis.png')

        return CarImg

    def hud(self):
        Hud = QtWidgets.QLabel('')
        Hud.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        Hud.setObjectName("Hud")
        Hud.setText(graphic_text('graphics/nav/nav_page_read.png'))

        return Hud

    def plate_reading(self):
        PlateReading = QtWidgets.QLabel('')
        PlateReading.setGeometry(QtCore.QRect(100, 45, 165, 44))
        PlateReading.setObjectName("PlateImg")
        font = QtGui.QFont()
        font.setFamily("LICENSE PLATE USA")
        font.setPointSize(28)
        PlateReading.setFont(font)
        PlateReading.setStyleSheet("color: red")

        return PlateReading

    def plate_conf(self):
        PlateConf = QtWidgets.QLabel('')
        PlateConf.setGeometry(QtCore.QRect(290, 56, 110, 30))
        PlateConf.setObjectName("PlateImg")
        font = QtGui.QFont()
        font.setFamily("Loma")
        font.setPointSize(20)
        PlateConf.setFont(font)
        PlateConf.setStyleSheet("color: red")

        return PlateConf

    # def next_btn(self):
    #     next_btn = QtWidgets.QPushButton('')
    #     next_btn.setEnabled(True)
    #     next_btn.setGeometry(QtCore.QRect(195, 245, 200, 200))
    #     next_btn.setStyleSheet("QPushButton {\n"
    #                            "    background-color: rgba(255, 255, 255, 0);\n"
    #                            "    border: 0px;\n"
    #                            "}")
    #     next_btn.setText('')
    #     icon = QtGui.QIcon()
    #     icon.addPixmap(QtGui.QPixmap("./graphics/next_arrow_2.png"),
    #                    QtGui.QIcon.Normal, QtGui.QIcon.On)
    #     next_btn.setIcon(icon)
    #     next_btn.setIconSize(QtCore.QSize(128, 128))
    #     next_btn.setObjectName("next_btn")

    #     return next_btn

    def alpr_btn(self):
        alpr_btn = QtWidgets.QPushButton('')
        alpr_btn.setEnabled(True)
        alpr_btn.setGeometry(QtCore.QRect(28, 114, 110, 126))
        alpr_btn.setStyleSheet("QPushButton {\n"
                               "    background-color: rgba(255, 255, 255, 50);\n"
                               "    border: 0px;\n"
                               "}")
        alpr_btn.setText('')
        alpr_btn.setIconSize(QtCore.QSize(128, 128))
        alpr_btn.setObjectName("alpr_btn")

        return alpr_btn

    def go_btn(self):
        go_btn = QtWidgets.QPushButton('')
        go_btn.setEnabled(True)
        go_btn.setGeometry(QtCore.QRect(800, 450, 200, 200))
        go_btn.setStyleSheet("QPushButton {\n"
                             "    background-color: rgba(255, 255, 255, 0);\n"
                             "    border: 0px;\n"
                             "}")
        go_btn.setText('')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./graphics/B.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.On)
        go_btn.setIcon(icon)
        go_btn.setIconSize(QtCore.QSize(128, 128))
        go_btn.setObjectName("go_btn")

        return go_btn

    # FOR NOTIFICATIONS
    def rep_btn(self):
        rep_btn = QtWidgets.QPushButton('')
        rep_btn.setEnabled(True)
        rep_btn.setGeometry(QtCore.QRect(700, 40, 256, 256))
        rep_btn.setStyleSheet("QPushButton {\n"
                              "    background-color: rgba(255, 255, 255, 0);\n"
                              "    border: 0px;\n"
                              "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./graphics/logo_256x256.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.On)
        rep_btn.setIcon(icon)
        rep_btn.setIconSize(QtCore.QSize(256, 256))
        rep_btn.setObjectName("rep_btn")

        return rep_btn

    def rep_text(self):
        rep_text = QtWidgets.QLabel('')
        # rep_text.setEnabled(True)
        # n_text = self.notifs()
        rep_text.setFont(QFont('Arial', 14))
        # rep_text.setBold(True)
        # rep_text.setText(n_text)
        rep_text.setGeometry(QtCore.QRect(400, 0, 500, 100))
        # rep_text.setStyleSheet("QPushButton {\n"
        #                     "    background-color: rgba(255, 255, 255, 0);\n"
        #                      "    border: 0px;\n"
        #                      "}")
        #icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap("./graphics/logo_256x256.png"),
        #               QtGui.QIcon.Normal, QtGui.QIcon.On)
        # rep_btn.setIcon(icon)
        #ep_btn.setIconSize(QtCore.QSize(256, 256))
        rep_text.setObjectName("rep_text")

        return rep_text

    #                  #
    # Helper Functions #
    #                  #

    def roundImage(self, CarImg, path):
        pixmap = QtGui.QPixmap(path)
        pixmap = pixmap.scaled(473, 253)

        # create empty pixmap of same size as original
        rounded = QtGui.QPixmap(473, 253)
        rounded.fill(QtGui.QColor("transparent"))

        # draw rounded rect on new pixmap using original pixmap as brush
        painter = QtGui.QPainter(rounded)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setBrush(QtGui.QBrush(pixmap))
        painter.setPen(QtCore.Qt.NoPen)

        #painter.drawRect(0, 0, 473, 253)

        path = QtGui.QPainterPath()
        path.setFillRule(QtCore.Qt.WindingFill)
        rect = QtCore.QRectF(0, 0, 473, 253)
        path.addRoundedRect(rect, 50, 50)
        path.addRect(0, 0, 50, 50)  # Top left corner not rounded
        painter.drawPath(path.simplified())

        # set pixmap of label
        CarImg.setPixmap(rounded)
        painter.end()

        return CarImg

    #                  #
    # Active Functions #
    #                  #

    def press_next(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("graphics/B.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.On),
        self.next_btn.setIcon(icon)

    def click_next(self):
        self.car_num += 1
        path = "sample_data/car"+str(self.car_num)+".jpg"
        self.roundImage(self.car_img, path)
        self.hud.setText(graphic_text('graphics/nav/nav_page_read'))
        self.plate_reading.setText('')
        self.plate_conf.setText('')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("graphics/B.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.On),
        self.next_btn.setIcon(icon)

    def release_next(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("graphics/B.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.On),
        self.next_btn.setIcon(icon)

    def press_alpr(self):
        self.hud.setText(graphic_text('graphics/nav/nav_page_clicked'))

    def click_alpr(self):
        self.runALPR(str(self.car_num))
        if (self.plate_reading.text() == ''):
            self.plate_reading.setText('FAILURE')
            self.plate_conf.setText('00%')

    def press_go(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "./graphics/B.png"), QtGui.QIcon.Normal, QtGui.QIcon.On),
        self.go_btn.setIcon(icon)

    def click_go(self):
        self.switch_window.emit()

    def press_rep(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("graphics/logo_256x256_2.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.On),
        self.rep_btn.setIcon(icon)

    def click_rep(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("graphics/logo_256x256.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.On),
        self.rep_btn.setIcon(icon)
        # n_text = self.notifs()
        # notif_label = QtWidgets.QLabel(n_text)
        # notif_label.setWindowTitle("Notification!")
        # notif_label.setGeometry(QtCore.QRect(700, 40, 256, 256))
        # notif_label.show()
        # BkgImg = QtWidgets.QLabel('')
        # BkgImg.setGeometry(QtCore.QRect(0, 0, 1024, 600))

    def release_rep(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("graphics/logo_256x256.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.On),
        self.rep_btn.setIcon(icon)

    #                  #
    # Machine Learning #
    #                  #

    def runALPR(self, num):
        plates = alpr(num)
        plate = plates[0].get('license_plate')
        conf = str(round(plates[0].get('confidence'))) + '%'
        self.plate_reading.setText(plate.lower())
        self.plate_conf.setText(conf)

        return plate

    #                            #
    # Audio & Text Notifications #
    #                            #

    # def notifs(self):
    #     n_text = notif_alert()
    #     return n_text


class Controller:

    def __init__(self):
        pass

    # def show_HomePage(self):
    #     self.HomePage = HomePage()
    #     self.HomePage.switch_window.connect(self.HomePage_to_NavPage)
    #     self.HomePage.show()

    def show_main(self):
        #self.window = MainWindow()
        # self.window.switch_window.connect(self.show_NavPage)
        # self.HomePage.close()
        self.window = NavPage()
        self.window.show()

    # def HomePage_to_NavPage(self):
    #     self.NavPage = NavPage()
    #     self.NavPage.switch_window.connect(self.NavPage_to_HomePage)
    #     self.NavPage.show()
    #     time.sleep(.1)
    #     self.HomePage.close()

    # def NavPage_to_HomePage(self):
    #     self.HomePage = HomePage()
    #     self.HomePage.switch_window.connect(self.HomePage_to_NavPage)
    #     self.HomePage.show()
    #     time.sleep(.1)
    #     self.NavPage.close()


def graphic_text(path):
    return "<html><head/><body><p><img src=\""+path+"\"/></p></body></html>"


def clock():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    return current_time


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_main()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
