# Qt bindings for python
from PySide2.QtCore import Qt, QFileSelector
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QGroupBox, QPushButton, QLineEdit, QCheckBox, QComboBox, QVBoxLayout, QHBoxLayout, QFileDialog
from PySide2.QtGui import QIcon

# Simplified System tools and commands
from tools.SysTools import *

# System commands and tools
from sys import argv
from blkinfo import BlkDiskInfo

app = QApplication(argv)

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("KFlasher")

		# Root Widget contains everything in this window
		root = QWidget()
		rootLayout = QVBoxLayout()
		root.setLayout(rootLayout)

		contCont = QWidget()
		contContLayout = QHBoxLayout()
		contCont.setLayout(contContLayout)

		# ISO Select container
		ISOSelectCont = QGroupBox("Select ISO")
		ISOSelectLayout = QVBoxLayout()
		ISOSelectCont.setLayout(ISOSelectLayout)

		contContLayout.addWidget(ISOSelectCont)

		# Line containing path to selected file
		ISOFileLine = QLineEdit()

		# Button to select ISO file
		selectIsoBtn = QPushButton("Select")
		selectIsoBtn.clicked.connect(lambda : self.selectFile(ISOFileLine))

		ISOSelectLayout.addWidget(ISOFileLine)
		ISOSelectLayout.addWidget(selectIsoBtn)

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

		flashDropDown = QComboBox()

		contContLayout.addWidget(flashSelectCont)
		rootLayout.addWidget(contCont)

		flashSelectLayout.addWidget(flashDropDown)

		self.setCentralWidget(root)

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

			for disk in filteredDisks:
				var[f"{disk['label']}"] = dict(name = f"{disk['label']}", size = f"{disk['size']}", location = f"{disk['name']}")
				flashDropDown.insertItem(0, f"{disk['label']}")

		usbdevices = {}
		checkFlashDrives(usbdevices)

		flashButton = QPushButton("Flash!")
		flashButton.clicked.connect(lambda: self.flash(flashDropDown.currentText(), usbdevices, ISOFileLine.text()))
		rootLayout.addWidget(flashButton)

	def selectFile(self, lineEdit):
		dial = QFileDialog.getOpenFileName(self, "Open ISO file", commandOutput("echo $HOME"), "ISO Files (*.iso)")

		lineEdit.setText(dial[0])

	def flash(self, flashOption, devicesList, iso):
		usb = devicesList[flashOption]
		location = usb["location"]
		print(f"dd if='{iso}' of='/dev/{location}' status=progress")
		runCommand(f"dd if='{iso}' of='/dev/{location}' status=progress", 1, 1)
		#commandOutput(f"dd if='{iso}' | pv | of='/dev/{location}'", 1)

# Assign main window and show it
window = MainWindow()
window.show()

# Start app (or event loop)
app.exec_()
