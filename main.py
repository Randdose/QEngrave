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



"""
class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("KFlasher")

		# Root Widget contains everything in this window
		root = QWidget()
		rootLayout = QVBoxLayout()
		root.setLayout(rootLayout)

		# Container for the select ISO and select drive boxes
		stepsCont = QWidget()
		stepsContLayout = QHBoxLayout()
		stepsCont.setLayout(stepsContLayout)

		ISOSelect = IsoSelect()

		stepsContLayout.addWidget(ISOSelect)

		flashSelectCont = QGroupBox("Select Drive")
		flashSelectLayout = QVBoxLayout()
		flashSelectCont.setLayout(flashSelectLayout)

		flashOptions = QGroupBox()
		flashOptionsLayout = QHBoxLayout()
		flashOptions.setLayout(flashOptionsLayout)

		refreshIcon = QIcon.fromTheme("view-refresh")
		refreshBtn = QPushButton("refresh")
		refreshBtn.setIcon(refreshIcon)
		refreshBtn.clicked.connect(lambda: checkFlashDrives(usbdevices))

		flashOptionsLayout.addWidget(refreshBtn)

		showAllDevicesCheck = QCheckBox("show all devices")
		showAllDevicesCheck.stateChanged.connect(lambda: checkFlashDrives(usbdevices))

		flashOptionsLayout.addWidget(showAllDevicesCheck)

		flashSelectLayout.addWidget(flashOptions)

		currentDrive = "this"

		flashDropDown = QComboBox()
		flashDropDown.currentTextChanged.connect(lambda: checkCurrentDrive(currentDrive))

		stepsContLayout.addWidget(flashSelectCont)
		rootLayout.addWidget(stepsCont)

		flashSelectLayout.addWidget(flashDropDown)

		self.setCentralWidget(root)

		def checkCurrentDrive(var):
			var = flashDropDown.currentText()
			print(var)

		def checkFlashDrives(var):
			myblkd = BlkDiskInfo()
			flashDropDown.clear()

			if(showAllDevicesCheck.isChecked()):
				filters = {}
			else:
				filters = {
					"rm": True,
					"hotplug": True
				}

			filteredDisks = myblkd.get_disks(filters)
			print(filteredDisks)

			for disk in filteredDisks:
				var[f"{disk['label']}"] = dict(name = f"{disk['label']}", size = f"{disk['size']}", location = f"{disk['name']}")
				flashDropDown.insertItem(0, f"{disk['label']}")
				#print(f"{disk['label']}")

		usbdevices = {}
		checkFlashDrives(usbdevices)

		flashButton = QPushButton("Flash!")
		flashButton.clicked.connect(lambda: self.startFlash(currentDrive))#flashDropDown.currentText(), usbdevices, ISOFileLine.text()))
		rootLayout.addWidget(flashButton)

		# flash = QProcess(self)#MainWindow)
		# flash.setProgram(f"pkexec dd if={iso} of=/dev/{location}")
		# flash.finished.connect(print("finished flashing"))
		# flash.start()

		progressBar = QProgressBar()
		progressBar.setFormat("")
		progressBar.setMinimum(0)
		progressBar.setMaximum(100)
		rootLayout.addWidget(progressBar)

		checkCurrentDrive(currentDrive)

	def selectFile(self, lineEdit):
		dial = QFileDialog.getOpenFileName(self, "Open ISO file", commandOutput("echo $HOME"), "ISO Files (*.iso)")

		lineEdit.setText(dial[0])

	def startFlash(self, CD): #flashOption, devicesList, iso):
		print(CD)
		#flash.start()
	# 	usb = devicesList[flashOption]
	# 	location = usb["location"]
	# 	print(f"dd if='{iso}' of='/dev/{location}' status=progress")
	# 	runCommand(f"dd if='{iso}' of='/dev/{location}' status=progress", 1, 1)
	#	commandOutput(f"dd if='{iso}' | pv | of='/dev/{location}'", 1)
"""

# Assign main window and show it
window = MainWindow()
window.show()

# Start app (or event loop)
app.exec_()
