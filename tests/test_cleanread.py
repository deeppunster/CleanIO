"""
test_cleanread.py - test the CleanRead class.
"""
from os import write
from pathlib import Path

import pytest

from src.cleanio.CleanIO import __version__, CleanRead


def test_version():
    """
    Test the current version of the module.

    (Remove this test before publishing this module.)

    :return:
    """
    assert __version__ == '0.1.0'


def test_nonexistance():
    """
    Test CleanRead to catch the nonexistance of a file to be read.

    :return:
    """
    filename = 'test_cleanread_nonexistance.txt'
    pathname = Path(filename)
    if pathname.exists():
        pathname.unlink()
    with pytest.raises(IOError, match=f'File {filename} not found') as exc:
        cr = CleanRead(filename)
    return


def test_fileread():
    """
    Test that CleanRead can read a text file.

    :return:
    """
    lines_of_text = (
        'One line of text',
        'Second line of text',
        'Third line ' 'of text',
    )
    filename = 'test_cleanread_reading.txt'
    pathname = Path(filename)
    pathname.unlink(missing_ok=True)
    with open(pathname, 'w') as fr:
        for line in lines_of_text:
            fr.write(line + '\n')
        fr.close()
    cr = CleanRead(filename)
    nbr = 0
    print()
    for line in cr.clean_read():
        assert lines_of_text[nbr] == line
        print(f'Nbr: {nbr}, line: ==>{line}<==')
        nbr += 1
    return


# EO
