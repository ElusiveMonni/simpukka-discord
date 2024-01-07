import shlex


class DiscordUtils:
    def __init__(self):
        pass

    def parse_args(self, message):
        """Argument parser help function"""
        args = shlex.split(message, posix=True)

        command = args[0]
        arguments = args[1:]

        return [command] + arguments