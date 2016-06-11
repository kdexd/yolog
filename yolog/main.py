import os
import sys
from yolog.yolog_generator import YologGenerator

yolog_gen = YologGenerator()


def main():
    git_arguments = sys.argv[1:]
    os.system(yolog_gen.git_command(" ".join(git_arguments)))
