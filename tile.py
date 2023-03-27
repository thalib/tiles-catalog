import os
import requests
import json
import pathlib
from bs4 import BeautifulSoup
import getopt
import sys
from datetime import date

###########################################
def saveFile(file_name, data):
    parentDir = pathlib.PurePath(file_name).parent
    if not os.path.exists(parentDir):
        print(f"mkdir: {parentDir}")
        os.makedirs(parentDir, exist_ok = True)
    print("   - Saving: " + file_name)  
    f=open(file_name,"w+", encoding="utf8")
    f.write(data)
    f.close()
    
def loadFile(file_name):
    print("  Loading: " + file_name)  
    f=open(file_name,"r", encoding="utf8")
    data = f.read()
    f.close()
    return data
###########################################
def tile_level_1(tile_data):
  file_input = ""
  row_count = len(tile_data['row'])
  file_input = " ".join(tile_data['row'])
  cmd_args = f" -tile x{row_count}  -border 1 -geometry +0+0"
  cmd = f"magick montage {file_input} {cmd_args} {TEMP_FILE}"
  print(cmd)
  os.system(cmd)
    
def tile_level_2(model):
  cmd_args = " +clone +clone +clone +clone +clone -tile x1  -geometry +0+0 "
  cmd = f"magick montage {TEMP_FILE} {cmd_args} out/{model}.png"
  print(cmd)
  os.system(cmd)
###########################################

# magick montage  wall/FISH-A.jpg wall/FISH-A.jpg wall/FISH-HL.jpg  wall/FISH-C.jpg wall/FISH-C.jpg wall/FISH-C.jpg -tile x6  -border 1 -geometry +0+0  out.png
# magick montage  out.png  +clone +clone +clone -tile x1  -geometry +0+0  out2.png

os.makedirs("out/image", exist_ok = True)

json_data = json.loads(loadFile("model.json"))

TEMP_FILE = "out/temp.png"
for row in json_data:
  model= row['model']
  tile_level_1(row)
  tile_level_2(model)
