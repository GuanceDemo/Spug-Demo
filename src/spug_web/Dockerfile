FROM centos:7.9.2009

ENV TZ=Asia/Shanghai
RUN mkdir -p /data/spug/spug_web && mkdir -p /data/repos
WORKDIR /data/spug/spug_web
# 导入rum的环境变量
RUN echo "export DATAKIT_ORIGIN='http://47.106.191.26:9529'" >> ~/.bashrc && echo "export RUM_ENV=test" >> ~/.bashrc && echo "export RUM_VERSION=1.0" >> ~/.bashrc && echo "export RUM_SERVICE=spug_web" >> ~/.bashrc
RUN echo "export SESSION_SAMPLE_RATE=100" >> ~/.bashrc && echo "export SESSION_REPLAY_SAMPLE_RATE=100" >> ~/.bashrc && echo "export allowedTracingOrigins='[/.*/]'" >> ~/.bashrc
RUN source ~/.bashrc

#RUN yum install -y epel-release https://packages.endpointdev.com/rhel/7/os/x86_64/endpoint-repo.x86_64.rpm && yum install -y --setopt=tsflags=nodocs nginx redis mariadb-devel python36 python36-devel openldap-devel supervisor git gcc wget unzip net-tools sshpass rsync sshfs && yum -y clean all --enablerepo='*'
RUN yum install -y epel-release https://packages.endpointdev.com/rhel/7/os/x86_64/endpoint-repo.x86_64.rpm && yum install -y --setopt=tsflags=nodocs nginx wget unzip npm net-tools && yum -y clean all --enablerepo='*'
RUN localedef -c -i en_US -f UTF-8 en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8
RUN echo -e '\n# Source definitions\n. /etc/profile\n' >> /root/.bashrc
RUN rm -rf ./build/

# RUN npm install
COPY ./node_modules/ /data/spug/spug_web/node_modules
COPY ./public/ /data/spug/spug_web/public
COPY ./src/ /data/spug/spug_web/src
COPY ./jsconfig.json /data/spug/spug_web/
COPY ./config-overrides.js /data/spug/spug_web/
COPY ./nginx.conf /data/spug/spug_web/
COPY ./package-lock.json /data/spug/spug_web/
COPY ./package.json /data/spug/spug_web/

RUN cd /data/spug/spug_web/ 
RUN npm install -g npm@9.8.1
RUN ls
RUN npm run build
RUN ls
#COPY ./build /data/spug/spug_web/build
COPY ./nginx.conf /etc/nginx/
VOLUME /data
EXPOSE 80
CMD ["nginx"]
