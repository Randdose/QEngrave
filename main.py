# Qt bindings for python
from PySide2.QtCore import Qt, QProcess, QFileSelector
from PySide2.QtWidgets import (
	QApplication, QMainWindow, QWidget, QGroupBox, QPushButton, QProgressBar,
	QCheckBox, QComboBox, QVBoxLayout, QHBoxLayout, QFileDialog
)
from PySide2.QtGui import QIcon

# PySide Components
# from pages.select_iso import IsoSelect
from main_window import MainWindow

# System commands and tools
from sys import argv
from blkinfo import BlkDiskInfo

app = QApplication(argv)

# Simplified System tools and commands
from tools.SysTools import *

# Assign main window and show it
window = MainWindow()
window.show()

# Start app (or event loop)
app.exec_()
