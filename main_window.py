# PySide widgets
from PySide2.QtWidgets import QMainWindow, QWidget, QHBoxLayout

# Get sections
from sections.Drive_Info import SelectDrive
from sections.ISO_Select import IsoSelect

# Main application window
class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("QEngrave")

		root = QWidget()
		rootLayout = QHBoxLayout()
		root.setLayout(rootLayout)

		selectDrive = SelectDrive()
		selectISO = IsoSelect()

		rootLayout.addWidget(selectDrive)
		rootLayout.addWidget(selectISO)

		self.setCentralWidget(root)
