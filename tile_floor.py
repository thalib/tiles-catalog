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

def tile_level_1(model):
  # magick montage in.png -duplicate 63 -tile 8x8 -border 1 -geometry +0+0 out1.png
  file_input = f"asset/tile/floor/{model}.png"
  file_out = f"out/temp/{model}-L1.png"
  cmd_args = f" -duplicate 63 -tile 8x8 -border 1 -geometry +0+0 "
  cmd = f"magick montage {file_input} {cmd_args} {file_out}"
  runCmd(cmd)

def tile_level_2(model):
  #magick out1.png -virtual-pixel tile -mattecolor transparent -distort Perspective '0,0 500,0  1920,0 1420,0  0,1920 0,1920  1920,1920 1920,1920' out2.png
  file_input = f"out/temp/{model}-L1.png"
  file_out = f"out/temp/{model}-L2.png"
  cmd_args = ' -virtual-pixel tile -mattecolor transparent -distort Perspective "0,0 500,0  1920,0 1420,0  0,1920 0,1920  1920,1920 1920,1920" '
  cmd = f"magick {file_input} {cmd_args} {file_out}"
  runCmd(cmd)

def tile_level_3(model):
  #magick out2.png -geometry +0+0 -gravity northwest -resize 2000x950^ -crop 1920x580+0+0  final.png
  file_input = f"out/temp/{model}-L2.png"
  file_out = f"out/temp/{model}-L3.png"
  cmd_args = ' -geometry +0+0 -gravity northwest -resize 2000x950! -crop 1920x580+0+0 '
  cmd = f"magick {file_input} {cmd_args} {file_out}"
  runCmd(cmd)

def tile_level_4(model, bg):
  #magick -size 1920x1080 xc:darkgrey  final.png -gravity northwest -geometry +0+500 -composite ../asset/bg/parking/outdoor-2.png -composite wow.png
  file_input = f"out/temp/{model}-L3.png"
  file_out = f"out/temp/{model}-L4.png"
  cmd_args = f" -size 1920x1080 xc:darkgrey  {file_input} -gravity northwest -geometry +0+500 -composite {bg} -composite "
  cmd = f"magick {cmd_args} {file_out}"
  runCmd(cmd)

###########################################
# magick montage  wall/FISH-A.jpg wall/FISH-A.jpg wall/FISH-HL.jpg  wall/FISH-C.jpg wall/FISH-C.jpg wall/FISH-C.jpg -tile x6  -border 1 -geometry +0+0  out.png
# magick montage  out.png  +clone +clone +clone -tile x1  -geometry +0+0  out2.png

os.makedirs("out/temp", exist_ok = True)
os.makedirs("out/image/floor/", exist_ok = True)

json_data = json.loads(loadFile("model2.json"))

bg_list = os.listdir("asset/bg/parking")
tile_list = os.listdir("asset/tile/floor")

for row in tile_list:
  
  bg = random.choice(bg_list)
  #if "bg" in row:
  #  bg = row['bg']
    
  file_bg = f"asset/bg/parking/{bg}"
  model = os.path.splitext(row)[0]
  print(f"  Processing: {model} with background {bg}")  
  tile_level_1(model)
  tile_level_2(model)
  tile_level_3(model)
  tile_level_4(model, file_bg)
  break
  
