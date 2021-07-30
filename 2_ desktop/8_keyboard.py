import pyautogui
# 메모장을 찾아가서 글자를 타이핑
w = pyautogui.getWindowsWithTitle("제목 없음")[0] #메모장 1개를 띄운 상태에서 가져옴
w.activate() # 뒤에 있는 메모장을 앞으로 활성화시킴
# 영어와 숫자만 입력, 한글은 입력x
# pyautogui.write("12345")
# pyautogui.write("snoopy", interval=0.2) #interval : 글자 입력시간제어

# 키보드로 나눠서 입력 - t e s t 순서대로 적고 왼쪽 방향키 2번, 오른쪽 방향키 2번 l a 순서대로 적고 enter입력
# pyautogui.write(["t", "e","s", "t", "left","left","right","l","a","enter"], interval=0.25)

# 특수 문자 입력
# shift 4 -> $
# pyautogui.keyDown("shift") # shift 키를 누른 상태
# pyautogui.press("4") # 숫자 4를 입력하고
# pyautogui.keyUp("shift") # shift키를 뗸다

# 조합키 (Hot Key)
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a") # press("a")
# pyautogui.keyUp("ctrl") # Ctrl + A

# 간편한 조합키
# pyautogui.hotkey("ctrl", "alt", "shift", "a")
# ctrl, alt, shift, a 순서대로 누르고 a, shift, alt, ctrl 순으로 뗌
# pyautogui.hotkey("ctrl",  "a")

import pyperclip #어떤 문장을 클립보드에 집어넣음
# 한글 작성 - 클립보드로 저장해서 붙임
# pyperclip.copy("스누피") #"스누피" 글자를 클립보드에 저장
# pyautogui.hotkey("ctrl", "v") #클립보드에 있는 내용을 붙여넣기

# 위 코드 함수로 작성
# def my_write(text):
#     pyperclip.copy(text)
#     pyautogui.hotkey("ctrl", "v")
#
# my_write("스누피가 찰리찰리해해")

# ctrl + alt + del : 자동화 프로그램 종료
