import pyautogui

# 절대 좌표로 마우스 이동
# pyautogui.moveTo(200,100) # 지정한 위치(가로x, 세로y)로 마우스를 이동
#duration : 초단위, 5초동안 100, 200위치로 이동
# pyautogui.moveTo(100,200, duration=5)

# pyautogui.moveTo(100,100, duration=0.25)
# pyautogui.moveTo(200,200, duration=0.25)
# pyautogui.moveTo(300,300, duration=0.25)

# 상대 좌표로 마우스 이동(현재 커서가 있는 위치로부터)
# pyautogui.moveTo(100,100, duration=0.25)
# print(pyautogui.position()) #Point(x, y)
# pyautogui.move(100, 100, duration=0.25)  # 100, 100기준으로 +100, +100 - 200, 200
# print(pyautogui.position()) #Point(x, y)
# pyautogui.move(100, 100, duration=0.25)  # 200, 200기준으로 300. 300
# print(pyautogui.position()) #Point(x, y)

p = pyautogui.position()
print(p[0], p[1]) #x, y
print(p.x, p.y) #x, y
