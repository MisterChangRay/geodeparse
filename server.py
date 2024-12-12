
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
    res = deparse(float(longitude), float(latitude))
    if(res == None):
        return {
            "code":"9999",
            "msg":"经纬度查询异常",
        }
            
    return res

def deparse(l, g):
    p = Point(round(l,5),round(g,5))
    res = {
        "code":"9999",
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
    minDistance = [0.2, None]
    for tmp in geometrys:
        distance = tmp[0].centroid.distance(p)
        if(distance < minDistance[0] ):
            minDistance[0] = distance
            minDistance[1] = tmp[1]
    
        if(tmp[0].contains(p) == True):
            areacode = tmp[1]["gb"]
            if(areacode in area_region_data_mapping):
                fullinfo = area_region_data_mapping[areacode]
                res["code"] = "0000"
                res["msg"] = "ok"
                res["province"] = fullinfo[0]
                res["provinceCode"] = fullinfo[1]
                res["city"] = fullinfo[2]
                res["cityCode"] = fullinfo[3]
                res["area"] = fullinfo[4]
                res["areaCode"] = fullinfo[5]
            else:
                res["msg"] = "未找到地图数据，请联系开发"
    if(res["code"] != "0000" and minDistance[1] is not None) :
        areacode = minDistance[1]["gb"]
        if(areacode in area_region_data_mapping):
            fullinfo = area_region_data_mapping[areacode]
            res["code"] = "0000"
            res["msg"] = "ok,最近距离匹配结果"
            res["province"] = fullinfo[0]
            res["provinceCode"] = fullinfo[1]
            res["city"] = fullinfo[2]
            res["cityCode"] = fullinfo[3]
            res["area"] = fullinfo[4]
            res["areaCode"] = fullinfo[5]
        
    return res

if __name__ == "__main__":
    with open('geo/mapping.json', encoding='utf-8') as f:
        area_region_data_mapping = json.load(f)
            
    with open('geo/world.json', encoding='utf-8') as f:
        area_region_data = json.load(f)
        for tmp in area_region_data["features"]:
            t = from_geojson(json.dumps(tmp))
            if(t.is_valid):
                geocountrys.append((
                    t,
                    tmp["properties"]
                ))
            else:
                print(tmp["properties"])
    with open('geo/china_areas.geojson', encoding='utf-8') as f:
        region_data = json.load(f)
        for tmp in region_data["features"]:
            t = from_geojson(json.dumps(tmp))
            if(t.is_valid):
                geometrys.append((
                    t,
                    tmp["properties"]
                ))
            else:
                print(tmp["properties"])
    print(deparse(115.557628,22.786789))

    # The options break wsgi, I had to use `run()`
    app.run(host="0.0.0.0", port=11785)

