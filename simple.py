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
    ['1002D.png', '1002HL.png', '1002L.png'],
    ['1004D.png', '1004HL.png', '1004L.png'],
    ['1009D.png', '1009HL.png', '1009L.png'],
    ['1010D.png', '1010HL.png', '1010L.png'],
    ['1011D.png', '1011HL.png', '1011L.png'],
    ['1021D.png', '1021HL.png', '1021L.png'],
    ['1026D.png', '1026HL.png', '1026L.png'],
    ['1028D.png', '1028HL.png', '1028L.png'],
    ['1029D.png', '1029HL.png', '1029L.png'],
    ['1030D.png', '1030HL.png', '1030L.png'],
    ['1031D.png', '1031HL.png', '1031L.png'],
    ['1034D.png', '1034HL.png', '1034L.png'],
    ['1035D.png', '1035HL.png', '1035L.png'],
    ['1036D.png', '1036HL.png', '1036L.png'],
    ['1038D.png', '1038HL.png', '1038L.png'],
    ['1115D.png', '1115HL.png', '1115L.png'],
    ['1120D.png', '1120HL.png', '1120L.png'],
    ['1122D.png', '1122HL.png', '1122L.png'],
    ['1123D.png', '1123HL.png', '1123L.png'],
    ['1981D.png', '1981HL.png', '1981L.png'],
    ['1982D.png', '1982HL.png', '1982L.png'],
    ['1984D.png', '1984HL.png', '1984L.png'],
    ['2211D.png', '2211HL.png', '2211L.png'],
    ['2292D.png', '2292HL.png', '2292L.png'],
    ['2301D.png', '2301HL.png', '2301L.png'],
    ['2337D.png', '2337HL.png', '2337L.png'],
    ['2346D.png', '2346HL.png', '2346L.png'],
    ['C002D.png', 'C002HL.png', 'C002L.png']
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

saveFile("model2.json", json.dumps(tiles_json, indent=2))