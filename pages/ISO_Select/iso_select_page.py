# PySide components
from PySide2.QtCore import Qt, QProcess, QFileSelector
from PySide2.QtWidgets import (
	QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QPushButton, QCheckBox, QLineEdit
)

# Import pages
from pages.ISO_Select.select_os import SelectOsCont
#from pages.ISO_Select.os_info import OsInfo

# ISO selection container
class IsoSelectPage(QWidget):
	def __init__(self):
		super().__init__()

		# Layout for the whole page
		rootLayout = QVBoxLayout()
		self.setLayout(rootLayout)

		selectOsOnCont = SelectOsCont()
		rootLayout.addWidget(selectOsOnCont)

		# osInfo = OsInfo()
		# rootLayout.addWidget(osInfo)
