import os
try:
    from ConfigParser import SafeConfigParser
except ImportError:
    from configparser import SafeConfigParser



RESET  = "$(tput sgr0)"
BACKSPACE = "%x08"


class YologGenerator(object):
    BLACK  = "$(tput bold)$(tput setaf 0)"
    RED    = "$(tput bold)$(tput setaf 1)"
    GREEN  = "$(tput bold)$(tput setaf 2)"
    YELLOW = "$(tput bold)$(tput setaf 3)"
    BLUE   = "$(tput bold)$(tput setaf 4)"
    PURPLE = "$(tput bold)$(tput setaf 5)"
    CYAN   = "$(tput bold)$(tput setaf 6)"
    WHITE  = "$(tput setaf 7)"

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
