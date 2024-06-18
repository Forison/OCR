# Makes sure we have an exclusive dir for our image detection
# It does not restrict anyone from using exp as your will recreate it for anyone using via terminal but would available to us exclusively for our ocr

import shutil
import os

def clear_dir(dir):
  try:
    if os.path.isdir(dir):
      shutil.rmtree(dir)
      return 'directory clearance was successful'
  except:
    return 'directory clearance error'