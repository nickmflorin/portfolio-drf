import os
import csv
from dotenv import load_dotenv


class ConfigError(Exception):

    def __init__(self, config_name):
        self.config_name = config_name

    def __str__(self):
        return f"{self.config_name} is a required environment variable."


class Config:
    """
    Loads configuration settings from shell environment or .env file, the name
    for which can be overriden by exporting DOTENV_PATH in your shell.

    In production, configuration variables are saved as a JSON string in AWS
    Secrets manager and then loaded into individual environment variables in
    our `wsgi.py` file
    """

    def __init__(self, filename=None):
        self._values = {}
        self._defaults = {}

        # Load environment variables from a .env file if it exists
        dotenv_path = filename or os.getenv('DOTENV_PATH', None)
        load_dotenv(dotenv_path=dotenv_path)

    def __call__(self, var_name, default='', cast=str, required=False):
        var_name = var_name.upper()
        if var_name not in self._values:
            value = os.getenv(var_name, default)
            self._defaults[var_name] = value
            self._values[var_name] = cast(value)

        if required and not self._values[var_name]:
            raise ConfigError(var_name)

        return self._values[var_name]

    @staticmethod
    def csvlist(value):
        if r'\n' in value:
            value = value.replace(r'\n', '\n')
        data = list(csv.reader(value.splitlines()))
        return data if len(data) > 1 else data[0]

    @staticmethod
    def bool(value):
        return value.upper() in ['YES', 'TRUE', '1']

    def write(self, filename=None):
        """
        Write out a dump of all previously register config values to either
        stdout or to a file of given ``filename``
        """
        lines = []
        for key, value in sorted(self._defaults.items()):
            lines.append('{}={}'.format(
                key,
                '' if value in (None, '') else value
            ))

        text = '\n'.join(lines)
        if filename:
            with open(filename) as fobj:
                fobj.write(text)
        else:
            print(text)


config = Config()
