# openjdk 기반이미지 slim 버전 사용 !
FROM openjdk:17-jdk-slim

#  필수 패키지 설치 ; maven   // 설치한 다음 설치 폴더를 지우겠다!
RUN apt update && apt install -y nano maven && rm -rf /var/lib/apt/lists/*

# 작업폴더 이름 변경 가능 !!
WORKDIR /workspace