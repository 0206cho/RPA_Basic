# Quiz) 아래 동작을 자동으로 수행하는 프로그램을 작성

# 1. 그림판 실행 (단축키 : win + r , 입력값 : mspaint) 및 최대화

# 2. 상단의 텍스트 기능을 이용하여 흰 영역 아무 곳에다가 글자 입력
# - 입력 글자 : "참 잘했어요"

# 3. 5초 대기 후 그림판 종료
#  이때, 저장하지 않음을 자동으로 선택하여 프로그램이 완전 종료되도록 함


import sys
import pyautogui
import pyperclip #어떤 문장을 클립보드에 집어넣음

# 1. 그림판 실행
pyautogui.hotkey("win", "r") # 단축키 : win + r 입력
pyautogui.write("mspaint") # 프로그램 명 입력
pyautogui.press("enter") # 엔터 키 입력

# 그림판 나타날 때까지 2초 대기
pyautogui.sleep(2)

# 그림판 최대화하기 위해 윈도우로 가져오기.
window = pyautogui.getWindowsWithTitle("제목 없음 - 그림판")[0]
if window.isMaximized == False: # 만약 최대화가 되어 있지 않다면
    window.maximize() # 최대화

# 2. 상단의 텍스트 기능을 이용하여 흰 영역에 "참 잘했어요" 입력
# 글자 버튼 클릭
btn_text = pyautogui.locateOnScreen("btn_text.png") # 사진의 이미지 찾기
if btn_text: #이미지를 찾아서 btn_text가 True가 되면
    pyautogui.click(btn_text, duration=0.5)  # 그 이미지를 클릭
else:
    print("찾기 실패") # 없으면 찾기 실패 문구 띄운 후 프로그램 종료
    sys.exit()

# 흰 영역 클릭
# pyautogui.click(200,200, duration=0.5) # 흰 영역 아무 곳 클릭

# 만약 이미지가 계속해서 변한다면 안 변하는 이미지를 기준으로 상대 좌표를 줘서 선택 가능
btn_brush = pyautogui.locateOnScreen("btn_brush.png")
pyautogui.click(btn_brush.left - 200, btn_brush.top + 200)

# 한글 작성 - 클립보드로 저장해서 붙이는 함수로 작성
def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")

my_write("참 잘했어요")

# 3. 5초 대기 후 그림판 종료
# 5초 대기
pyautogui.sleep(3)

# 프로그램 종료
window.close()

# 저장 안함 선택
pyautogui.sleep(0.5) # 팝업이 늦게 뜰 가능성
pyautogui.press("n") # 저장하지 않음