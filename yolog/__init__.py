__author__ = "Karan Desai"
__email__ = "karandesai281196@gmail.com"
__version__ = "0.1.0"
__license__ = "MIT"

from yolog_generator import YologGenerator

yolog_gen = YologGenerator()


def configure():
	yolog_gen.set_gitconfig_alias()


def unconfigure():
	yolog_gen.unset_gitconfig_alias()
