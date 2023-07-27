import os
from configparser import ConfigParser

cf = ConfigParser()
cf.read("spug.conf")
# ddtrace环境变量
os.environ["DD_SERVICE"] = cf["ddtrace"]["dd_service"]   # 设置服务名
os.environ["DD_ENV"] =  cf["ddtrace"]["dd_env"]           # 设置环境名
os.environ["DD_VERSION"] = cf["ddtrace"]["dd_env"]          # 设置版本号
os.environ["DD_LOGS_INJECTION"] = cf["ddtrace"]["dd_logs_injection"]  # 开启log注入
os.environ["DD_REMOTE_CONFIGURATION_ENABLED"] = cf["ddtrace"]["dd_remote_configuration_enabled"]  # 开启log注入
os.environ["DD_AGENT_HOST"] = cf["ddtrace"]["dd_agent_host"]   #datakit host
os.environ["DD_AGENT_PORT"] = cf["ddtrace"]["dd_agent_port"]  #datakit port

# mysql环境变量
os.environ["MYSQL_DATABASE"] = cf["mysql"]["db_name"] 
os.environ["MYSQL_USER"] = cf["mysql"]["db_user"] 
os.environ["MYSQL_PASSWORD"] = cf["mysql"]["db_password"] 
os.environ["MYSQL_HOST"] = cf["mysql"]["db_host"] 
os.environ["MYSQL_PORT"] = cf["mysql"]["db_port"]
print(os.environ.get("DD_SERVICE"),"==============================================================ssssssssssss")
