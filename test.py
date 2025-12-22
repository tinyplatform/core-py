from Application import *

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QMainWindow

class TestApp(Application):
    app_ID = 'test'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        print('NEW APP INSTANCE')
        print(self.app_ID, self.configuration_version, self.app_version)

        self.mainWindow = QMainWindow()
        menuBar = self.mainWindow.menuBar()
        file = menuBar.addMenu("&File")

        self.mainWindow.show()

app = TestApp()
exit(app.exec())