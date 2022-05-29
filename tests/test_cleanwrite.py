"""
test_cleanread.py - test the CleanRead class.
"""
from pathlib import Path

import pytest

from src.cleanio.CleanIO import __version__, CleanRead


def test_version():
    assert __version__ == '0.1.0'

def test_nonexistance():
    filename = 'test_cleanread_nonexistance.txt'
    pathname = Path(filename)
    if pathname.exists():
        pathname.unlink()
    with pytest.raises(IOError, match=f'File {filename} not found') as exc:
        cr = CleanRead(filename)

def test_fileread():
    pass

# EOF
