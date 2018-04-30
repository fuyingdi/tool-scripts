from selenium import webdriver
from PIL import Image
from io import BytesIO
url = 'https://learnopengl.com/Getting-started/OpenGL'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

content = browser.find_element_by_id('content')
location = content.location
size = content.size

shotimg = browser.get_screenshot_as_png()
browser.quit()
im = Image.open(BytesIO(shotimg)) # uses PIL library to open image in memory
left = location['x']
top = location['y']
right = location['x'] + size['width']
bottom = location['y'] + size['height']

# im = im.crop((left, top, right, bottom)) # defines crop points
im.save('screenshot.png') # saves new cropped image
