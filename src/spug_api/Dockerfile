FROM centos:7.9.2009

ENV TZ=Asia/Shanghai
RUN echo 
RUN mkdir -p /data/repos

RUN ls
RUN pwd
COPY ./docker/init_spug /usr/bin/
#COPY ./src/docs/docker/nginx.conf /etc/nginx/
COPY ./docker/ssh_config /etc/ssh/
COPY ./docker/spug.ini /etc/supervisord.d/
COPY ./docker/redis.conf /etc/
COPY ./docker/entrypoint.sh /
COPY ./apps/ /data/spug/spug_api/apps
COPY ./consumer/ /data/spug/spug_api/consumer
COPY ./libs/ /data/spug/spug_api/libs
COPY ./logs/ /data/spug/spug_api/logs
COPY ./spug/ /data/spug/spug_api/spug
COPY ./storage/ /data/spug/spug_api/storage
COPY ./tools/ /data/spug/spug_api/tools
#COPY ./venv/ /data/spug/spug_api/venv
COPY ./manage.py/ /data/spug/spug_api/manage.py
COPY ./requirements.txt/ /data/spug/spug_api/requirements.txt
COPY ./spug.conf/ /data/spug/spug_api/spug.conf


#RUN yum install -y epel-release https://packages.endpointdev.com/rhel/7/os/x86_64/endpoint-repo.x86_64.rpm && yum install -y --setopt=tsflags=nodocs nginx redis mariadb-devel python36 python36-devel openldap-devel supervisor git gcc wget unzip net-tools sshpass rsync sshfs && yum -y clean all --enablerepo='*'
RUN yum install -y epel-release https://packages.endpointdev.com/rhel/7/os/x86_64/endpoint-repo.x86_64.rpm && yum install -y --setopt=tsflags=nodocs nginx redis mariadb-devel python36 python36-devel openldap-devel supervisor git gcc wget unzip net-tools && yum -y clean all --enablerepo='*'

RUN pip3 install --no-cache-dir --upgrade pip -i https://mirrors.aliyun.com/pypi/simple/
RUN pip3 install --no-cache-dir -i https://mirrors.aliyun.com/pypi/simple/ \
    gunicorn \
    mysqlclient \
    cryptography==36.0.2 \
    apscheduler==3.7.0 \
    asgiref==3.2.10 \
    Django==2.2.28 \
    channels==2.3.1 \
    channels_redis==2.4.1 \
    paramiko==2.11.0 \
    django-redis==4.10.0 \
    requests==2.22.0 \
    GitPython==3.0.8 \
    python-ldap==3.4.0 \
    openpyxl==3.0.3 \
    user_agents==2.2.0 \
    ddtrace==1.16.0  \
    configparser==5.2.0

RUN localedef -c -i en_US -f UTF-8 en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8
RUN echo -e '\n# Source definitions\n. /etc/profile\n' >> /root/.bashrc

VOLUME /data
EXPOSE 80
ENTRYPOINT ["sh", "/data/spug/spug_api/tools/start-server.sh"]
