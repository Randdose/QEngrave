# PySide widgets
from PySide2.QtWidgets import (
	QWidget, QPushButton, QLineEdit, QComboBox, QLabel, QGroupBox, QHBoxLayout,
	QVBoxLayout
)

from pages.ISO_Select.os_info import OsInfo

class SelectOsCont(QGroupBox):
	def __init__(self):
		super().__init__()

		rootLayout = QHBoxLayout()
		self.setLayout(rootLayout)

		selectOsBox = SelectOsBox()
		rootLayout.addWidget(selectOsBox)

		osInfoBox = OsInfoBox()
		rootLayout.addWidget(osInfoBox)

# GroupBox to select an OS
class SelectOsBox(QGroupBox):
	def __init__(self):
		super().__init__()

		self.setTitle("Select OS")

		layout = QVBoxLayout()
		self.setLayout(layout)

		OsNameEdit = LabeledEdit("Drive name:")
		layout.addWidget(OsNameEdit)

		ArchOptions = ComboBox([
			"64bit", "32bit", "ARM"
		])
		layout.addWidget(ArchOptions)

class OsInfoBox(QGroupBox):
	def __init__(self):
		super().__init__()

		self.setTitle("OS Info")

		layout = QVBoxLayout()
		self.setLayout(layout)

		osInfo = OsInfo()
		layout.addWidget(osInfo)
		#self.OsImagPixDir = "/"


# Components
#* QLineEdit, with a QLabel, inside a QWidget. Basically.
class LabeledEdit(QWidget):
	def __init__(self, labelTxt):
		super().__init__()

		layout = QHBoxLayout()
		self.setLayout(layout)

		self.lineLabel = QLabel(labelTxt)
		self.lineEdit = QLineEdit()

		layout.addWidget(self.lineLabel)
		layout.addWidget(self.lineEdit)

#* QComboBox but sane
class ComboBox(QComboBox):
	def __init__(self, options):
		super().__init__()

		self.options = options

		for option in self.options:
			self.addItem(option)
