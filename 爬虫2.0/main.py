import csv
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By  #selenium4 选择元素类
from get_user_agent import get_user_agent_of_pc

#数据保存
file = open("csv_results/result.csv", mode="a", encoding="utf-8", newline="")
csv_writer = csv.DictWriter(
    file,
    fieldnames=[  #字典写入模式
        "商品描述", "店铺", "价格", "评论数量", "商品链接", "图片地址"
    ])
csv_writer.writeheader()  #写入表头

options = webdriver.EdgeOptions()
options.add_argument(f'user-agent={get_user_agent_of_pc()}')
driver = webdriver.Edge()  #启动浏览器驱动
driver.get("https://www.jd.com")  #让对象打开浏览器打开指定网址
driver.maximize_window()  #最大化浏览器
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR, "#key").send_keys("书")  #执行搜索操作
driver.find_element(By.CSS_SELECTOR,
                    "#search > div > div.form > button").click()

# 下滑操作函数
def drop_down():
    for x in range(1, 12, 1):
        time.sleep(1)
        j = x / 9
        #通过selenium 实现JS操作
        js = "document.documentElement.scrollTop = document.documentElement.scrollHeight * %f" % j
        driver.execute_script(js)

def get_page_info():
    """获取每一个页面信息的函数"""
    driver.implicitly_wait(10)
    drop_down()
    time.sleep(2) #暂停两秒，防止图片加载不出来
    lst = driver.find_elements(By.CSS_SELECTOR, ".goods-list-v2 .gl-item")

    #遍历每一个商品块元素
    for li in lst:
        #商品名
        title = li.find_element(By.CSS_SELECTOR, ".p-name em").text.replace("\n", "")
        price = li.find_element(By.CSS_SELECTOR, ".p-price i").text
        comment = li.find_element(By.CSS_SELECTOR, ".p-commit a").text
        shop_name = li.find_element(By.CSS_SELECTOR, '.curr-shop.hd-shopname').text
        url = li.find_element(By.CSS_SELECTOR, '.p-name a').get_attribute('href')
        pic_url = li.find_element(By.CSS_SELECTOR, '.p-img img').get_attribute('src')
        #防止图片加载不出来
        times = 1 #图片加载次数
        while (pic_url == None and times < 10):
            pic_url = li.find_element(By.CSS_SELECTOR, '.p-img img').get_attribute('src')

        # 存储数据到csv
        dit = {
            "商品描述": title,
            "店铺": shop_name,
            "价格": price,
            "评论数量": comment,
            "商品链接": url,
            "图片地址": pic_url
        }
        csv_writer.writerow(dit)

        # 保存商品图片
        img_name = pic_url.split("/")[-1]
        headers = {"user-agent": get_user_agent_of_pc()}
        response = requests.get(pic_url, headers = headers)
        img_data = response.content
        
        with open("pic_results/" + img_name, "wb") as f:
            f.write(img_data)


start_time = time.time()

# 自定义爬取多少页，默认100页
for page in range(1,101):
    print("正在爬取 {} 页".format(page))
    get_page_info()
    # 翻页功能
    button = driver.find_element(By.CSS_SELECTOR, ".pn-next")
    href = button.get_attribute("href")
    if href != None:
        button.click()        

end_time = time.time()
# 程序运行时间格式化输出
sum_time = int(end_time - start_time)
m, s = divmod(sum_time, 60)
h, m = divmod(m, 60)
print ("程序总用时：%02d:%02d:%02d" % (h, m, s))
