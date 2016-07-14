from __future__ import print_function
import os
try:
    from ConfigParser import SafeConfigParser
except ImportError:
    from configparser import SafeConfigParser


class ConfigHandler(object):
    def __init__(self, path):
        self.path = os.path.expandvars(os.path.expanduser(path))

        self.config_parser = SafeConfigParser()
        self.config_parser.read(self.path)

        self.attributes = {'author', 'date', 'description', 'hash', 'refs'}
        self.colors = {'WHITE', 'BLACK', 'RED', 'YELLOW', 'GREEN', 'BLUE',
                       'CYAN', 'PURPLE'}

    def update_color(self, attribute, color):
        if attribute.lower() not in self.attributes:
            print("{0}: Invalid attribute !".format(attribute))
            print("Choose one of {0}.".format(self.attributes))
        elif color.upper() not in self.colors:
            print("{0}: Invalid color !".format(color))
            print("Choose one of {0}.".format(self.colors))
        else:
            self.config_parser.set("color", attribute.lower(), color.upper())

            with open(self.path, 'w') as f:
                self.config_parser.write(f)
            print("Updated {0} color of {1} attribute successfully !".format(
                color.upper(), attribute.lower()
            ))
