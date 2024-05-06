# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 20:31:19 2017

@author: sylhare
"""

import sys
import os
from os.path import dirname, abspath

print(os.path.sep.join(dirname(abspath(__file__)).split(os.path.sep)[:-1]))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(os.path.dirname(os.getcwd()))
readme = os.path.join("docs", "README.md")
print(os.path.join(os.path.dirname(os.getcwd()), readme))

# ==============================================================================
# os.getcwd()
# file = open("newfile.txt", "w")
# file.write('\n'+"hello world in the new file")
# file.write('\n'+"and another line")
#
# file = open('newfile.txt', 'r')
# print (file.read())
# #file.read(number of character to read)
# #file.readline(line to print)
# #file.readlines() give back an array with the data
# file.close()
#
# ==============================================================================

# Going through the list of arguments
# python file_handling.py file_1 file_2 file_3
for index in enumerate(sys.argv):

    # Ignoring script name which is  argv[0]
    if index != 0:
        file = open(sys.argv[index], 'r')
        # Adding a ~ at the end so we don't erase the source file in case of a bug
        file2 = open(sys.argv[index] + '~', 'w')

        # Going through the lines of the source file
        lines = file.readlines()
        for line in lines:
            # Replacing the 4 spaces by a tabulation in the line
            final_line = line.replace('    ', '\t')
            # Writing the new line in the new file
            file2.write(final_line)

        # Close the source file
        file.close()
        # Close the new file
        file2.close()

### Same Example in short, replace 4 spaces by a tabulation
for file in sys.argv[1:]:
    with open(file + '~', 'w') as f:
        f.write(open(file).read().replace('    ', '\t'))
