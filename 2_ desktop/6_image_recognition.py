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
checkbox = pyautogui.locateOnScreen("checkbox.png")
pyautogui.click(checkbox)