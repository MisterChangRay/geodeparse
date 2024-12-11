# geodeparse
逆地址编码,实现gps定位解析省市县。

将坐标解析为省市区，提供统一的json和sql文件，可以将坐标和省市区编码进行统一转换。

文件目录列表：
- `address.json`文件用于前端项目使用,树形json
- `t_address.sql`数据表包含数据,方便后端导入使用


# 使用方式
1. clone项目
2. 安装python3.8+版本以上
3. `pip install` 安装依赖
4. 执行`server.py`启动项目
5. 使用接口访问`http://127.0.0.1:11785/geo/gps/decode`


# 本地请求示例



项目提供了测试端口方便大家使用，测试域名：`http://geoparse.mtils.com`



# 数据来源

数据来源于政府网站：天地图，于2024.5月收集的数据。

官网： http://lbs.tianditu.gov.cn/server/guide.html

# 附加数据
1. 高德地址逆编码：https://lbs.amap.com/demo/javascript-api/example/geocoder/regeocoding