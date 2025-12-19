# helper tools for the ticore platform
import os

def is_running_windows():
    return os.name == 'nt'

def get_userdata_root():
    if is_running_windows():
        return os.getenv('LOCALAPPDATA')
    else:
        return '~'

def get_tidata_root():
    return os.path.join(get_userdata_root(), '.ti')