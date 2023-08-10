from PySide2.QtCore import Qt, QProcess, QFileSelector
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import (
	QWidget, QPushButton, QCheckBox, QLineEdit, QGroupBox, QVBoxLayout,
	QHBoxLayout, QComboBox, QFileDialog
	)
from tools.SysTools import getDrives

class IsoSelect(QGroupBox):
	def __init__(self):
		super().__init__()

		rootLayout = QVBoxLayout()
		self.setLayout(rootLayout)
		self.setTitle("Select ISO")

		IsoSelectCont = QWidget()
		IsoSelectContLayout = QHBoxLayout()
		IsoSelectCont.setLayout(IsoSelectContLayout)

		IsoSelectBtn = QPushButton(
			QIcon().fromTheme("document-open"), "Select ISO file"
		)
		IsoSelectLine = QLineEdit()

		IsoSelectBtn.clicked.connect(lambda: self.showFileDial())

		IsoSelectContLayout.addWidget(IsoSelectBtn)
		IsoSelectContLayout.addWidget(IsoSelectLine)

		rootLayout.addWidget(IsoSelectCont)

	def showFileDial(self):
		dial = QFileDialog
		fileName = dial.getOpenFileName(self, "open ISO file", "$HOME", "ISO files (*.iso)")
		print(fileName)
