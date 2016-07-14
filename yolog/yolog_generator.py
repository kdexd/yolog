import os
try:
    from ConfigParser import SafeConfigParser
except ImportError:
    from configparser import SafeConfigParser


RESET = "$(tput sgr0)"
BACKSPACE = "%x08"

help_description = ("""
{yellow}Yolog - Beautify your Git logs !
{white}--------------------------------
{cyan}Usage: yolog [<additional optional commands>]

{green}1. yolog -n
{white}-      Display recent n commits.

{green}2. yolog --skip=n
{white}-      Skip recent n commits and display further.

{green}3. yolog --author=john
{white}-      Filter commits according to author.
{white}       Part of name / whole will be accepted.

{green}4. yolog --before=dd-mmm-yyyy
{green}   yolog --until=dd/mmm/yyyy
{white}-      Display commits before this date.

{green}5. yolog --after=dd/mmm/yyyy
{green}   yolog --since=dd-mmm-yyyy
{white}-      Display commits after this date.

{green}6. yolog --grep="foo\ bar"
{white}-      Display commits with "foo bar" in their description.

{green}7. yolog --help
{green}   yolog -h
{white}-      Display this instruction.

{cyan}* Any of these can be combined together and used.
{cyan}* Regular expressions are also accepted in grep and author.
{cyan}* Use escape character if using whitespace: yolog --grep="fixes\ bug"
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
                yellow=self.YELLOW, green=self.GREEN, cyan=self.CYAN,
                white=self.WHITE, reset=RESET
            ))
        )
