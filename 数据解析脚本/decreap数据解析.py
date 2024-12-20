
import pandas as pd



import pandas as pd
import win32gui  # 用于窗口和控件操作
import win32api  # 用于 Win32 API 操作
import win32con  # 用于一些常量操作
import time      # 用于延



excel = pd.read_csv('D:/workspace/geodeparse/ok_geo.csv/ok_geo.csv')
# df = excel.parse(0, header=0)

from shapely import from_geojson,to_geojson
import json

j = 0 

res = {
"type": "FeatureCollection",
"name": "AreaCity-Polygon",
"crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },
"features": [

]
}

import re

jsons = []
res["features"] = jsons
uni = {}
citys = []
for i in excel.loc[excel['deep'] == int(1)].iterrows():
    j+=1
    tmp = i[1]
   

    pol = tmp["polygon"]
    if(pol == 'EMPTY'):
        continue
    type11 = pol.count(";")
    total = re.split("[,;]", pol)
    name = ""
    citys.append(tmp["ext_path"])
    
    
    
import win32gui  # 用于窗口和控件操作
import win32api  # 用于 Win32 API 操作
import win32con  # 用于一些常量操作
import time      # 用于延

hwnds = []
hwndbtn = None
def call(w,e) :
    global hwnds
    global hwndbtn
    clz = win32gui.GetClassName(w)
    txt = win32gui.GetWindowText(w)
    print(clz, txt)
    if(txt == "转成geojson文件"):
        hwndbtn = w
    if(clz ==  'WindowsForms10.EDIT.app.0.1e09f85_r7_ad1'):
        hwnds.append(w)


    pass
hwnd1 = win32gui.FindWindow("WindowsForms10.Window.8.app.0.1e09f85_r7_ad1", "AreaCity Geo格式转换工具 Ver:1.3.240505")
# hwnd1 = win32gui.FindWindowEx(hwnd1, 0, "WindowsForms10.Window.8.app.0.1e09f85_r7_ad1", None)


win32gui.EnumChildWindows(hwnd1, call, None)
# win32gui.EnumChildWindows(hwnd1, call, None)

time.sleep(3)
for (i,city) in enumerate(citys):
    win32gui.SendMessage(hwnds[5], win32con.WM_SETTEXT, 0, city)
    win32gui.SendMessage(hwndbtn, win32con.BM_CLICK,0, 0)
    print("当前 {} 总共 {}".format(i,len(citys)))
    time.sleep(5)
    