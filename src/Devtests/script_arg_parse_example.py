#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

Script Description

"""
import argparse

def check_arguments():
    """ check args of script """
    
    parser = argparse.ArgumentParser(description='Convert csv to json')
    parser.add_argument('path', metavar='file', type=str, nargs='+',
                        help='the path of the input file .csv')
    parser.add_argument('delimiters', metavar='delim', type=str, nargs='+',
                        help="Delimiters of the .csv, default is ';'")
    
    args = parser.parse_args()
    print(args.accumulate(args.integers))
    
def main():  
    """ Main of the script """
    
if __name__ == '__main__':
    main()
