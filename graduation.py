title = "佳一中2021届18班毕业去向图"

import json
from baidugeo import Geocoder

from pyecharts import options as opts
from pyecharts.charts import Geo

#存储大学对应学生
students_data = {}

with open("students.json", "r", encoding="utf-8") as f:
    students_data = json.load(f)

g = Geocoder("t2dIEXo5A3at8GSCwLKaEsNVk6rFh3mH")
#存储大学对应的省份, 经纬度, 学生
school_data = {}

for i in students_data.keys():
    try:

        pos = g.encode(i)
        addr = g.decode(*pos)
        school_data[i] = {
            "province": addr["province"],
            "pos": pos,
            "students": students_data[i]
            }
    except Exception as e:
        print(f"查询学校 {i} 出错, 学校信息 {e.args[0]}")

print(school_data)

#存储省份对应的大学
provinces = {}
for i in school_data.keys():
    if school_data[i]["province"] not in provinces:
        provinces[school_data[i]["province"]] = []

    provinces[school_data[i]["province"]].append(i)

#绘图
g = Geo(init_opts=opts.InitOpts(page_title=title))
g.add_schema(maptype="china", selected_mode="multiple")

for i in school_data.keys():
    g.add_coordinate(i, *school_data[i]["pos"])
    print(f"学校: {i}, 位置: {school_data[i]['pos']}")

for i in provinces.keys():
    schools = provinces[i]
    points = []
    for j in schools:
        points.append([j, students_data[j]])
    print(f"省份: {i}, 位置: {points}")
    g.add(i, points, symbol_size=60, symbol="pin")


g.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
g.set_global_opts(
    title_opts=opts.TitleOpts(title=title, pos_top="bottom" )
)
g.render("index.html")