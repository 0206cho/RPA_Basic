import pyautogui

fw = pyautogui.getActiveWindow() # 현재 활성화된 윈도우 창
print(fw.title)