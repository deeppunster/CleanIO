"""
CleanRead.py - Read a text file without the clutter in mainstream code.
"""

from logging import getLogger, debug, error

__author__ = 'Travis Risner'
__project__ = 'CleanIOProject'
__creation_date__ = '05/22/2022'
__version__ = '0.1.0'


# "${Copyright.py}"
from pathlib import Path


class CleanReadClass:
    """
    CleanReadClass - Read a text file without the clutter in mainstream code.
    """

    def __init__(self, file_path: Path | str):
        """
        Prepare to read the text file specified.

        :param file_path: filename and optional path to read
        """
        self.filename = file_path
        if isinstance(self.filename, Path):
            self.pathname = self.filename
        else:
            self.pathname = Path(self.filename)
        try:
            self.file_exists = self.pathname.exists()
        except TypeError as e:
            raise TypeError('file_path must be a string or a pathlike object')
        if not self.file_exists:
            raise OSError(f'File {self.filename} not found.')
        return

    def clean_read(self):
        """
        Read a line from a text file.

        :return: The line just read
        """
        with open(self.pathname, 'r') as fr:
            textline = fr.readline()
            yield textline
        return


if __name__ == '__main__':
    filename = 'Selftest.txt'
    cr = CleanReadClass(filename)

# EOF
