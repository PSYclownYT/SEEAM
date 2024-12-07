import sys
import os
import playsound
from PyQt5 import QtGui, QtCore, uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import playsound
import threading

def play_sound(sound_file):
    playsound.playsound(sound_file)
    mywindow.close()
    os.system('python launcher.py')

# Example usage
sound_file = "assets\seeamstart.mp3"  # Replace with your actual sound file path
thread = threading.Thread(target=play_sound, args=(sound_file,))


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        label = QtWidgets.QLabel(self)
        pixmap = QtGui.QPixmap('assets\SeeamLogo.png')
        label.setPixmap(pixmap)
        self.setCentralWidget(label)
        self.resize(pixmap.width(), pixmap.height())

        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.X11BypassWindowManagerHint
        )
    
    

    

app = QApplication(sys.argv)
mywindow = MainWindow()
mywindow.show()
thread.start()
app.exec()
