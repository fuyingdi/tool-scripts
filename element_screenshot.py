"""
一个根据元素截图的模块，原理是先截一张完整的图再按照元素的位置裁切
"""
from selenium import webdriver
from PIL import Image
from io import BytesIO
import time
import os


def shot_whole_page(url, element_name='content', scroll=5):
    url = url
    browser = webdriver.PhantomJS()  # 实例化一个webdriver
    browser.maximize_window()
    browser.get(url)

    content = browser.find_element_by_id(element_name)
    location = content.location  # 获取对象的位置
    # print(location)
    # print(location.keys())
    size = content.size  # 获取对象的大小

    # 通过执行一段js脚本让页面渐渐的滚动到底
    # 解决截图不全的问题
    for i in range(scroll):
        browser.execute_script('window.scrollBy(0,800);')
        time.sleep(0.5)

    browser.save_screenshot('screenshot.png')  # 截取整个页面
    browser.quit()
    return location, size


def shot_element(url, element_name='content'):
    element_location,element_size = shot_whole_page(url,element_name)
    im = Image.open('screenshot.png')  # uses PIL library to open image in memory
    left = element_location['x']
    top = element_location['y']
    right = element_location['x'] + element_size['width']
    bottom = element_location['y'] + element_size['height']
    im = im.crop((left, top, right, bottom))  # defines crop points

    filecount = len(os.listdir('image'))
    im.save('image'+os.sep + 'page' + str(filecount+1) + '.png')  # saves new cropped image
    print('save screenshot as %s' % ('image'+os.sep + 'page' + str(filecount+1) + '.png'))

if  __name__ == '__main__':
    # print('fool')
    shot_element('https://learnopengl.com/Getting-started/OpenGL')