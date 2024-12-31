import pandas as pd
import json

sheet2 = pd.read_excel('xzqh2020-03.xlsx',sheet_name= 0, header=0)
areas = None
citys = None
with open ("D:\\workspace\\geodeparse\\geo\\china_areas.geojson", encoding="utf8") as f:
    tmp = f.read()
    areas = json.loads(tmp)

with open ("D:\\workspace\\geodeparse\\geo\\china_city.geojson", encoding="utf8") as f:
    tmp = f.read()
    citys = json.loads(tmp)

mapp = {}
sqls22 = ""


# 所有直辖市
zx = {
    '156419001':'济源市',
    '156429021':'神农架林区',
'156429006':'天门市',
'156429005':'潜江市',
'156429004':'仙桃市',
'156469029':'保亭黎族苗族自治县',
'156469028':'陵水黎族自治县',
'156469027':'乐东黎族自治县',
'156469026':'昌江黎族自治县',
'156469025':'白沙黎族自治县',
'156469024':'临高县',
'156469023':'澄迈县',
'156469022':'屯昌县',
'156469021':'定安县',
'156469030':'琼中黎族苗族自治县',
'156469007':'东方市',
'156469006':'万宁市',
'156469005':'文昌市',
'156469002':'琼海市',
'156469001':'五指山市',
'156659010':'胡杨河市',
'156659012':'白杨市',
'156659011':'新星市',
'156659009':'昆玉市',
'156659008':'可克达拉市',
'156659003':'图木舒克市',
'156659002':'阿拉尔市',
'156659001':'石河子市',
'156659007':'双河市',
'156659006':'铁门关市',
'156659005':'北屯市',
'156659004':'五家渠市'
}

# 直辖市
zxs = {
    "156110000":"北京",
    "156120000":"天津",
    "156310000":"上海",
    "156500000":"重庆",
    "156810000":"香港"
    
}
import re
#查找区
def findarea(parent, root):
    parent["child"] = []
    
    # j1 = 0
    # for tmp in areas["features"]:
    #     if(tmp["properties"]["gb"].startswith ( parent["code"][0:6])):
    #         j1 += 1

    global sqls22
    fa = False
    for tmp in areas["features"]:
        # print("=============")
        # print(tmp[1])
        tmp2 = {
                        "name":tmp["properties"]["name"],
                        "code":tmp["properties"]["gb"],
                        "parentCode":str(parent["code"]),
                        "level":3
                    }

        # print("=============")
        # print(tmp[1])
        pcode = parent["code"][0:7]
        if(root["code"] in zxs):
            pcode = parent["code"][0:6]
        if(tmp["properties"]["name"] == parent["name"] and 
           tmp["properties"]["gb"].startswith ( pcode) and tmp["properties"]["gb"] in zx and tmp["properties"]["name"] == zx[tmp["properties"]["gb"] ] ):
            parent["child"].append(tmp2);
            # mapp = ["台湾省","156710000","台湾省","156710000","嘉义县","156716000"]
            mapp[tmp2["code"]] = [root["name"], root["code"], parent["name"], parent["code"], tmp2["name"], tmp2["code"]]
            sqls22 = sqls22 + "INSERT INTO t_address VALUES (null, '{}', '{}', '{}', '{}', '{}', '{}');".format(
                parent["code"],parent["name"],tmp2["code"],tmp2["name"], root["code"], root["name"]
            )
            fa = True
            break
            # print("直辖" + tmp2["name"])
      
        
        pass
    
    if(fa == True):
        return
    if( parent["code"].endswith("0") == False):
        return        
    for tmp in areas["features"]:
        # print("=============")
        # print(tmp[1])
        tmp2 = {
                        "name":tmp["properties"]["name"],
                        "code":tmp["properties"]["gb"],
                        "parentCode":str(parent["code"]),
                        "level":3
                    }
       
        # print("=============")
        # print(tmp[1])
        pcode = parent["code"][0:7]
        if(root["code"] in zxs):
            pcode = parent["code"][0:6]
        if(  tmp["properties"]["gb"].startswith ( pcode )):
            
            parent["child"].append(tmp2);
            # mapp = ["台湾省","156710000","台湾省","156710000","嘉义县","156716000"]
            mapp[tmp2["code"]] = [root["name"], root["code"], parent["name"], parent["code"], tmp2["name"], tmp2["code"]]
            sqls22 = sqls22 + "INSERT INTO t_address VALUES (null, '{}', '{}', '{}', '{}', '{}', '{}');".format(
                parent["code"],parent["name"],tmp2["code"],tmp2["name"], root["code"], root["name"]
            )
        
        pass


#查找市区
def findcity(parent):
    parent["child"] = []
    for tmp in  citys["features"]:
        if(tmp["properties"]["gb"].startswith ( parent["code"][0:5])):
            tmp3 = {
                "name":tmp["properties"]["name"],
                "code":tmp["properties"]["gb"],
                "parentCode":str(parent["code"]),
                "level":2
            }
            parent["child"].append(tmp3);
            findarea(tmp3, parent)
    pass

sheet2.loc[(sheet2['省gb'] == 156110000) & (sheet2['市gb'] == 156110000)]
import json
res = []

x = sheet2.groupby(by=["省gb", "省name"]).count()

for i in x.iterrows():
    
    
    tmp = {
        "name":i[0][1],
        "code":str(i[0][0]),
        "child":[],
        "level":1
    }
    res.append(tmp)
    findcity(tmp)

f1 = open("tmp.json", "w",encoding="utf-8")
f1.write( json.dumps(res,ensure_ascii=False))
f1.close()

f1 = open("tmp2.txt", "w",encoding="utf-8")
f1.write( sqls22)
f1.close()

f1 = open("tmp3.txt", "w",encoding="utf-8")
f1.write( json.dumps(mapp,ensure_ascii=False))
f1.close()


# 验证导出的地址, 有没有区为空的
for tmp in res:
    for c in tmp["child"]:
        
        if(len(c["child"]) == 0):
            print(c["name"])