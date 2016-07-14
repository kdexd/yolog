import os
try:
    from ConfigParser import SafeConfigParser
except ImportError:
    from configparser import SafeConfigParser


RESET = "$(tput sgr0)"
BACKSPACE = "%x08"

help_description = ("""
{yellow}Yolog - Beautify your Git logs !
{white}================================
{cyan}Author: {author}
{cyan}Version: {version}
{cyan}Usage: yolog [-h|--help] [-c|--config attribute COLOR]
{cyan}             [<additional commands>]

{yellow}HELP MESSAGE
{white}------------

{green}    -h or --help
{white}        Display this help description.

{yellow}COLOR CHANGING
{white}--------------

{green}    -c attribute COLOR or --config attribute COLOR
{white}        Change color of 'attribute' to 'COLOR'.
{white}        attribute: author, date, description, hash, refs
{white}        COLOR: RED, GREEN, YELLOW, BLUE, CYAN, PURPLE, BLACK, WHITE

{yellow}ADDITIONAL COMMANDS
{white}-------------------

{green}    -N or -n N
{white}        Display recent n commits.

{green}    --skip N
{white}        Skip recent N commits and display further.

{green}    --author "john\ doe"
{white}        Filter commits according to name of author.
{white}        Part of name / whole will be accepted.

{green}    --before DD-MMM-YYYY or --until DD/MMM/YYYY
{white}        Display commits before this date.
{white}        Hyphen(-) and forward slash(/) can be used interchangeably.

{green}    --after DD/MMM/YYYY or --since DD-MMM-YYYY
{white}        Display commits after this date.
{white}        Hyphen(-) and forward slash(/) can be used interchangeably.

{green}    --grep "foo\ bar"
{white}        Display commits with "foo bar" in their description.

{cyan}    * Any of these can be combined together and used.
{cyan}    * Regular expressions are also accepted in grep and author.
{cyan}    * Use escape character if using whitespace: yolog --grep="fixes\ bug"
{reset}""")


class YologGenerator(object):
    BLACK = "$(tput bold)$(tput setaf 0)"
    RED = "$(tput bold)$(tput setaf 1)"
    GREEN = "$(tput bold)$(tput setaf 2)"
    YELLOW = "$(tput bold)$(tput setaf 3)"
    BLUE = "$(tput bold)$(tput setaf 4)"
    PURPLE = "$(tput bold)$(tput setaf 5)"
    CYAN = "$(tput bold)$(tput setaf 6)"
    WHITE = "$(tput setaf 7)"

    def __init__(self, path):
        self.config = SafeConfigParser()
        self.path = os.path.expandvars(os.path.expanduser(path))
        self.config.read(self.path)

        self._hash = "{0}%h{1}".format(
            getattr(self, self.config.get("color", "hash")), RESET)

        self._author = "{0}%an{1}".format(
            getattr(self, self.config.get("color", "author")), RESET)

        self._date = "{0}%aD{1}{2}".format(
            getattr(self, self.config.get("color", "date")), BACKSPACE * 15, RESET)

        self._refs = "{0}%d{1}".format(
            getattr(self, self.config.get("color", "refs")), RESET)

        self._description = "{0}%s{1}".format(
            getattr(self, self.config.get("color", "description")), RESET)

        self._format = "{0};;{1};;{2};;{3} {4}".format(
            self._hash, self._author, self._date, self._refs, self._description
        )

    def git_command(self, git_arguments):
        return (
            "git log --pretty=\"tformat:{0}\" --graph --all {1} | "
            "column -t -s \";;\" | less -FXRS".format(
                self._format, git_arguments
            )
        )

    def print_help(self):
        return (
            "echo \"{0}\" | less -RS".format(help_description.format(
                author=__import__('yolog').__author__,
                version=__import__('yolog').__version__,
                yellow=self.YELLOW,
                green=self.GREEN,
                cyan=self.CYAN,
                white=self.WHITE,
                reset=RESET
            ))
        )
