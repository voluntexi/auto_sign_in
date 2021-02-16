import sys
import io
from selenium import webdriver
import time
import json
import requests
import base64
from selenium.webdriver.common.action_chains import ActionChains
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码

# 建立chrome浏览器对象，括号里是Chromedriver在你的电脑上的路径，需要修改
browser = webdriver.Chrome('E:/daka/chromedriver')
# 基本信息，需要修改
xuehao = '3120180901401'
name = '席铁钧'
password = 'xtj125478963'
# 登录页面
url = 'https://wxyqfk.zhxy.net/?yxdm=10623#/login'
browser.set_window_size(598, 702)
# 访问登录页面
browser.get(url)

# 等待一定时间，让js脚本加载完毕
browser.implicitly_wait(5)
time.sleep(3)
# print(browser.page_source.encode('utf-8').decode())
# 定位输入框并输入相关信息
browser.find_elements_by_class_name("van-field__control")[0].send_keys(xuehao)
browser.find_elements_by_class_name("van-field__control")[1].send_keys(name)
browser.find_elements_by_class_name("van-field__control")[3].send_keys(password)

# 等待一定时间，让js脚本加载完毕
browser.implicitly_wait(3)
time.sleep(2)
# browser.sleep(3)
browser.find_element_by_xpath('//button').click()
browser.implicitly_wait(3)
time.sleep(2)
# 地址重定向到登陆后页面
url2 = 'https://wxyqfk.zhxy.net/?yxdm=14262#/clockIn'
browser.set_window_size(598, 702)
browser.get(url2)
browser.implicitly_wait(10)

try:
    but = browser.find_element_by_class_name("van-button")
    but.click()
except:
    browser.get(url2)
time.sleep(2)
try:
    wenxintishi=browser.find_element_by_class_name('van-button')
    wenxintishi.click()
except:
    time.sleep(2)
    print('not find')
try:
    browser.find_element_by_class_name('sign-in-btn')
    print('跳转成功')
    browser.find_element_by_class_name('sign-in-btn')

except:
    print('跳转失败，重新跳转')
    browser.get(url2)
    time.sleep(3)
    browser.find_element_by_class_name('sign-in-btn')
    browser.find_element_by_class_name('van-button').click()

# 关闭温馨提示的框
try:
    wenxintishi=browser.find_element_by_class_name('van-button')
    print('find')
    wenxintishi.click()
except:
    time.sleep(2)
    print('not find')
time.sleep(3)
try:
    browser.find_element_by_class_name('sign-in-btn').click()
except:
    wenxintishi=browser.find_element_by_class_name('van-button')
    wenxintishi.click()
    browser.find_element_by_class_name('sign-in-btn').click()

time.sleep(3)
try:
    browser.find_element_by_tag_name('img')
    time.sleep(3)
    browser.find_element_by_class_name('sign-in-btn').click()
    try:
        browser.find_element_by_class_name('sign-in-btn').click()
    except:
        pass
except:
    pass

browser.find_elements_by_xpath('//label')[0].click()
browser.find_elements_by_xpath('//label')[6].click()
left = browser.find_element_by_name("a_12_0")
ActionChains(browser).click_and_hold(left).perform()
left = browser.find_elements_by_xpath('//label')[14].click()
ActionChains(browser).click_and_hold(left).perform()
browser.find_elements_by_xpath('//label')[20].click()
browser.find_elements_by_xpath('//label')[22].click()

time.sleep(2)

image = browser.find_element_by_tag_name('img').get_attribute('src')
try :
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
except:
    pass
print(image)

#验证码识别ocr
from recognize import recognize
from recognize import recognize2
data1 = recognize(image)
data2 = recognize2(image)
print(data1)
from recognize import json1
k = json1(data1)
m = json1(data2)
browser.find_elements_by_class_name("van-field__control")[2].send_keys(m)
time.sleep(1)
browser.find_element_by_class_name('sign-in-btn').click()
time.sleep(3)
browser.quit()


