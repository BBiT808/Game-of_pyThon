#베이스 이미지
FROM ubuntu:22.04

#메타데이터 추가
LABEL maintainer="EH image https://github.com/BBiT808/Game-of_pyThon"

#시스템 업데이트
RUN apt update -y && \
       apt install -y sudo passwd openssh-server wget && \
       apt install -y nano net-tools && \
       apt install -y iputils-ping openjdk-8-jdk python3-pip && \
       apt clean && \
       rm -rf /var/lib/apt/lists/*

# 계정 생성 및 세팅
RUN groupadd pkeh && useradd -m -d /home/pkys -s /bin/bash -g pkeh -G sudo pkeh && \
       echo "pkeh:1234" | chpasswd && \
       mkdir -p /home/pkeh/.ssh && \
       chown -R pkeh:pkeh /home/pkeh && \
       echo "export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64" >> /home/pkeh/.bashrc && \
       echo "export PATH=$PATH:/home/pkys/.local/bin" >> /home/pkys/.bashrc && \
       chown pkeh:pkeh /home/pkeh/.bashrc && \
       mkdir -p /var/run/sshd && \
       echo "PermitRootLogin no" >> /etc/ssh/sshd_config && \
       echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config

#사용자 변경
USER pkeh

#작업환경 변경
WORKDIR /home/pkeh

#pip 업그레이드 및 주피터랩 설치
RUN pip install --upgrade pip && pip install jupyterlab

#ssh 서버 실행 및 주피터랩 가동(외부 접속 가능) -- 20250408 수정 !! 삭제권한 부여 !! 유성쌤 복귀 ^_^
CMD ["/bin/bash","-c","service ssh start && python3 -m jupyterlab --ip=0.0.0.0 --port=8888 --allow-root --FileContentsManager.delete_to_trash=False"]

#실행
#CMD ["/bin/bash","-c","service ssh start && exec /bin/bash"]