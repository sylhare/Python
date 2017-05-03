# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 18:50:13 2017

@author: sylhare
@source: http://stackoverflow.com/questions/5411603/how-to-remove-trailing-whitespace-in-code-using-another-script

"""

import os
import sys


def main():
    """
    if an argument is given, will remove space of the file,
    else it will remove space of all 'py' files in the directory

    """
    if len(sys.argv) == 1:
        print("All '.py' file from directory will be trimmed")
        main_reboot()
    else:
        path = sys.argv[1]
        if os.path.exists(path):
            rm_trailing_space(path)
        else:
            print("file not found: %s" % sys.argv[1])
            sys.exit(1)

def main_reboot():
    """
    Remove trailing spaces for all files in the current directory

    """
    path = os.getcwd()
    # os.walk(path) return path, dirs, fils
    for files in os.walk(path):
        print(files[2])
        for file in files[2]:
            if file[-3:] == '.py':
                rm_trailing_space(file)

def user_input():
    """
    Ask validation before doing anything

    """
    yes = set(['yes','y', 'yup', ''])
    no = set(['no','n'])

    while True:
        print("continue? [y\n]")
        choice = input().lower()
        if choice in yes:
            return True
        elif choice in no:
            return False
        else:
            sys.stdout.write("Please respond with 'yes' or 'no'")


def rm_trailing_space(path):
    """
    Remove all trailing space from the file of the path

    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            new = [line.rstrip() for line in file]
        with open(path, 'w', encoding='utf-8') as file:
            [file.write('%s\n' % line) for line in new]
        print("[ OK ] {0}".format(path))
    except Exception as e:
        print("[FAIL] {0} {1}".format(path, str(type(e).__name__ )))


if __name__ == "__main__":
    main_reboot()
