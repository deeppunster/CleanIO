"""
SampleUsage.py - Sample program using CleanIO.
"""
import os
from dotenv import dotenv_values


from src.cleanio.CleanIO import CleanRead, CleanWrite

lines_of_text = [
    'first line of text',
    'second line of text',
    'third line of text',
    'fourth line of text',
    '',
    'Above line was empty',
]


def sample_write(filename: str):
    """
    Write the lines of text to a file.

    :param filename:
    :return:
    """
    cw = CleanWrite(filename)
    for line in lines_of_text:
        cw.clean_writeline(line)
    cw.clean_close()
    return


def sample_read(filename: str):
    """
    Read and print the lines just written.

    :param filename:
    :return:
    """
    print(f'Lines read from {filename}:\n')
    cr = CleanRead(filename)
    for line in cr.clean_read():
        print(line)
    print('\nDone')
    return


if __name__ == '__main__':
    env: dict = dotenv_values()
    filename = env['myfile']
    os.unlink(filename)
    sample_write(filename)
    sample_read(filename)

# EOF
