# PySide components
from PySide2.QtCore import Qt, QProcess, QFileSelector
from PySide2.QtWidgets import (
	QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QPushButton, QCheckBox, QLineEdit
)

from pages.ISO_Select.select_os_online import SelectOsOnCont

# ISO selection container
class IsoSelectPage(QWidget):
	def __init__(self):
		super().__init__()

		# Layout for the whole page
		rootLayout = QVBoxLayout()

		selectOsOnCont = SelectOsOnCont()
		rootLayout.addWidget(selectOsOnCont)
		self.setLayout(rootLayout)


		# IsoLayout = QVBoxLayout()
		# self.setLayout(IsoLayout)
  #
		# self.setTitle("Select ISO")
  #
		# # Line containing path to selected file
		# ISOFileLine = QLineEdit()
  #
		# # Button to select ISO file
		# selectIsoBtn = QPushButton("Select")
		# selectIsoBtn.clicked.connect(lambda : selectFile(ISOFileLine))
  #
		# IsoLayout.addWidget(selectIsoBtn)
		# IsoLayout.addWidget(ISOFileLine)


