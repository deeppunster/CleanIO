"""
CleanIO.py - Read or write a text file without the clutter in mainstream code.
"""

__author__ = 'Travis Risner'
__project__ = 'CleanIOProject'
__creation_date__ = '05/22/2022'
__version__ = '0.1.0'

from logging import getLogger, debug, error
from pathlib import Path


class CleanRead:
    """
    CleanRead - Read a text file without the clutter in mainstream code.
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


class CleanWrite:
    """
    CleanWrite - Write a text file without the clutter in mainstream code.
    """

    def __init__(self, file_path: Path | str):
        """
        Prepare to write the text file specified.

        :param file_path: filename and optional path to write
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
        if self.file_exists:
            raise OSError(f'File {self.filename} already exists.')
        # initialize the generator
        self._write(None)
        return

    def clean_write(self, text_line: str):
        """
        Write a line to a text file.

        :return:
        """
        line_of_text = text_line
        self._write().send(line_of_text)
        return

    def clean_close(self):
        """
        Flush the file buffers and close the file.

        :return:
        """
        self._write().close()

    def _write(self):
        """
        Create and manage a generator to write text to a file.

        :return:
        """
        with open(self.pathname, 'W') as fw:
            textline = yield
            fw.writelines(textline)
        return


if __name__ == '__main__':
    pass

# EOF
