import os
import sys
import string
import shutil
from pathlib import Path
import tarfile

lis = []
files = []

def getfiles(path):
    if os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for name in files:
                yield os.path.join(root, name)
    else:
        yield path

if (len(sys.argv) < 3):
    print("Too few arguments")
    exit()

else:
  tar = tarfile.open(sys.argv[1], "w:gz")
  count = 0
  for get in sys.argv[2:]:
    if Path(get).exists():
        if os.path.isdir(get):
          fromdir = get
          for f in getfiles(fromdir):
            if not(os.path.abspath(f).replace("/","-") in files):
             files.append(os.path.abspath(f).replace("/","-"))
             tar.add(f,arcname=os.path.abspath(f).replace("/","-"))

        else:
          if not(os.path.abspath(get).replace("/","-") in files):
             files.append(os.path.abspath(get).replace("/","-"))
             tar.add(get,arcname=os.path.abspath(get).replace("/","-"))
    else:
      count = count+1
      lis.append(get)

  if count == len(sys.argv)-2 :
      print("All files are missing")
      os.remove(sys.argv[1])
      exit()
  else:
      print("Successfully compressed")
      for i in lis:
          print(i)
  tar.close()
