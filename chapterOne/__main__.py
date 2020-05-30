import os
import chapterOne.fileloader as fileloader

baseFolder = os.path.join(os.getcwd(), 'formats')

if __name__ == '__main__':
  print(fileloader.tooShortLoaderFromFolder(baseFolder))