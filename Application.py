from PySide6.QtWidgets import QApplication

from Version import Version
from configuration.Config import Config
import helpers, os

class Application(QApplication):
    app_ID: str = 'DEV'
    configuration_version: int = 1
    app_version: Version = Version()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # TODO: config
        self.config = Config(os.path.join(helpers.get_tidata_root(), self.app_ID, 'config.json'))
