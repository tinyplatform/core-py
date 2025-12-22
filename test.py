from Application import *

from PySide6.QtWidgets import QWidget

class TestApp(Application):
    app_ID = 'test'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        print('NEW APP INSTANCE')
        print(self.app_ID, self.configuration_version, self.app_version)

app = TestApp()

window = QWidget()
window.show()

app.aboutQt()
exit(app.exec())