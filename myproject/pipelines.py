# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql


class MyProjectPipeline:
    def __init__(self):
        self.connect = pymysql.connect(host='localhost', user='root', password='123456', db='base_data', port=3306)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        self.cursor.execute(
            'INSERT INTO data_info(car_brand, car_series, car_model, car_purchased, car_mileage, car_price)VALUES'
            '("{}","{}","{}","{}","{}","{}")'.format(
                item['brand'], item['series'], item['model'], item['purchased'], item['mileage'], item['price']))

        self.connect.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()
