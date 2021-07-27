from openpyxl import load_workbook
wb = load_workbook("sample_5.xlsx")
ws = wb.active

# 행 데이터 삭제 - 8번쨰 줄에 있는 7번 학생 데이터 삭제
# ws.delete_rows(8)

# 여러행 데이터 삭제 - 8번째 줄부터 3줄삭제
# ws.delete_rows(8,3)

# wb.save("sample_delete_rows.xlsx")


# 열 데이터 삭제 - B열 삭제
# ws.delete_cols(2)

# 여러열 데이터 삭제 - B,C열 삭제
ws.delete_cols(2,2)
wb.save("sample_delete_col.xlsx")