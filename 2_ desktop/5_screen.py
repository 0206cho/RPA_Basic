import pyautogui
# 스크린 샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshot.png") #파일로 저장

# 위치 정보
# pyautogui.mouseInfo()
# 965,18 81,0,81 #510051

# 픽셀의 RGB 값 출력
pixel = pyautogui.pixel(965,18) #주어진 좌표 값에 해당하는 픽셀을 가져옴
print(pixel)

# 내가 클릭하려고 하는 부분의 RGB값을 비교해 정말 그곳이 맞는지 판단 - 맞으면 True
# print(pyautogui.pixelMatchesColor(965,18, (81,0,81)))
print(pyautogui.pixelMatchesColor(965,18, pixel))