from selenium import webdriver
from lxml import etree
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import  By
from myproject.items import MyProjectItem

import re
import time
import random

import pymysql
connect = pymysql.connect(host='localhost', user='root', password='123456', db='base_data', port=3306)
cursor = connect.cursor()

def catchData(htmlElement):
    div_list = htmlElement.xpath("//div[@class='car-card content-item']")
    for div in div_list:
        #title = div.xpath("./img/@alt")[0]
        title = div.xpath("./h5/text()")[0]
        title = re.sub(r"\n", "", title).strip()
        title = title.split(" ")
        item = MyProjectItem()
        if len(title) == 4:
            item['brand'] = title[0]  #汽车品牌
            item['series'] = title[0]  #汽车系列
            item['model'] = "".join(title[1])  #汽车款式
        else:
            item['brand'] = title[0]
            item['series'] = title[1]
            item['model'] = "".join(title[2])

        purchased = div.xpath("./div[@class='card-tags']/text()")[0]
        purchased = re.sub(r"\n", "", purchased).strip()
        item['purchased'] = purchased  # 购买年份


        mileage = div.xpath("./div[@class='card-tags']/span[@class='gzfont']/text()")[0]
        mileage = re.sub("\\ue9ce", "0", mileage)
        mileage = re.sub("\\ue41d", "1",  mileage)
        mileage = re.sub("\\ue630", "2", mileage)
        mileage = re.sub("\\ueaf2", "3", mileage)
        mileage = re.sub("\\ue325", "4", mileage)
        mileage = re.sub("\\ue891", "5", mileage)
        mileage = re.sub("\\uec4c", "6", mileage)
        mileage = re.sub("\\ue1d0", "7", mileage)
        mileage = re.sub("\\ue76e", "8", mileage)
        mileage = re.sub("\\ue52e", "9", mileage)

        price = div.xpath("./div[@class='card-price']/p/span[@class='gzfont']/text()")

        item['mileage'] = round(random.uniform(0, 20),2) #随机公里
        item['price'] = round(random.uniform(5, 50),2)  #随机价格

        cursor.execute(
            'INSERT INTO data_info(car_brand, car_series, car_model, car_purchased, car_mileage, car_price)VALUES'
            '("{}","{}","{}","{}","{}","{}")'.format(
                item['brand'], item['series'], item['model'], item['purchased'], item['mileage'], item['price']))
        connect.commit()

if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
    driver.get("https://www.guazi.com/buy#bread")
    

