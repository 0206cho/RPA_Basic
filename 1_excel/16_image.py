from openpyxl import Workbook
from openpyxl.drawing.image import Image #이미지를 사용하기 위해서

wb = Workbook()
ws = wb.active

img = Image("mylove.png")

#C3위치에 img.png파일의 이미지를 삽입
ws.add_image(img, "C3")

wb.save("sample_image.xlsx")

