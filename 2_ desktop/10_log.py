import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s")
# DEBUG : 디버그 레벨 이상 모든 로그를 찍어줌
# format : 로그를 어떻게 찍을 지 정의
# %(asctime)s: 시간정보 찍음, %(levelname)s: log레벨 정보, %(message)s : 사용자가 입력한 로그가 뜸

# 로그 레벨 순 : debug < info < warning < error < critical
# logging.debug("야 이거 누가 짠거야!") # 개발단계에서 쓰는거
# logging.info("자동화 수행 준비") # 정보로 실제 프로그램쓰는 사람의 pc에도 보이게
# logging.warning("이 스크립트는 조금 오래되어 실행중에 문제가 있을 수 있습니다.") # 경고
# logging.error("에러가 발생하였습니다. 에러코드는...")
# logging.critical("복구가 불가능한 심각한 문제가 발생하였습니다.") #치명적인 문제 발생

# 터미널과 파일에 함께 로그 남기기
import logging
from datetime import datetime
# 시간[로그레벨] 메시지 형태로 로그를 작성
logFormatter= logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger()
# 로그 레벨 설정
logger.setLevel(logging.DEBUG)

# 스트림(터미널)
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFormatter)
logger.addHandler(streamHandler)

# 파일
filename =datetime.now().strftime("mylogfile_%Y%m%d%H%M%S.log") # mylogfile_20210731011820.log
fileHandler = logging.FileHandler(filename, encoding="utf-8")
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

logger.debug("로그를 남기는 테스트 진행")