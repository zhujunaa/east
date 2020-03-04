from PyQt5 import QtGui
import sys
from PyQt5 import *
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtWidgets import QApplication, qApp

from pyqt.MainWindow import MainWindow

if __name__ == '__main__':
    names = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
    new_names = [name.upper() for name in names if len(name) > 3]
    print(new_names)
    # return
    #
    # ['ALICE', 'JERRY', 'WENDY', 'SMITH']
    # app = QApplication(sys.argv)
    # QApplication.setQuitOnLastWindowClosed(True)
    # file = QFile("dev.css");
    # if (file.open(QFile.ReadOnly)):
    #     styleIn = QTextStream(file)
    #     qss = styleIn.readAll()
    #     qApp.setStyleSheet(qss)
    #     file.close()
    # w = MainWindow()
    # w.showMaximized();
    # sys.exit(app.exec_())

