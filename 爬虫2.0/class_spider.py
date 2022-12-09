import csv
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By  #selenium4 选择元素类
from get_user_agent import get_user_agent_of_pc


class jd_spider():
    """爬取京东商品数据,提供一个页数参数,默认为1"""

    def __init__(self, page_number=1):
        fieldnames = [  #字典写入模式
            "商品描述", "店铺", "价格", "评论数量", "商品链接", "图片地址"
        ]
        jd_url = "https://www.jd.com"
        page_number = self.page_number


    def csv_initer(self, csv_filename):
        "初始化csv文件"
        file = open("csv_results/result.csv",
                    mode="a",
                    encoding="utf-8",
                    newline="")
        #字典写入模式
        csv_writer = csv.DictWriter(
            file,
            fieldnames = self.field_names)
        # 写入表头
        csv_writer.writeheader()

    def 


