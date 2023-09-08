#!/bin/bash
# Copyright: (c) OpenSpug Organization. https://github.com/openspug/spug
# Copyright: (c) <spug.dev@gmail.com>
# Released under the AGPL-3.0 License.
# start worker service

echo "export DD_SERVICE=python-spug" >> ~/.bashrc
echo "export DD_TAGS=project:mobie_sdk_demo,env:test,version:1.0" >> ~/.bashrc
#echo "export DD_AGENT_HOST=https://pe-dk.guance.space" >> ~/.bashrc
echo "export DD_AGENT_HOST=47.106.191.26" >> ~/.bashrc
echo "export DD_AGENT_PORT=9529" >> ~/.bashrc
echo "export DD_LOGS_INJECTION='true'" >> ~/.bashrc
echo "export DD_VERSION=1.1" >> ~/.bashrc
echo "export DD_REMOTE_CONFIGURATION_ENABLED='true'" >> ~/.bashrc
echo "export REDIS_HOST=mysql.spug" >> ~/.bashrc
echo "export REDIS_PORT=6379" >> ~/.bashrc
echo "export REDIS_PASSWORD=viFRKZiZkoPmXnyF" >> ~/.bashrc
source  ~/.bashrc

# 设置MySQL数据库的相关信息
DB_NAME="spug"
DB_USER="root"
DB_PASSWORD="admin@123456"

# 检查数据库是否存在
database_exists=$(mysql -u $DB_USER -p$DB_PASSWORD -e "SHOW DATABASES LIKE '$DB_NAME';" | grep "$DB_NAME")

if [ -z "$database_exists" ]; then
    # 如果数据库不存在，则创建数据库
    echo "Creating database $DB_NAME..."
    mysql -u $DB_USER -p$DB_PASSWORD -e "CREATE DATABASE $DB_NAME;"
    echo "Database $DB_NAME created successfully!"
else
    echo "Database $DB_NAME already exists."
fi



mysql -h mysql.spug -u root -padmin@123456 -e "CREATE DATABASE spug;"

cd /data/spug/spug_api/
python3 manage.py updatedb
python3 manage.py user add -u admin -p admin -s -n admin

exec ddtrace-run python3 manage.py runserver 0.0.0.0:8000
