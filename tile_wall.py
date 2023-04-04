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

def runCmd(cmd: str):
  print(f" ✅  {cmd}")
  ret = os.system(cmd)
  if not ret == 0:
     print("#Error: " + str(ret))
     exit(255)
###########################################
def tile_level_1(tile_data):
  file_input = ""
  file_out = f"out/temp/{model}"
  row_count = len(tile_data['row'])
  file_input = " ".join(tile_data['row'])
  cmd_args = f" -tile x{row_count}  -border 1 -geometry +0+0"
  cmd = f"magick montage {file_input} {cmd_args} {file_out}-L1.png"
  runCmd(cmd)
    
def tile_level_2(model):
  file_out = f"out/temp/{model}"
  file_out_final = f"out/image/{model}"
  cmd_args = " -duplicate 8 -tile x1 -geometry +0+0 -gravity southwest -resize 2000x950^ -crop 1920x890+0+0 "
  cmd = f"magick montage {file_out}-L1.png {cmd_args} {file_out}-L2.png"
  cmd = f"magick montage {file_out}-L1.png {cmd_args} {file_out}-L2.png"
  runCmd(cmd)

def tile_level_3(model, tile_data):
  file_out = f"out/temp/{model}"
  offset_x = 50
  offset_y = 80
  file_input = list(set(tile_data['row']))
  cmd_args = ""
  cmd_args += f" -gravity northwest -fill black -pointsize 35 -annotate +{offset_x}+15 Model:{model} "
  cmd_args += f" -gravity north -fill black -pointsize 35 -annotate +{offset_x}+15 www.deltaware.in "
  cmd_args += f" -gravity northeast -fill black -pointsize 35 -annotate +{offset_x}+15 Whatsapp:9940198130 "
  for item in file_input:
    cmd_args += f" {item} -border 5 -geometry 300x180+{offset_x}+{offset_y} -gravity northwest -composite "
    offset_x += 300
    offset_y += 5
  
  cmd = f"magick  -size 1920x280 xc:white {cmd_args} {file_out}-L3.png"
  runCmd(cmd)
  
def tile_level_4(model, background):
  file_out = f"out/image/wall/{model}"  
  file_in = f"out/temp/{model}"
  cmd_args = f" -size 1920x1360 xc:darkgrey {file_in}-L2.png -gravity northwest -geometry +0+0 -composite {background} -composite "
  cmd_args += " asset/logo.png -gravity northwest -geometry +50+20 -composite "
  cmd_args += f" {file_in}-L3.png -gravity southeast -geometry +0+0 -composite "
  cmd = f"magick {cmd_args} {file_out}.png"
  runCmd(cmd)
  
###########################################
# magick montage  wall/FISH-A.jpg wall/FISH-A.jpg wall/FISH-HL.jpg  wall/FISH-C.jpg wall/FISH-C.jpg wall/FISH-C.jpg -tile x6  -border 1 -geometry +0+0  out.png
# magick montage  out.png  +clone +clone +clone -tile x1  -geometry +0+0  out2.png

PATH_OUT = "out/image/wall"
PATH_BG = "asset/bg/outdoor"

os.makedirs("out/temp", exist_ok = True)
os.makedirs(PATH_OUT, exist_ok = True)

json_data = json.loads(loadFile("model_wall_tiles.json"))

bg_list = os.listdir("asset/bg/wall")

for row in json_data:
  model = row["model"]
  file_out = f"{PATH_OUT}/{model}.png"
  
  if not os.path.exists(file_out):
    bg = random.choice(bg_list)
    if "bg" in row:
      bg = row['bg']
      
    file_bg = f"asset/bg/wall/{bg}"
    print(f"  Processing: {model} with background {bg}")  
    tile_level_1(row)
    tile_level_2(model)
    tile_level_3(model, row)
    tile_level_4(model, file_bg)
