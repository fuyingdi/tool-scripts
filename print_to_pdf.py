"""
用selenium批量进行print to pdf
"""
from reportlab.pdfgen import canvas
from selenium import webdriver
from PIL import Image
from reportlab.lib.pagesizes import A4,B5
from reportlab.lib.pagesizes import portrait
import os


# browser = webdriver.Chrome()


def combine_to_pdf(path):
    ls = os.listdir(path)
    can = canvas.Canvas('result.pdf',pagesize=B5)
    pages = 0
    for img in ls:
        i = Image.open(path+os.sep+img)
        assert isinstance(i, Image.Image)
        w, h = i.size
        i = i.resize((int(0.5*w), int(0.5*h)), Image.ANTIALIAS)
        i.save(path+os.sep+'副本'+img)
        can.drawImage(path+os.sep+'副本'+img, 0, 0)
        can.showPage()
        pages = pages + 1
    can.save()

if __name__ == '__main__':
    combine_to_pdf(os.getcwd()+os.sep+'image')



