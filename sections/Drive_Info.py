import PySide2
from PySide2.QtCore import Qt, QProcess, QFileSelector
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import (
		QWidget, QLabel, QPushButton, QCheckBox, QGroupBox, QVBoxLayout,
		QHBoxLayout, QComboBox
	)

from tools.SysTools import getDrives

class SelectDrive(QGroupBox):
	def __init__(self):
		super().__init__()

		rootLayout = QVBoxLayout()
		self.setLayout(rootLayout)
		self.setTitle("Select Drive")

		topBar = QWidget()
		topBarLayout = QHBoxLayout()
		topBar.setLayout(topBarLayout)

		refreshBtn = QPushButton(QIcon().fromTheme("view-refresh"), "Refresh")
		showAllCheck = QCheckBox("show all drives")

		refreshBtn.clicked.connect(
			lambda: self.refreshDrives(showAllCheck.isChecked())
		)
		showAllCheck.stateChanged.connect(
			lambda: self.refreshDrives(showAllCheck.isChecked())
		)

		topBarLayout.addWidget(refreshBtn)
		topBarLayout.addWidget(showAllCheck)

		self.deviceCBox = QComboBox()
		self.deviceCBox.currentTextChanged.connect(lambda: self.refreshInfo())

		self.currDriveInfo = QGroupBox("Drive Info")
		self.currDriveInfoLayout = QVBoxLayout()
		self.currDriveInfo.setLayout(self.currDriveInfoLayout)

		rootLayout.addWidget(topBar)
		rootLayout.addWidget(self.deviceCBox)
		rootLayout.addWidget(self.currDriveInfo)

		self.refreshDrives(showAllCheck.isChecked())

	def refreshDrives(self, showAll):
		self.deviceCBox.clear()

		drives = getDrives(showAll=showAll)
		for drive in drives:
			info = {
				"name": drive["label"],
				"location": drive["name"],
				"size": drive["size"],
				"vendor": drive["vendor"],
				"removable": drive["rm"]
			}
			self.deviceCBox.addItem(f"{drive['label']} ({drive['name']})", info)
			#print(drive)

		self.refreshInfo()

	def refreshInfo(self):
		print(">>> ", self.currDriveInfoLayout.count())

		def clearLayout():
			if self.currDriveInfoLayout is not None:
				while self.currDriveInfoLayout.count():
					item = self.currDriveInfoLayout.takeAt(0)
					widget = item.widget()
					if widget is not None:
						widget.deleteLater()
					else:
						self.clearLayout(item.layout())
		clearLayout()

		oldInfo = self.deviceCBox.currentData()

		if(not isinstance(oldInfo, type(None))):
			info = {
				"Name": oldInfo["name"],
				"Location": oldInfo["location"],
				"Size": oldInfo["size"],
				"Vendor": oldInfo["vendor"],
				"Removable": oldInfo["removable"]
			}

			for key in info.keys():
				infoLabel = QLabel(f"{key}: {info[f'{key}']}")
				self.currDriveInfoLayout.addWidget(infoLabel)

	def printData(self):
		print(self.deviceCBox.currentText())
		print(self.deviceCBox.currentData())
