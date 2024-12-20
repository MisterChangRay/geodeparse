
from flask import Flask
import json
import re
from flask import request
from shapely.geometry import Polygon, Point
from shapely import from_geojson,to_geojson
app = Flask(__name__)
geometrys = []
geocountrys = []
area_region_data_mapping = {}

@app.route('/geo/gps/decode', methods=['POST'])
def hello_world():
    jsonbody = request.get_json()
    
    longitude = ( jsonbody.get("longitude"))
    latitude = (jsonbody.get("latitude"))
    if(longitude == None or longitude == ''):
        return {
            "code":"9999",
            "msg":'参数异常 示例:{"longitude":"118.1371","latitude":"24.5261"}',
        }
    if(latitude == None or latitude == ''):
        return {
            "code":"9999",
            "msg":'参数异常 示例:{"longitude":"118.1371","latitude":"24.5261"}',

        }
    res = deparse(longitude, latitude)
    if(res == None):
        return {
            "code":"9999",
            "msg":"经纬度查询异常",
        }
            
    return res

def deparse(l, g):
    p = Point(round(float(l), 5),round(float(g), 5))
    res = {
        "code":"9999",
        "req": "{},{}".format(l, g),
        "msg":"未查询到坐标定位信息",
        "province": "",
        "provinceCode": "",
        "city": "",
        "cityCode": "",
        "area": "",
        "areaCode": ""
        # ,"country": "未知"
    }
    for tmp in geocountrys:
        if(tmp[0].contains(p) == True):
            res["country"] = tmp[1]["full_name"]
    minDistance = [0.5, None]
    for tmp in geometrys:
        distance = tmp[0].centroid.distance(p)
        if(distance < minDistance[0] ):
            minDistance[0] = distance
            minDistance[1] = tmp[1]
    
        if(tmp[0].contains(p) == True):
            areacode = tmp[1]["id"]
            if(areacode in area_region_data_mapping):
                fullinfo = area_region_data_mapping[areacode]
                ext = fullinfo["ext_path"].split(" ")
                code = str(fullinfo["id"])
                res["code"] = "0000"
                res["msg"] = "ok"
                res["province"] = ext[0]
                res["provinceCode"] = code[0:2]
                res["city"] = ext[1]
                res["cityCode"] =  code[0:4]
                res["area"] = ext[2]
                res["areaCode"] = code
            else:
                res["msg"] = "未找到地图数据，请联系开发"

        
    return res

if __name__ == "__main__":
    with open('geo/mapping.json', encoding='utf-8') as f:
        area_region_data_mapping = json.load(f)

    with open('geo/areas.json', encoding='utf-8') as f:
        region_data = json.load(f)
        for tmp in region_data["features"]:
            t = from_geojson(json.dumps(tmp, ensure_ascii=False))
            if(t.is_valid):
                geometrys.append((
                    t,
                    tmp["properties"]
                ))
            else:
                print(tmp["properties"])
    print(deparse(117.181654,	39.129657))
    # print(deparse(117.208256,	39.131854))
	
    # The options break wsgi, I had to use `run()`
    app.run(host="0.0.0.0", port=11785)

