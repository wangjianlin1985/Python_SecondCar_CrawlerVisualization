import webbrowser as browser

import pymysql as my_sql
from pyecharts import options as opts
from pyecharts.charts import Bar, Pie, Page


def get_data():
    sql_conn = my_sql.connect(host='localhost', user='root', password='123456', db='base_data', port=3306)
    cursor = sql_conn.cursor()
    sql = 'SELECT car_brand, car_series, car_purchased, car_price FROM base_data.data_info' \
          ' GROUP BY car_brand, car_series, car_model, car_purchased' \
          ' ORDER BY rand(), car_brand, car_series, car_model, car_purchased limit 10'
    cursor.execute(sql)
    data = cursor.fetchall()
    sql_conn.close()
    return data


def get_data_top5():
    sql_conn = my_sql.connect(host='localhost', user='root', password='123456', db='base_data', port=3306)
    cursor = sql_conn.cursor()
    sql = 'SELECT car_brand, count(car_brand) as sell_count FROM base_data.data_info' \
          ' GROUP BY car_brand ORDER BY sell_count desc limit 0,5'
    cursor.execute(sql)
    data = cursor.fetchall()
    sql_conn.close()
    return data


car_list = get_data()
count_list = get_data_top5()
brand = []
price = []
count = []

for car in car_list:
    brand.append(car[0] + "\r\n" + car[1] + "\r\n" + car[2])
    price.append(car[3])

x1 = brand
y1 = price
brand = []

for car in count_list:
    brand.append(car[0])
    count.append(car[1])
x2 = brand
y2 = count


def bar_charts():
    chart_graph = Bar()
    chart_graph.width = "100%"
    # 设置x轴
    chart_graph.add_xaxis(xaxis_data=x1)

    # 设置y轴
    chart_graph.add_yaxis(series_name='单位(万元)', y_axis=y1, bar_width="50%")
    # 数据项设置
    chart_graph.set_global_opts(
        title_opts=opts.TitleOpts(title='车型价格统计图'),
        legend_opts=opts.LegendOpts(is_show=True),
        tooltip_opts=opts.TooltipOpts(trigger='axis', axis_pointer_type='cross'),
        datazoom_opts=opts.DataZoomOpts(type_="inside")
    )
    return chart_graph


def pie_charts():
    pie_chart = Pie()
    pie_chart.width = "100%"
    pie_chart.add("", [list(z) for z in zip(x2, y2)])
    pie_chart.set_global_opts(
        title_opts=opts.TitleOpts(title="在售车型品牌前五名")
    )
    pie_chart.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c} 辆"))
    return pie_chart


page = Page(layout=Page.SimplePageLayout)
page.add(pie_charts(), bar_charts())
page.render("line.html")
browser.open("line.html")
