# PySide widgets
from PySide2.QtWidgets import (
	QWidget, QPushButton, QLineEdit, QComboBox, QLabel, QComboBox, QGroupBox,
	QHBoxLayout, QVBoxLayout
)

class SelectOsOnCont(QGroupBox):
	def __init__(self):
		super().__init__()

		self.setTitle("Online Installation")

		rootLayout = QHBoxLayout()
		self.setLayout(rootLayout)

		selectOsBox = SelectOsBox()
		rootLayout.addWidget(selectOsBox)

# GroupBox to select an OS
class SelectOsBox(QGroupBox):
	def __init__(self):
		super().__init__()

		self.setTitle("Select OS")

		layout = QVBoxLayout()
		self.setLayout(layout)

		OsNameEdit = LabeledEdit("OS Name:")
		layout.addWidget(OsNameEdit)

		ArchOptions = ComboBox([
			"64bit", "32bit", "ARM"
		])
		layout.addWidget(ArchOptions)

# Components

#* QLineEdit, with a QLabel, inside a QWidget. Basically.
class LabeledEdit(QWidget):
	def __init__(self, labelTxt):
		super().__init__()

		layout = QHBoxLayout()
		self.setLayout(layout)

		lineLabel = QLabel(labelTxt)
		lineEdit = QLineEdit()

		layout.addWidget(lineLabel)
		layout.addWidget(lineEdit)

#* QComboBox but sane
class ComboBox(QComboBox):
	def __init__(self, options):
		super().__init__()

		for o in options:
			self.addItem(o)
