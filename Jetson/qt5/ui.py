import sys, time
from PyQt5 import QtCore, QtWidgets, QtGui
from alpr import alpr

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
    WelcomeTo = QtWidgets.QLabel('Welcome To:')
    WelcomeTo.setGeometry(QtCore.QRect(30, 10, 571, 121))
    font = QtGui.QFont()
    font.setFamily("Loma")
    font.setPointSize(72)
    WelcomeTo.setFont(font)
    WelcomeTo.setStyleSheet(
      "color: rgb(214, 58, 25);"
      "background-color: rgba(255, 255, 255, 0);"
      "border: 0px;\n"
      "border-color: rgba(255, 255, 255, 0);"
    )
    WelcomeTo.setObjectName("WelcomeTo")
    return WelcomeTo

  def linkah_text(self):
    Linkah = QtWidgets.QLabel('LINKAH')
    Linkah.setGeometry(QtCore.QRect(250, 170, 421, 121))
    font = QtGui.QFont()
    font.setFamily("Loma")
    font.setPointSize(86)
    Linkah.setFont(font)
    Linkah.setStyleSheet(
      "color: rgb(0, 0, 0);"
      "background-color: rgba(255, 255, 255, 0);"
      "border: 0px;"
      "border-color: rgba(255, 255, 255, 0);"
    )
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

    #self.bkg_img = self.bkg_img()
    #self.bkg_img.setParent(self)

    self.car_num = 0
    

    self.car_img = self.car_img()
    self.car_img.setParent(self)

    self.plate_reading = self.plate_reading()
    self.plate_reading.setParent(self)

    self.alpr_btn = self.alpr_btn()
    self.alpr_btn.setParent(self)
    self.alpr_btn.pressed.connect(self.press_alpr)
    self.alpr_btn.clicked.connect(self.click_alpr)

    self.go_btn = self.go_btn()
    self.go_btn.setParent(self)
    self.go_btn.pressed.connect(self.press_go)
    self.go_btn.clicked.connect(self.click_go)




  def press_go(self):
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("./graphics/chevron_depressed.png"), QtGui.QIcon.Normal, QtGui.QIcon.On),
    self.go_btn.setIcon(icon)

  def click_go(self):
    self.switch_window.emit()

  def press_alpr(self):
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("./graphics/chevron_depressed.png"), QtGui.QIcon.Normal, QtGui.QIcon.On),
    self.alpr_btn.setIcon(icon)

  def click_alpr(self):
    self.car_num += 1
    self.runALPR(str(self.car_num))

  def bkg_img(self):
    BkgImg = QtWidgets.QLabel('')
    BkgImg.setGeometry(QtCore.QRect(0, -100, 1024, 700))
    BkgImg.setObjectName("BkgImg")
    BkgImg.setText("<html><head/><body><p><img src=\"./graphics/vis.png\"/></p></body></html>")
    return BkgImg

  def car_img(self):
    CarImg = QtWidgets.QLabel('')
    CarImg.setGeometry(QtCore.QRect(0,0,500,375))
    CarImg.setObjectName("PlateImg")
    CarImg.setText("<html><head/><body><p><img src=\"./graphics/vis.png\"/></p></body></html>")

    #CarImg.setText("<html><head/><body><p><img src=\""+'2'+"\"/></p></body></html>")
    return CarImg
  
  def plate_reading(self):
    PlateReading = QtWidgets.QLabel('')
    PlateReading.setGeometry(QtCore.QRect(500,0,500,375))
    PlateReading.setObjectName("PlateImg")
    font = QtGui.QFont()
    font.setFamily("Loma")
    font.setPointSize(72)
    PlateReading.setFont(font)
    PlateReading.setStyleSheet("color: red")
   
    return PlateReading


  def go_btn(self):
    go_btn = QtWidgets.QPushButton('')
    go_btn.setEnabled(True)
    go_btn.setGeometry(QtCore.QRect(600, 300, 200, 200))
    go_btn.setStyleSheet("QPushButton {\n"
    "    background-color: rgba(255, 255, 255, 0);\n"
    "    border: 0px;\n"
    "}")
    go_btn.setText('')
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("./graphics/chevron.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
    go_btn.setIcon(icon)
    go_btn.setIconSize(QtCore.QSize(128, 128))
    go_btn.setObjectName("go_btn")

    return go_btn

  def alpr_btn(self):
    alpr_btn = QtWidgets.QPushButton('')
    alpr_btn.setEnabled(True)
    alpr_btn.setGeometry(QtCore.QRect(200, 300, 200, 200))
    alpr_btn.setStyleSheet("QPushButton {\n"
    "    background-color: rgba(255, 255, 255, 0);\n"
    "    border: 0px;\n"
    "}")
    alpr_btn.setText('')
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("./graphics/chevron.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
    alpr_btn.setIcon(icon)
    alpr_btn.setIconSize(QtCore.QSize(128, 128))
    alpr_btn.setObjectName("alpr_btn")

    return alpr_btn

  def runALPR(self, num):
    plates = alpr(num)
    plate = plates[0].get('license_plate')
    print(plate)
    self.plate_reading.setText(plate)
    pic_url = "sample_data/car"+num+".jpg"
    self.car_img.setText("<html><head/><body><p><img src=\""+pic_url+"\"/></p></body></html>")
    return plate

# Defines connections between pages
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