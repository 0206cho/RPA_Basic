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

# 자동화 대상이 바로 보여지지 않는 경우
# 1. 계속기다리기
# file_menu_notpad = pyautogui.locateOnScreen("file_menu_notepad.png")
# # 화면에 메모장이 가려져 있으므로 file_menu_notpad는 None가 들어감
# # if file_menu_notpad:
# #     pyautogui.click(file_menu_notpad)
# # else:
# #     print("발견 실패")
# while file_menu_notpad is None: # 노트패드가 발견될까지 반복해서 찾음
#     file_menu_notpad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     print("발견 실패")
# pyautogui.click(file_menu_notpad)

# 2. 일정 시간동안 기다리기(TimeOut)
import time # 시간 사용하기 위해
import sys # 프로그램 종료하기 위해

# timeout = 10 #10초대기
# start = time.time() # 시작 시간 설정
# file_menu_notpad = None
# while file_menu_notpad is None:
#     file_menu_notpad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     end = time.time() # 종료 시간 설정
#     if end - start > timeout: # 지정한 10초를 초과하면
#         print("시간 종료")
#         sys.exit()
#
# pyautogui.click(file_menu_notpad)

# 위 코드함수로 정의
def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target

def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s] Target not found ({img_file}). Terminate program.")
        sys.exit()

my_click("file_menu_notepad.png", 10)