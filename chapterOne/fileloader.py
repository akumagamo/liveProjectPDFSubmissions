import os

def loadFilesFromFolder(baseFolder):
  """Return all files in passed folder and subfolders."""
  foundFiles = []
  for subdir, dirs, files in os.walk(baseFolder):
    for filename in files:
      foundFiles.append(os.path.join(subdir , filename))
  return foundFiles

def tooShortLoaderFromFolder(dir):
  """Return all files in passed folder and subfolders.
  (Short and not so readable version of 'loadFilesFromFolder')
  """
  return [sdir + os.sep + f for sdir, _, files in os.walk(dir) for f in files]

