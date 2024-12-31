# geodeparse
逆地址编码,实现gps定位解析省市县编码及地名，数据采集于2024.5月，希望帮助到大家。

项目提供统一的json和sql文件，以及默认逆地址编码解析服务实现。

文件目录列表：
- `address.json`文件用于前端项目使用,树形json
- `t_address.sql`数据表包含数据,方便后端导入使用
- `xzqh2020-03.xlsx`天地图省市区编码下载源文件


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

数据来源于政府网站：天地图，于2024.5月收集的数据（审图号：GS（2024）0650号）。

官网： http://lbs.tianditu.gov.cn/server/guide.html

# 附加数据
1. 高德地址逆编码：https://lbs.amap.com/demo/javascript-api/example/geocoder/regeocoding



# 版本记录

v1.0.3 
- 修复天地图geojson和excel数据表格数据不一致问题
- geojson中增加港澳台的解析

v0.0.1
- geoparse 发布