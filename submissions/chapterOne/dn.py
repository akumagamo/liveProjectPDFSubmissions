import os

dir = os.path.join(os.getcwd(), 'formats')

def getfiles():
  """Return all files in passed folder and subfolders."""
  return [sdir + os.sep + f for sdir, _, files in os.walk(dir) for f in files]

print(getfiles())