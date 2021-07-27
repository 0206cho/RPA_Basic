from openpyxl import load_workbook
wb = load_workbook("sample_5.xlsx")
ws = wb.active

# 8번째 줄이 비워짐
# ws.insert_rows(8)

# 8번쨰 줄 위치에 5줄 추가
# ws.insert_rows(8,5)

# wb.save("sample_insert_rows.xlsx")


# 새로운 빈 열이 추가 - B열 비어짐
# ws.insert_cols(2)

# B번열부터 3열 추가
# ws.insert_cols(2, 3)
wb.save("sample_insert_cols.xlsx")