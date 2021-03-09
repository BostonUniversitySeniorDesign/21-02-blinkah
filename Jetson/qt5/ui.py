import sys, time
from PyQt5 import QtCore, QtWidgets, QtGui


class MainWindow(QtWidgets.QWidget):

  switch_window = QtCore.pyqtSignal(str)

  def __init__(self):
    QtWidgets.QWidget.__init__(self)
    self.setWindowTitle('Main Window')

    layout = QtWidgets.QGridLayout()

    self.line_edit = QtWidgets.QLineEdit()
    layout.addWidget(self.line_edit)

    self.button = QtWidgets.QPushButton('Switch Window')
    self.button.clicked.connect(self.switch)
    layout.addWidget(self.button)

    self.setLayout(layout)

  def switch(self):
    self.switch_window.emit(self.line_edit.text())




class HomePage(QtWidgets.QWidget):

  switch_window = QtCore.pyqtSignal()

  def __init__(self):
    QtWidgets.QWidget.__init__(self)
    self.setGeometry(QtCore.QRect(0,0,1024,600))
    self.setWindowTitle("COPYRIGHT BLINKAH 2021-2069")
    #self.setWindowIcon(QtGui.QIcon("./graphics/B.png"))

    # Enable borderless windowed
    flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
    self.setWindowFlags(flags)

    self.logo = self.logo_img()
    self.logo.setParent(self)

    self.b = self.b_img()
    self.b.setParent(self)

    self.welcome = self.welcome_text()
    self.welcome.setParent(self)

    self.linkah = self.linkah_text()
    self.linkah.setParent(self)
    
    self.go_btn = self.go_btn()
    self.go_btn.setParent(self)
    self.go_btn.pressed.connect(self.press)
    self.go_btn.clicked.connect(self.click)

  def click(self):
    self.switch_window.emit()

  def press(self):
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("./graphics/chevron_depressed.png"), QtGui.QIcon.Normal, QtGui.QIcon.On),
    self.go_btn.setIcon(icon)

  def logo_img(self):
    Logo = QtWidgets.QLabel('')
    Logo.setGeometry(QtCore.QRect(700, 40, 256, 256))
    Logo.setObjectName("Logo")
    Logo.setText("<html><head/><body><p><img src=\"./graphics/logo_256x256.png\"/></p></body></html>")
    return Logo

  def b_img(self):
    B = QtWidgets.QLabel('')
    B.setGeometry(QtCore.QRect(40, 130, 200, 200))
    B.setObjectName("B")
    B.setText("<html><head/><body><p><img src=\"./graphics/b_200x200.png\"/></p></body></html>")
    return B

  def welcome_text(self):
    WelcomeTo = QtWidgets.QLineEdit('Welcome To:')
    WelcomeTo.setGeometry(QtCore.QRect(30, 10, 571, 121))
    font = QtGui.QFont()
    font.setFamily("Papyrus")
    font.setPointSize(72)
    WelcomeTo.setFont(font)
    WelcomeTo.setStyleSheet("QLineEdit{\n"
    "    color: rgb(214, 58, 25);\n"
    "    background-color: rgba(255, 255, 255, 0);\n"
    "    border: 0px;\n"
    "    border-color: rgba(255, 255, 255, 0);\n"
    "}")
    WelcomeTo.setReadOnly(True)
    WelcomeTo.setObjectName("WelcomeTo")
    return WelcomeTo

  def linkah_text(self):
    Linkah = QtWidgets.QLineEdit('LINKAH')
    Linkah.setGeometry(QtCore.QRect(250, 170, 421, 121))
    font = QtGui.QFont()
    font.setFamily("Arial")
    font.setPointSize(86)
    Linkah.setFont(font)
    Linkah.setStyleSheet("QLineEdit{\n"
      "    color: rgb(0, 0, 0);\n"
      "    background-color: rgba(255, 255, 255, 0);\n"
      "    border: 0px;\n"
      "    border-color: rgba(255, 255, 255, 0);\n"
      "}")
    Linkah.setReadOnly(True)
    Linkah.setObjectName("LINKAH")
    return Linkah

  def go_btn(self):
    go_btn = QtWidgets.QPushButton('')
    go_btn.setEnabled(True)
    go_btn.setGeometry(QtCore.QRect(600, 300, 200, 200))
    go_btn.setStyleSheet("QPushButton {\n"
    "    background-color: rgba(255, 255, 255, 0);\n"
    "    border: 0px;\n"
    "}")
    go_btn.setText("")
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("./graphics/chevron.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
    go_btn.setIcon(icon)
    go_btn.setIconSize(QtCore.QSize(128, 128))
    go_btn.setObjectName("go_btn")

    return go_btn

class NavPage(QtWidgets.QWidget):

  switch_window = QtCore.pyqtSignal()

  def __init__(self):
    QtWidgets.QWidget.__init__(self)
    self.setGeometry(QtCore.QRect(0,0,1024,600))
    self.setWindowTitle("COPYRIGHT BLINKAH 2021-2069")
    #self.setWindowIcon(QtGui.QIcon("./graphics/B.png"))

    # Enable borderless windowed
    flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
    self.setWindowFlags(flags)

    self.bkg_img = self.bkg_img()
    self.bkg_img.setParent(self)

    self.go_btn = self.go_btn()
    self.go_btn.setParent(self)
    self.go_btn.pressed.connect(self.press)
    self.go_btn.clicked.connect(self.click)

  def click(self):
    self.switch_window.emit()

  def press(self):
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("./graphics/chevron_depressed.png"), QtGui.QIcon.Normal, QtGui.QIcon.On),
    self.go_btn.setIcon(icon)

  def bkg_img(self):
    BkgImg = QtWidgets.QLabel('')
    BkgImg.setGeometry(QtCore.QRect(0, -100, 1024, 700))
    BkgImg.setObjectName("BkgImg")
    BkgImg.setText("<html><head/><body><p><img src=\"./graphics/vis.png\"/></p></body></html>")
    return BkgImg

  def go_btn(self):
    go_btn = QtWidgets.QPushButton('')
    go_btn.setEnabled(True)
    go_btn.setGeometry(QtCore.QRect(600, 300, 200, 200))
    go_btn.setStyleSheet("QPushButton {\n"
    "    background-color: rgba(255, 255, 255, 0);\n"
    "    border: 0px;\n"
    "}")
    go_btn.setText("")
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("./graphics/chevron.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
    go_btn.setIcon(icon)
    go_btn.setIconSize(QtCore.QSize(128, 128))
    go_btn.setObjectName("go_btn")

    return go_btn

class Controller:

  def __init__(self):
    pass

  def show_HomePage(self):
    self.HomePage = HomePage()
    self.HomePage.switch_window.connect(self.HomePage_to_NavPage)
    self.HomePage.show()

  def show_main(self):
    self.window = MainWindow()
    self.window.switch_window.connect(self.show_NavPage)
    self.HomePage.close()
    self.window.close()

  def HomePage_to_NavPage(self):
    self.NavPage = NavPage()
    self.NavPage.switch_window.connect(self.NavPage_to_HomePage)
    self.NavPage.show()
    time.sleep(.1)
    self.HomePage.close()

  def NavPage_to_HomePage(self):
    self.HomePage = HomePage()
    self.HomePage.switch_window.connect(self.HomePage_to_NavPage)
    self.HomePage.show()
    time.sleep(.1)
    self.NavPage.close()

def main():
  app = QtWidgets.QApplication(sys.argv)
  controller = Controller()
  controller.show_HomePage()
  sys.exit(app.exec_())

if __name__ == '__main__':
  main()