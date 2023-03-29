import os
import requests
import json
import pathlib
from bs4 import BeautifulSoup
import getopt
import sys
from datetime import date
import random

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
  file_out = f"out/temp/{model}"
  row_count = len(tile_data['row'])
  file_input = " ".join(tile_data['row'])
  cmd_args = f" -tile x{row_count}  -border 1 -geometry +0+0"
  cmd = f"magick montage {file_input} {cmd_args} {file_out}-L1.png"
  print(f"    - {cmd}")
  os.system(cmd)
    
def tile_level_2(model):
  file_out = f"out/temp/{model}"
  file_out_final = f"out/image/{model}"
  cmd_args = " -duplicate 8 -tile x1 -geometry +0+0 -gravity southwest -resize 2000x950^ -crop 1920x890+0+0 "
  cmd = f"magick montage {file_out}-L1.png {cmd_args} {file_out}-L2.png"
  print(f"    - {cmd}")
  os.system(cmd)

def tile_level_3(model, background):
  file_out = f"out/temp/{model}"
  file_out_final = f"out/image/{model}"
  cmd = f"magick -size 1920x1080 xc:darkgrey  {file_out}-L2.png -gravity northwest -geometry +0+0 -composite {background} -composite {file_out_final}.png"
  print(f"    - {cmd}")
  os.system(cmd)
   
###########################################
# magick montage  wall/FISH-A.jpg wall/FISH-A.jpg wall/FISH-HL.jpg  wall/FISH-C.jpg wall/FISH-C.jpg wall/FISH-C.jpg -tile x6  -border 1 -geometry +0+0  out.png
# magick montage  out.png  +clone +clone +clone -tile x1  -geometry +0+0  out2.png

os.makedirs("out/temp", exist_ok = True)
os.makedirs("out/image", exist_ok = True)

json_data = json.loads(loadFile("model2.json"))

bg_list = os.listdir("asset/bg/wall")
wall_list = os.listdir("asset/tile/wall")
print(wall_list)

for row in json_data:
  model = row["model"]
  bg = random.choice(bg_list)
  if "bg" in row:
    bg = row['bg']
    
  file_bg = f"asset/bg/wall/{bg}"
  print(f"  Processing: {model} with background {bg}")  
  tile_level_1(row)
  tile_level_2(model)
  tile_level_3(model, file_bg)
