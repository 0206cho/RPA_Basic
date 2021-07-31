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
import time
import datetime

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
size = os.path.getsize("10_log.py")
print(size)