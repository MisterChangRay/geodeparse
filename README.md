# geodeparse
逆地址编码,实现gps定位解析省市县编码及地名，数据采集于2024.12月，希望帮助到大家。

此数据未我司线上使用数据，geo数据不免费。请酌情使用此分支

项目提供统一的json和sql文件，以及默认逆地址编码解析服务实现。

文件目录列表：
- `address.json`文件用于前端项目使用,树形json
- `t_address.sql`数据表包含数据,方便后端导入使用
- `ok_geo.csv.7z`地图省市区编码下载源文件


# 使用方式
1. clone项目
2. 安装python3.8+版本以上
3. `pip install` 安装依赖
4. 执行`server.py`启动项目
5. 使用接口访问`http://127.0.0.1:11785/geo/gps/decode`


# 本地请求示例

项目提供了测试端口方便大家测试使用（不保证稳定性）

测试域名：`http://geoparse.mtils.com/geo/gps/decode`

![image](https://github.com/user-attachments/assets/8b0a94cf-d898-4778-a208-9afa47d076c3)


# 数据来源

数据来源于另一个开源网站，这个大哥也做了很多年了。 

他的数据是从高德地图爬取的，精度比较高。天地图有个缺点就是精度不太高。有时候边界处可能会解析错误！

项目地址：https://xiangyuecn.github.io/

他家还提供街道的geo,不过是付费的。

此数据是我购买的，不免费开放。想要的可以联系Q80921006

# 附加数据
1. 高德地址逆编码：https://lbs.amap.com/demo/javascript-api/example/geocoder/regeocoding

