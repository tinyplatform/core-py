from PySide6.QtCore import QSize, Qt, QDir
from Application import *

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QTabWidget, QWidget, QMainWindow, QTreeView, QVBoxLayout, QFileSystemModel

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        treeModel = QFileSystemModel()
        treeModel.setRootPath(QDir.currentPath())

        treeView = QTreeView()
        treeView.setModel(treeModel)

        layout = QVBoxLayout(self)
        layout.addWidget(treeView)
        self.setLayout(layout)

class TestApp(Application):
    app_ID = 'test'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        print('NEW APP INSTANCE')
        print(self.app_ID, self.configuration_version, self.app_version)

        self.mainWindow = MyWindow()
        self.mainWindow.show()

app = TestApp()
exit(app.exec())