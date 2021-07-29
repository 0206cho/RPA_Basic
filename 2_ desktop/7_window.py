import pyautogui
# 현재 활성화된 윈도우 창 정보
# fw = pyautogui.getActiveWindow()
# print(fw.title) # 창의 제목정보
# print(fw.size)  # 창의 크기정보(width, height)
# print(fw.left, fw.top, fw.right, fw.bottom)  # 창의 좌표정보
# pyautogui.click(fw.left + 25, fw.top + 20)

#모든 윈도우 가져오기
# for w in pyautogui.getAllWindows():
#     print(w)

# 지정한 타이틀의 윈도우 정보만 가져오기
# for w in pyautogui.getWindowsWithTitle("제목 없음"):
#     print(w)

# 지정한 타이틀의 윈도우 정보 중에서 제일 첫번째에 있는 윈도우
w = pyautogui.getWindowsWithTitle("제목 없음")[0]
print(w)

if w.isActive == False: # 현재 활성화가 되지 않았다면
    w.activate() #활성화(맨앞으로가져오기)

# if w.isMinimized == False: # 현재 최소화가 되지 않았다면
#     w.minimize() # 최소화

if w.isMaximized == False: # 현재 최대화가 되지 않았다면
    w.maximize() # 최대화

pyautogui.sleep(1)

w.restore() # 화면 원복

w.close() # 윈도우 닫기