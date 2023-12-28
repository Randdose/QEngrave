from PySide2.QtCore import Qt, QProcess, QFileSelector
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import (
	QWidget, QLabel, QPushButton, QCheckBox, QLineEdit, QGroupBox, QVBoxLayout,
	QHBoxLayout, QComboBox, QFileDialog
)

from tools.SysTools import getDrives, commandOutput

import os

class IsoSelect(QGroupBox):
	def __init__(self):
		super().__init__()

		rootLayout = QVBoxLayout()
		self.setLayout(rootLayout)
		self.setTitle("Select ISO")

		IsoSelectCont = QWidget()
		IsoSelectContLayout = QHBoxLayout()
		IsoSelectCont.setLayout(IsoSelectContLayout)

		self.IsoSelectLine = QLineEdit()
		IsoSelectBtn = QPushButton(QIcon().fromTheme("document-open"), None)

		IsoSelectBtn.clicked.connect(lambda: self.getIso())

		IsoSelectContLayout.addWidget(self.IsoSelectLine)
		IsoSelectContLayout.addWidget(IsoSelectBtn)

		self.IsoInfo = QGroupBox("ISO Info")
		self.IsoInfoLayout = QVBoxLayout()
		self.IsoInfo.setLayout(self.IsoInfoLayout)

		rootLayout.addWidget(IsoSelectCont)
		rootLayout.addWidget(self.IsoInfo)

		try:
		 self.refreshInfo()
		except:
			print("1")

	def getInfo(self):

		def clearInfoBox():
			if self.IsoInfoLayout is not None:
				while self.IsoInfoLayout.count():
					item = self.IsoInfoLayout.takeAt(0)
					widget = item.widget()
					if widget is not None:
						widget.deleteLater()
					else:
						self.clearLayout(item.layout())
		clearInfoBox()

		stat = os.stat(self.IsoSelectLine.text())
		info = {
			"Size": stat.st_size
		}
		readableInfo = {
			"Size": f"{round(int(stat.st_size) / 1073742000, 2)} GiB" if int(stat.st_size) > 1073742000 else f"{round(int(stat.st_size) / 1048576, 2)} MiB"
		}

		for key in readableInfo.keys():
				infoLabel = QLabel(f"{key}: {readableInfo[f'{key}']}")
				self.IsoInfoLayout.addWidget(infoLabel)

	def getIso(self):
		dial = QFileDialog
		fileName = dial.getOpenFileName(
			self, "open ISO file", commandOutput("echo $HOME"), "ISO files (*.iso)"
		)
		self.IsoSelectLine.setText(fileName[0])
		self.getInfo()
