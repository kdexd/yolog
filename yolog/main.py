from __future__ import print_function
import os
import sys
from yolog.yolog_generator import YologGenerator

yolog_gen = YologGenerator()

help_description = ("""
Yolog - Beautify your Git logs !
--------------------------------
Usage: yolog [<additional optional commands>]

1. yolog -n
-      Display recent n commits.

2. yolog --skip=n
-      Skip recent n commits and display further.

3. yolog --author=john
-      Filter commits according to author.
       Part of name / whole will be accepted.

4. yolog --before=dd-mmm-yyyy
   yolog --until=dd/mmm/yyyy
-      Display commits before this date.

5. yolog --after=dd/mmm/yyyy
   yolog --since=dd-mmm-yyyy
-      Display commits after this date.

6. yolog --grep="foo\ bar"
-      Display commits with "foo bar" in their description.

7. yolog --help
   yolog -h
-      Display this instruction.

* Any of these can be combined together and used.
* Regular expressions are also accepted in grep and author.
* Use escape character if using whitespace: yolog --grep="fixes\ bug"
""")


def main():
    git_arguments = sys.argv[1:]
    if git_arguments and (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
        print(help_description)
    else:
        os.system(yolog_gen.git_command(" ".join(git_arguments)))
