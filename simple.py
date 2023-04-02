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

tiles_list = [
    ['1001D.png', '1001HL.png', '1001L.png'],
    ['1007D.png', '1007HL.png', '1004L.png'],
    ['1027D.png', '1027HL1.png', '1027HL2.png'],
    ['1039L.png', '1039HL1.png', '1039HL2.png'],
    ['1040D.png', '1040HL.png', '1040L.png'],
    ['1052D.png', '1052HL.png', '1052L.png'],
    ['1100D.png', '1100HL.png', '1100L.png'],
    ['1983D.png', '1983HL1.png', '1983HL1.png']
]

tiles_json = []
for row in tiles_list:
    print(row)
    model = row[0][:4]
    new_tile = {
      "model": f"DNW-{model}",
      "row": [
        f"asset/tile/wall/{row[2]}",
        f"asset/tile/wall/{row[2]}",
        f"asset/tile/wall/{row[1]}",
        f"asset/tile/wall/{row[1]}",
        f"asset/tile/wall/{row[0]}",
        f"asset/tile/wall/{row[0]}"
      ]
    }
    tiles_json.append(new_tile)

print(tiles_json)

saveFile("model3.json", json.dumps(tiles_json, indent=2))