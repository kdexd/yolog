from __future__ import print_function
import os
import shutil
import sys
from setuptools import setup
try:
    from ConfigParser import SafeConfigParser
except ImportError:
    from configparser import SafeConfigParser

config_dirpath = os.path.expandvars(os.path.expanduser("~/.yolog"))

if os.path.exists(config_dirpath):
    shutil.rmtree(config_dirpath)

if sys.argv[1] in {"build", "install", "develop"}:
    os.mkdir(config_dirpath)
    config = SafeConfigParser()
    config.add_section('color')
    config.set('color', 'hash', 'YELLOW')
    config.set('color', 'author', 'BLUE')
    config.set('color', 'date', 'GREEN')
    config.set('color', 'refs', 'RED')
    config.set('color', 'description', 'WHITE')
    with open(os.path.join(config_dirpath, 'config.ini'), 'w') as f:
        config.write(f)

setup(
    name='yolog',
    version=__import__('yolog').__version__,
    description=__import__('yolog').__description__,
    url=__import__('yolog').__url__,
    author=__import__('yolog').__author__,
    author_email=__import__('yolog').__email__,
    license=__import__('yolog').__license__,
    packages=['yolog'],
    entry_points={
        'console_scripts': ['yolog = yolog.main:main']
    },
    zip_safe=True
)

print("If you installed with sudo privileges, current owner of ~/.yolog directory "
      "would be root. Please change the owner to user for better experience. ")
