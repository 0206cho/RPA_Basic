import pyautogui
# 사진과 동일한 부분을 클릭
# file_menu = pyautogui.locateOnScreen("file_menu.png") #file_menu.png이미지의 정보를 찾아 반환
# print(file_menu)
# pyautogui.click(file_menu)

# 사진의 위치로 마우스 이동
# trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon)

# 사진이 없는 경우 - None
# screen = pyautogui.locateOnScreen("screenshot.png")
# print(screen)

# 체크박스 3개 한번에 클릭
# for i in pyautogui.locateAllOnScreen("checkbox.png"): # 이미지의 모든 정보 가져옴
#     print(i)
#     pyautogui.click(i)

# 위와 동일한 작업을 locateOnScreen으로 할 경우 - 맨 처음 체크박스만 표시됨
# checkbox = pyautogui.locateOnScreen("checkbox.png")
# pyautogui.click(checkbox)

# 속도 개선
# 1. GrayScale - 컬러로 되어 있는 이미지를 흑백으로 전환 후 비교 30% 속도 개선 -> 정확도는 떨어질 수 있음
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale=True)
# pyautogui.moveTo(trash_icon)

# 2. 범위 지정 - 원래는 전체 범위에서 찾았지만 region을 이용하면 지정한 범위에서만 찾음
# pyautogui.mouseInfo()
# 1541,490 240,240,240 #F0F0F0
# 1766,751 255,255,255 #FFFFFF

# trash_icon = pyautogui.locateOnScreen("trash_icon.png", region=(1541, 490, 1766-1541, 751-490))
# pyautogui.moveTo(trash_icon)

# 3. 정확도 조정 - 픽셀 하나하나가 완전히 똑같지 않아도 몇 % 이상이면 똑같다고 인식하는거
# check = pyautogui.locateOnScreen("check.png", confidence=0.9) # confidence : 기본값 0.99로 99%
# pyautogui.moveTo(check)