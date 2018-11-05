from reportlab.lib.pagesizes import A4, portrait, landscape
from reportlab.pdfgen import canvas
import os


def convert_images_to_pdf(img_path, pdf_path):
    pages = 0
    (w, h) = portrait(A4)
    c = canvas.Canvas(pdf_path, pagesize=portrait(A4))
    ls = os.listdir(img_path)
    ls.sort(key=lambda x: int(x[-7:-4]))
    for i in ls:
        f = img_path + os.sep + str(i)
        c.drawImage(f, 0, 0, w, h)
        c.showPage()
        print('添加' + str(i))
        pages = pages + 1
    c.save()
    print('合并完成')


if __name__ == '__main__':
    convert_images_to_pdf('F:\\Overlord+Novel+v01-08\\Novel Overlord v01-08\\オーバーロード 1 不死者の王', 'F:\\Overlord+Novel+v01-08\\Novel Overlord v01-08\\オーバーロード 1 不死者の王_result.pdf')
