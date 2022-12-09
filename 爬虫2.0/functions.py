import time
import random
import requests


def drop_down(driver):
    for x in range(1, 12, 2):
        time.sleep(1)
        j = x / 9
        #通过selenium 实现JS操作
        js = "document.documentElement.scrollTop = document.documentElement.scrollHeight * %f" % j
        driver.execute_script(js)

