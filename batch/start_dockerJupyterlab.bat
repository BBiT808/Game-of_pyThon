@echo off
echo jupyter lab starting...
timeout 10 /nobreak
docker run --hostname=JUPYTERLAB --user=pkdata --env=PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin --volume=D:\keh\code:/home/pkdata/pkdata:rw --network=dbtest_db_net --workdir=/home/pkdata -p 22:22 -p 8888:8888 --restart=always --label='com.docker.compose.config-hash=2ef0d732ddbfd9a689b370e2d9bf4c4472d59a71c0e137f81d2ab7e0a05f4ae8' --label='com.docker.compose.container-number=1' --label='com.docker.compose.depends_on=' --label='com.docker.compose.image=sha256:35b2235b8184c76c86e7915b98bfd8f2290e4e889bdee7ce4cb48bf752d478d3' --label='com.docker.compose.oneoff=False' --label='com.docker.compose.project=dbtest' --label='com.docker.compose.project.config_files=D:\keh\code\dockerfile_data\DBtest\docker-compose.yml' --label='com.docker.compose.project.working_dir=D:\keh\code\dockerfile_data\DBtest' --label='com.docker.compose.service=jupyterlab1' --label='com.docker.compose.version=2.33.1' --label='maintainer=EH image https://github.com/BBiT808/Game-of_pyThon' --label='org.opencontainers.image.ref.name=ubuntu' --label='org.opencontainers.image.version=22.04' --runtime=runc -d dbtest-jupyterlab1

python dockerjupyterlab.py

pause