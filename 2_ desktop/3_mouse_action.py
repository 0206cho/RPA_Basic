import pyautogui
# 클릭할 좌표확인
# pyautogui.sleep(3) # 3초 대기
# print(pyautogui.position())

# pyautogui.click(961, 17, duration=1) # 1초동안 (961, 17)좌표로 이동 후  마우스 클릭
# pyautogui.click() # 마우스 클릭 - Down + Up

# 보통은 클릭을 쓰고, 얘네는 드래그 앤 드랍할 때 사용
# pyautogui.mouseDown() # 마우스 버튼 클릭하고 있는 상태
# # pyautogui.mouseUp() # 마우스 버튼에서 손을 뗀 상태

# 더블클릭
# pyautogui.doubleClick()
# pyautogui.click(clicks=2)

# 드래그앤 드롭
# pyautogui.moveTo(100,100)
# pyautogui.mouseDown() # 마우스 버튼 누른 상태
# pyautogui.moveTo(200, 300)
# pyautogui.mouseUp() # 마우스 버튼 뗸 상태

# 오른쪽 클릭
# pyautogui.rightClick()

# 왼쪽 클릭
# pyautogui.leftClick()

# 마우스 휠 클릭
# pyautogui.middleClick()

# 마우스 드래그
# print(pyautogui.position())
# pyautogui.moveTo(652, 572)
# pyautogui.drag(100,0) # 현재 위치 기준으로 x100만큼 y 0만큼 드래그
# pyautogui.drag(100,0, duration=0.25) #너무 빠른 동작으로 drag 수행이 안될 떄는 duration설정
# pyautogui.dragTo(1152, 572, duration=0.25) #절대 좌표 기준으로 드래그

# 마우스 스크롤
pyautogui.scroll(-300) # 양수이면 위 방향으로, 음수이면 아래 방향으로 300만큼 스크롤
