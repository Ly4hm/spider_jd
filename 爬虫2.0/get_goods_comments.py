import csv
import time
import random
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By  #selenium4 选择元素类
from get_user_agent import get_user_agent_of_pc
from functions import drop_down

# 打开csv文件
csv_file = open("csv_results/result.csv", "r", encoding="utf-8")
reader = csv.reader(csv_file)
next(reader)  #跳过第一行

def get_good_comment(url):
    "爬取指定url(商品页面)的评论信息"


start_time = time.time()

options = webdriver.EdgeOptions()
options.add_argument(f'user-agent={get_user_agent_of_pc()}')
driver = webdriver.Edge()  #启动浏览器驱动


# 从result.csv读取数据
for row in reader:
    driver.get(row[-2])  #让对象打开浏览器打开指定网址
    driver.maximize_window()  #最大化浏览器
    driver.implicitly_wait(10)
    drop_down(driver)
    f = open("csv_results/comments/{}.txt".format(row[0]), mode="a", encoding="utf-8")

    
    # for i in range(11):
    #     drop_down(driver)
    #     comments = driver.find_elements(By.CSS_SELECTOR, ".comment-con")
    #     # 遍历当前页面的评论
    #     for comment in comments:
    #         print(comment.text)
    #         # 讲评论存储到以商品名为文件名的txt文件内，每行一个评论
    #         f.write(comment.text + "\n")
        
    #     href = driver.find_element(By.CSS_SELECTOR, ".ui-pager-next").get_attribute("href")
    #     driver.get(row[-2] + href)

    f.close()
    break


time.sleep(2)