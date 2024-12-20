
import pandas as pd



import pandas as pd
import win32gui  # 用于窗口和控件操作
import win32api  # 用于 Win32 API 操作
import win32con  # 用于一些常量操作
import time      # 用于延

import os
import json
folder_path = 'C:\\Users\\Miste\\Downloads\\Compressed\\ok_geo.csv'

files1 = []
for root, dirs, files in os.walk(folder_path):
    for file_name in files:
        abs_file_path = os.path.join(root, file_name)
        if(abs_file_path.endswith("json")):
            print(abs_file_path)
            files1.append(abs_file_path)
    
    
datas = []    
for (i, f) in enumerate(files1):
    f2 = open(f, "r",encoding="utf-8")
    line = f2.read()
    datas.append(json.loads(line))

print(11)

res = {
"type": "FeatureCollection",
"name": "AreaCity-Polygon",
"crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },
"features": [

]
}

tmp2 = []
for (i, f) in enumerate(datas):
    for(j,k) in enumerate(datas[i]["features"]):
        tmp2.append(k)

res["features"] = tmp2
f1 = open("tmp.json", "w",encoding="utf-8")
f1.write( json.dumps(res,ensure_ascii=False))
f1.close()