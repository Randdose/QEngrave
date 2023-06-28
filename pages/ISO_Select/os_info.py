# PySide components
from PySide2.QtWidgets import (
	QWidget, QPushButton, QLineEdit, QComboBox, QLabel, QGroupBox,
	QHBoxLayout, QVBoxLayout, QGridLayout
)
from PySide2.QtGui import QPixmap
from PySide2.QtCore import QSize
import PySide2

class OsInfo(QGroupBox):
	def __init__(self):
		super().__init__()

		rootLayout = QGridLayout()
		self.setLayout(rootLayout)

		imgSrc = "/home/random/Downloads/231032376_5118306298292699_4037784113179645605_n"
		imgMap = QPixmap(imgSrc)
		size = QSize(100,100)
		imgMap.scaled(size)
		img = QLabel()
		img.setPixmap(imgMap)
		img.setScaledContents(True)

		rootLayout.addWidget(img, 0, 0, 2, 2)
