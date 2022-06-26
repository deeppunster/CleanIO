"""
test_cleanread.py - test the CleanWrite class.
"""
from pathlib import Path

import pytest

from src.cleanio.CleanIO import __version__, CleanWrite


def test_version():
    """
    Test the current version of the module.

    (Remove this test before publishing this module.)

    :return:
    """
    assert __version__ == '0.1.0'


def test_existance():
    """
    Test CleanWrite to catch the pre-existance of a file to be written.

    :return:
    """
    filename = 'test_cleanwrite_existance.txt'
    pathname = Path(filename)
    pathname.touch(exist_ok=True)
    with pytest.raises(
        IOError, match=f'File {filename} already exists.'
    ) as exc:
        cw = CleanWrite(filename)
    return


def test_filewrite():
    """
    Test that CleanWrite can write a text file.

    :return:
    """
    lines_of_text = [
        'One line of text\n',
        'Second line of text\n',
        'Third line ' 'of text\n',
    ]
    filename = 'test_cleanwrite_writing.txt'
    pathname = Path(filename)
    if pathname.exists():
        pathname.unlink()
    cw = CleanWrite(filename)
    for line in lines_of_text:
        cw.clean_writeline(line)
    cw.clean_close()
    with open(pathname, 'rt') as fw:
        # for nbr, line in enumerate(fw.readline()):
        #     assert lines_of_text[nbr] == line
        print('\n\n')
        for line in fw.readline():
            print(line)

    return


# EOF
