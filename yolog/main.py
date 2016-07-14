from __future__ import print_function
import os
import sys
from yolog.yolog_generator import YologGenerator
from yolog.config_handler import ConfigHandler


def main():
    git_arguments = sys.argv[1:]
    config_filepath = '~/.yolog/config.ini'

    if git_arguments:
        if sys.argv[1] in {'-h', '--help', 'help'}:
            yolog_gen = YologGenerator(config_filepath)
            os.system(yolog_gen.print_help())

        elif sys.argv[1] in {'-c', '--config', 'config'}:
            config_handler = ConfigHandler(config_filepath)
            config_handler.update_color(sys.argv[2], sys.argv[3])

        else:
            yolog_gen = YologGenerator(config_filepath)
            os.system(yolog_gen.git_command(' '.join(git_arguments)))

    else:
        yolog_gen = YologGenerator(config_filepath)
        os.system(yolog_gen.git_command(' '))
