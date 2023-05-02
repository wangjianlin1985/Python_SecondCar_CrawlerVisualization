scrapy crawl my_spider  爬取数据

python GraphReport.py 生成报表

Python - Python 3.6.8
pycharm - PyCharm Community Edition 2020.3.2

爬虫环境

程序开发软件：Pycharm  数据库：mysql

  现在介绍的是一个用Python开发的爬取二手车网站数据及其分析的程序。爬取的时候采用selenium驱动google浏览器进行数据的抓取，抓取的网页内容传入lxml模块的etree对象HTML方法通过xpath解析DOM树，不过二手车的关键数据比如二手车价格，汽车表显里程数字采用了字体文件加密，这里我们只能随机生成一个价格用于演示程序的完整运行，如果想破解的话可能要截图后利用图片识别技术了。然后数据的展示采用pyecharts，它是一个用于生成 Echarts 图表的类库。爬取的数据插入mysql数据库和分析数据读取mysql数据库表都是通过pymysql模块操作！
