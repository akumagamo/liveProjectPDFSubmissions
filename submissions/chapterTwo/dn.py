import os
import configparser
import pdfplumber

from PyPDF2 import PdfFileReader
from collections import OrderedDict

FORMAT_ONE_IDENTITIER = 'ALBARAN Nº'
FORMAT_TWO_IDENTITIER = 'TALLER'

config = configparser.ConfigParser(delimiters= ('=','|'), dict_type= OrderedDict)
    
def getfiles(folder):
  '''Return all files in passed folder and subfolders.'''

  return [sdir + os.sep + f for sdir, _, files in os.walk(folder) for f in files if f.endswith('.pdf')]

def readini(filename):
  '''Reads the ini-files values and returns a Ordered dictionary.'''

  with open(filename) as file:
    lines = ("[DEFAULT]\n" + file.read())
    return config.read_string(lines)

def getformfields(pdf, tree=None, retval=None, fileobj=None):
    ''' Returns PDF fields found with PyPDF2 getFields. '''

    return pdf.getFields(tree= tree, retval= retval, fileobj= fileobj)

def getfields(filename):
  '''gets Fields from PDF and removes unneeded values.'''

  with open(filename, 'rb') as file:
    pdf = PdfFileReader(file)
    return getformfields(pdf)

def filter(entries, testfunction):
  '''Finds the index of a entry in a list, where the return function returns True.'''

  return next(idx for idx, entry in enumerate(entries) if testfunction(entry))   

def gettextfields(iniFile1, iniFile2, filename):
    '''Read the Needed Text-fields out of PDF depending on format'''
    
    with pdfplumber.open(filename) as pdf:
      firstPage = pdf.pages[0]

      # TODO: refactor to only extract once the text
      firstPageContent = firstPage.extract_text()

      if firstPageContent.find(FORMAT_ONE_IDENTITIER) != -1:
        firstPageTableContent = firstPage.extract_tables()[0]
        columnIdx = filter(firstPageTableContent[0], lambda item: (item if item else '').find('ALBARAN Nº') != -1 ) 
        print(columnIdx)
        print("FORMAT 1")
      elif firstPageContent.find(FORMAT_TWO_IDENTITIER) != -1:

        print("FORMAT 2")
      else:
        raise TypeError("PDF DN Format not recognised.")

    print(firstPageContent)

def execute():
  '''starts the pdf parsing and field grabbing.'''

  try: 
      filesFolder = os.path.join(os.getcwd(), 'formats')
      baseFolder = os.path.dirname(os.path.realpath(__file__))

      ini1FileName = os.path.join(baseFolder, 'format1.ini')
      ini2FileName = os.path.join(baseFolder, 'format2.ini')
      
      iniFile1 = readini(ini1FileName)
      iniFile2 = readini(ini2FileName)
      
      files = getfiles(filesFolder)
      for file in files:
        print(getfields(file))
        print(gettextfields(iniFile1, iniFile2, file))

  except BaseException as msg:
      print('Error occured: ' + str(msg))

if __name__ == '__main__':
    execute()