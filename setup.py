import os
import shutil
import sys
from setuptools import setup

config_dirpath = os.path.expandvars(os.path.expanduser("~/.yolog"))

if os.path.exists(config_dirpath):
    shutil.rmtree(config_dirpath)

if sys.argv[1] in {"build", "install", "develop"}:
    os.mkdir(config_dirpath)

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
