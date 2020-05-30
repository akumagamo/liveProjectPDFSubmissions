import os
import sys
import pdfplumber

from collections import OrderedDict
from PyPDF2 import PdfFileReader

def getfiles():
    # Instruction(s) to get the list of PDF files goes here (and/or below)...

def readini(fname):
    # Instruction(s) to read an .ini file go here (and/or below)...

def getformfields(obj, tree=None, retval=None, fileobj=None):
    # Check resource: How to extract PDF fields from a filled-out form in Python

def getfields(fn):
    # Instruction(s) to read form fields go here (and/or below)... 
    # This function should call getformfields

def gettextfields(i1, i2, fn):
    # Instruction(s) to get the text fields goes here...

def execute():
    try: 
        i1 = readini('l1.ini') # Read the 1st .ini file
        i2 = readini('l2.ini') # Read the 2nd .ini file
        # Read fields for each file (instructions are missing here)
        # Both getfields and gettextfields should be invoked
    except BaseException as msg:
        print('Error occured: ' + str(msg))

if __name__ == '__main__':
    execute()