from __future__ import print_function
import os
import shutil
import sys
from setuptools import setup
from ConfigParser import SafeConfigParser

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
    version='0.2.2',
    description='Beautify your git logs!',
    url='http://github.com/karandesai-96/yolog',
    author='Karan Desai',
    author_email='karandesai281196@gmail.com',
    license='MIT',
    packages=['yolog'],
    entry_points={
        'console_scripts': ['yolog = yolog.main:main']
    },
    zip_safe=True
)

print("If you installed with sudo privileges, current owner of ~/.yolog directory "
      "would be root. Please change the owner to user for better experience. ")
