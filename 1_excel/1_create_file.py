from openpyxl import Workbook # openpyxl사용하기 위해서
wb = Workbook() # 엑셀의 새 워크북 생성
ws = wb.active # 현재 활성화된 Sheet가져옴
ws.title = "NadoSheet" # 워크 시트의 이름 변경
wb.save("sample.xlsx") # 파일 저장
wb.close() # 파일 닫기