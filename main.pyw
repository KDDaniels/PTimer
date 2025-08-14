#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QApplication
from main_window import MainWindow

def run():
    app = QApplication([])
    win = MainWindow()
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run()