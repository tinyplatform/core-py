# global and local configuratitoon system for the ticore platform
import helpers
import json, os

# note:
# the indentation when dumping is intentional, because even if the user should be able to configure their program graphically,
# the task of manually configuring their options via the file should be made easy.

class Configuration:
    def __init__(self, app_name: str, app_display_name: str = "", default_config: dict = {}):
        """Configuration manager. Housed in the .ti directory for your system.

        Args:
            app_name (str): internal application name (e.g. fm, clock, bu, git...)
            app_display_name (str, optional): external application name. Defaults to "ti" + app_name. Only uied once, when the application is first installed.
            default_config (dict, optional): the default configuration layout 
        """

        self.app_name = app_name
        if app_display_name == "":
            self.app_display_name = "ti" + self.app_name

        self.cf_dir = os.path.join(helpers.get_tidata_root(), app_name)
        if not os.path.isdir(self.cf_dir):
            os.makedirs(self.cf_dir)

        self.cf_path = os.path.join(self.cf_dir, 'config.json')
        if not os.path.exists(self.cf_path):
            with open(self.cf_path, 'w') as f:
                f.write(json.dumps(default_config, indent=4))
        with open(self.cf_path, 'r') as f:
            self.config = json.load(f)
    
    def read_config(self) -> dict:
        """Read the config file for the application and load it into `self.config`.

        Returns:
            dict: the configuration options
        """
        with open(self.cf_path, 'r') as f:
            self.config = json.load(f)
        return self.config
    
    def write_config(self) -> None:
        """Write the configuration options to the config file.
        """
        with open(self.cf_path, 'w') as f:
            f.write(json.dumps(self.config, indent=4))