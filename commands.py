from ranger.api.commands import *

class terminal(Command):
    """:terminal

    Spawns an "x-terminal-emulator" starting in the current directory.
    """
    def execute(self):
        command = '/usr/bin/urxvtc'
        self.fm.run(command, flags='f')
