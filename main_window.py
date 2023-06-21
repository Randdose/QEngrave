# PySide widgets
from PySide2.QtWidgets import QMainWindow, QWidget, QStackedWidget, QStackedLayout

# Get pages for the page stack
from pages.ISO_Select.iso_select_page import IsoSelectPage
# from pages.select_drive import SelectDrive
# from pages.flash_info import FlashInfo

# Main application window
class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		pageStack = QWidget()
		stackedLayout = QStackedLayout()
		pageStack.setLayout(stackedLayout)

		self.setWindowTitle("KFlasher")

		isoSelectPage = IsoSelectPage()

		self.setCentralWidget(pageStack)

		stackedLayout.addWidget(isoSelectPage)
