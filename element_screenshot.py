"""
一个根据元素截图的模块，原理是先截一张完整的图再按照元素的位置裁切
"""
from selenium import webdriver
from PIL import Image
from io import BytesIO
import time\


url = 'https://learnopengl.com/Getting-started/OpenGL'
browser = webdriver.Chrome()  # 实例化一个webdriver
browser.maximize_window()
browser.get(url)

content = browser.find_element_by_id('content')
location = content.location  # 获取对象的位置
size = content.size  # 获取对象的大小

# 通过执行一段js脚本让页面滚动到底
# 解决截图不全的问题
for i in range(5):
    browser.execute_script('window.scrollBy(0,800);')
    time.sleep(0.5)
'''
browser.execute_script("""var delay = 10;//in milliseconds
var scroll_amount = 10;// in pixels
var interval;
function scroller() {
    var old = document.body.scrollTop;//保存当前滚动条到顶端的距离
    document.body.scrollTop += scroll_amount;//让滚动条继续往下滚动
    if (document.body.scrollTop == old) {//到底部后就无法再增加scrollTop的值
        clearInterval(interval);
    }
}
function scrollToBottom()
{
  interval = setInterval("scroller()",delay);
}

scrollToBottom()""")
'''
shotimg = browser.get_screenshot_as_png()  # 截取整个页面
# browser.quit()
im = Image.open(BytesIO(shotimg))  # uses PIL library to open image in memory
left = location['x']
top = location['y']
right = location['x'] + size['width']
bottom = location['y'] + size['height']

# im = im.crop((left, top, right, bottom)) # defines crop points
im.save('screenshot.png') # saves new cropped image
