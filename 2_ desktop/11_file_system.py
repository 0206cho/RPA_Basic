# 파일 기본
import os
# print(os.getcwd()) # current woking directory 현재 작업 공간

# 작업공간 이동
# os.chdir("작업공간") # rpa_basic으로 작업 공간 이동
# print(os.getcwd())

# 부모 폴더로 이동
# os.chdir("..")
# print(os.getcwd())

# 조부모 폴더로 이동
# os.chdir("../..")
# print(os.getcwd())

# 주어진 절대 경로로 이동
# os.chdir("c:/")
# print(os.getcwd())

# 파일경로 만들기 - 절대경로 생성
# file_path = os.path.join(os.getcwd(), "my_file.txt") #os.path.join : 다 더함
# open(file_path, ...) # 절대경로로 작업 가능

# 파일 경로에서 폴더 정보 가져오기 - 파일명 제외한 경로 가져옴
# print(os.path.dirname(r"D:/RPA/rpa_basic/2_ desktop/11_file_system.py")) # r : 문자 그래도 적어줌

# 파일 정보 가져오기
# import time
# import datetime

# 파일의 생성 날짜
# ctime = os.path.getctime("10_log.py")
# print(ctime)
# 날짜 정보를 strftime 을 통해서 년월일 시분초 형태로 출력
# print(datetime.datetime.fromtimestamp(ctime))
# print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))

# 파일의 수정 날짜
# mtime = os.path.getmtime("10_log.py")
# print(datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d %H:%M:%S"))

# 파일의 마지막 접근 날짜
# atime = os.path.getatime("10_log.py")
# print(datetime.datetime.fromtimestamp(atime).strftime("%Y%m%d %H:%M:%S"))

# 파일 크기 - 바이트 단위
# size = os.path.getsize("10_log.py")
# print(size)

# 파일 목록 가져오기
# print(os.listdir()) # 모든 폴더, 파일 목록 가져오기
# (X
# print(os.listdir("rpa_basic")) # 주어진 폴더 밑에서 모든 폴더, 파일 목록 가져오기

# 하위 폴더 모두 포함해서 파일 목록 가져오기
# 현재폴더로부터 가져오고 싶으면 os.walk(.)
# result = os.walk("1_excel") # 주어진 폴더 밑에 있는 모든 폴더, 파일 목록 가져오기
#
# for root, dirs, files in result:
#     # (X
#     print(root, dirs, files)

# 폴더 내에서 특정 파일들을 찾으려면?
# name = "11_file_system.py"
# result = []
# for root, dirs, files in os.walk("."):
# # for root, dirs, files in os.walk(os.getcwd()): # 전체 경로
#     #[a.txt, b.txt, .....11_file_system.py, ...]
#     if name in files:
#         result.append(os.path.join(root, name))
#
# print(result)

# 만약 폴더 내에서 특정 패턴을 가진 파일들을 찾으려면?
# *.xlsx, *.txt, 자동화*.png
# import fnmatch # 파일 이름이 일치하는지 확인하기 위해서
# pattern = "file*.png" #.py로 끝나는 모든 파일
# result=[]
# for root, dirs, files in os.walk("."):
#     # [a.txt, b.txt, .....11_file_system.py, ...]
#     for name in files:
#         if fnmatch.fnmatch(name, pattern): # 이름이 패턴과 일치하다면
#             result.append(os.path.join(root, name))
# print(result)

# (X
# 주어진 경로가 파일인지 폴더인지 확인
# print(os.path.isdir("2_desktop")) #2_desktop은 폴더인가?
# print(os.path.isfile("2_desktop")) #2_desktop은 파일인가?

# 만약 지정된 경로에 해당하는 파일 / 폴더가 없다면?
# print(os.path.isfile("2_desktoppp")) # - flse

# 주어진 경로가 존재하는지
# if os.path.exists("trash_icon.png"):
#     print("파일 또는 폴더가 존재합니다.")
# else:
#     print("존재하지 않습니다.")

# 파일 만들기
# open("new_file.txt", "a").close() # 빈 파일 생성

# 파일명 변경하기
# os.rename("new_file.txt", "new_file_rename.txt") # new_file.txt -> new_file_rename.txt

# 파일 삭제하기
# os.remove("new_file_rename.txt")

# 폴더 만들기 - 작업공간 기준(현재경로)
# os.mkdir("new_folder")

# 폴더 만들기 - 절대 경로 기준
# os.mkdir("D:/RPA/rpa_basic/1_excel/new_folder")

# 하위 폴더를 가진 폴더 생성
# os.mkdir("new_folder/a/b/c") -> 오류
# os.makedirs("new_folders/a/b/c")

# 폴더명 변경
# os.rename("new_folder", "new_folder_rename")

# 폴더 삭제
# os.rmdir("new_folder_rename") # 폴더 안이 비었을 때만 삭제 가능
# os.rmdir("new_folders") 폴더 안에 내용이 있어서 삭제 불가능

# 폴더 안이 비어있지 않아도 완전 삭제 가능
import shutil # shell utilities
# shutil.rmtree("new_folders")

# 파일 복사하기
# 어떤 파일을 폴더 안으로 복사하기 (X
# shutil.copy("trash_icon.png", "test_folder") #복사할 파일, 복사할 위치

# 새로운 파일 이름으로 폴더 안에 복사 (X
# shutil.copy("trash_icon.png", "test_folder/copied_trash_icon.png") # 복사할 파일, 복사할 위치(파일명까지- 파일명변경가능)

# 원본파일 경로, 대상 파일경로까지 - 폴더명만 적으면 오류. 파일명까지 적어야함 (X
# shutil.copyfile("trash_icon.png", "test_folder/copied_trash.png")

# 원본 파일 경로, 대상폴더(파일 경로) (X
# shutil.copy2("check.png", "test_folder/copied2_check.png")

# copy, copyfile : 메타정보 복사 (x
# copy2 : 메타정보복사 O

# 폴더 복사 (X
# shutil.copytree("1_excel", "1_excel_copy") # 원본 폴더 경로, 대상 폴더 경로

# 폴더 이동 (X
# shutil.move("test_folder", "test_folder2")
# 기존 폴더명, 이동할 폴더명 -> 만약 기존 폴더명이 없으면 이동할 폴더명으로 폴더명이 변경됨
# 기존 폴더명이 있고, 이동할 폴더명이 없으면 이동할 폴더명이 기존폴더명으로 변경
