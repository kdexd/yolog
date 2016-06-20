from __future__ import print_function
from ConfigParser import SafeConfigParser
import os


class ConfigHandler(object):
    def __init__(self, path):
        self.path = os.path.expandvars(os.path.expanduser(path))
        self.config = SafeConfigParser()
        self.config.read(self.path)

    def set_color(self, attribute, color):
        if attribute not in {"author", "date", "description", "hash", "refs"}:
            print("{0}: Invalid attribute !".format(attribute))
        elif color.upper() not in {"WHITE", "BLACK", "RED", "GREEN",
                           "CYAN", "BLUE", "PURPLE", "YELLOW"}:
            print("{0}: Invalid color !".format(color))
        else:
            self.config.set("color", attribute, color.upper())
            with open(self.path, 'w') as f:
                self.config.write(f)
            print("Changed Successfully !")
