import os
import configparser
import pdfplumber

from PyPDF2 import PdfFileReader
from collections import OrderedDict

FORMAT_ONE_IDENTITIER = 'ALBARAN Nº'
FORMAT_TWO_IDENTITIER = 'TALLER'

def getfiles(folder):
  '''Return all files in passed folder and subfolders.'''

  return [sdir + os.sep + f for sdir, _, files in os.walk(folder) for f in files if f.endswith('.pdf')]

def readini(filename):
  '''Reads the ini-files values and returns a Ordered dictionary.'''

  config = configparser.ConfigParser(delimiters= ('=','|'), dict_type= OrderedDict , default_section="[DEFAULT]")
  with open(filename) as file:
    lines = ("[DEFAULT]\n" + file.read())
    config.read_string(lines)
    return config

def getformfields(pdf, tree=None, retval=None, fileobj=None):
    ''' Returns PDF fields found with PyPDF2 getFields. '''

    return pdf.getFields(tree= tree, retval= retval, fileobj= fileobj)

def getfields(filename):
  '''gets Fields from PDF and removes unneeded values.'''

  with open(filename, 'rb') as file:
    pdf = PdfFileReader(file)
    return getformfields(pdf)

def filterFunction(value):
  return lambda entry: (entry if entry else '').lower().find(value.lower()) != -1 

def filter(entries, testfunction):
  '''Finds the index of a entry in a list, where the return function returns True.'''

  return next(idx for idx, entry in enumerate(entries) if testfunction(entry))   

def gettextfields(iniFile1, iniFile2, filename):
    '''Read the Needed Text-fields out of PDF depending on format'''

    textFields = {}
    with pdfplumber.open(filename) as pdf:
      firstPage = pdf.pages[0]

      firstPageContent = firstPage.extract_text()
      # TODO: refactor to only extract once the text
      firstPageTableContent = firstPage.extract_tables()

      if firstPageContent.find(FORMAT_ONE_IDENTITIER) != -1:
        firstPageTableContent = firstPageTableContent[0]

        for key, value in iniFile1["DEFAULT"].items():
          if len(value) > 1:
            index = filter(firstPageTableContent[0], filterFunction(value))
            if index > -1 :
              textFields[key] = firstPageTableContent[1][index]

      elif firstPageContent.find(FORMAT_TWO_IDENTITIER) != -1:
        firstPageTableContent = firstPageTableContent[1]

        # TODO: refactor duplication
        for key, value in iniFile2["DEFAULT"].items():
          if len(value) > 1:
            index = filter(firstPageTableContent[0], filterFunction(value))
            if index > -1 : 
              textFields[key] = firstPageTableContent[0][index].split('\n')[1]

      else:
        raise TypeError("PDF DN Format not recognised.")

    return textFields

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
        print('\nFile: ', file)
        print('\nFields:')
        print(getfields(file))
        print('\nTextfields:')
        print(gettextfields(iniFile1, iniFile2, file))

  except BaseException as msg:
      print('Error occured: ' + str(msg))

if __name__ == '__main__':
    execute()