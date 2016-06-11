import os
from yolog.yolog_generator import YologGenerator

yolog_gen = YologGenerator()


def main():
	os.system(yolog_gen.git_command())
