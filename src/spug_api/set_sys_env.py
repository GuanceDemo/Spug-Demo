from configparser import ConfigParser
import os
cf = ConfigParser()
cf.read("spug.conf")
print(cf["ddtrace"]["dd_service"])
print(cf["mysql"]["db_database"])
print(cf["mysql"]["db_password"] )
# ddtrace环境变量
os.environ["DD_SERVICE"] = cf["ddtrace"]["dd_service"]   # 设置服务名
os.environ["DD_ENV"] =  cf["ddtrace"]["dd_env"]           # 设置环境名
os.environ["DD_VERSION"] = cf["ddtrace"]["dd_env"]          # 设置版本号
os.environ["DD_LOGS_INJECTION"] = cf["ddtrace"]["dd_logs_injection"]  # 开启log注入
os.environ["DD_REMOTE_CONFIGURATION_ENABLED"] = cf["ddtrace"]["dd_remote_configuration_enabled"]  # 开启log注入
os.environ["DD_AGENT_HOST"] = cf["ddtrace"]["dd_agent_host"]   #datakit host
os.environ["DD_AGENT_PORT"] = cf["ddtrace"]["dd_agent_port"]  #datakit portdadassssss
print(os.environ.get('DD_SERVICE'))
# mysql环境变量
os.environ["MYSQL_DATABASE"] = cf["mysql"]["db_database"] 
os.environ["MYSQL_USER"] = cf["mysql"]["db_user"] 
os.environ["MYSQL_PASSWORD"] = cf["mysql"]["db_password"] 
os.environ["MYSQL_HOST"] = cf["mysql"]["db_host"] 
os.environ["MYSQL_PORT"] = cf["mysql"]["db_port"]
print(os.environ.get('MYSQL_PASSWORD'))
#redis
os.environ["REDIS_HOST"] = cf["redis"]["redis_host"]
os.environ["REDIS_PORT"] = cf["redis"]["redis_port"]

# rum环境变量
os.environ["APPLICATION_ID"] = cf["rum"]["applicationId"] 
os.environ["DATAKIT_ORIGIN"] = cf["rum"]["datakitOrigin"] 
os.environ["RUM_ENV"] = cf["rum"]["env"] 
os.environ["RUM_VERSION"] = cf["rum"]["version"] 
os.environ["RUM_SERVICE"] = cf["rum"]["service"] 
os.environ["SESSION_SAMPLE_RATE"] = cf["rum"]["sessionSampleRate"]
os.environ["SESSION_REPLAY_SAMPLE_RATE"] = cf["rum"]["sessionReplaySampleRate"]
os.environ["TRACK_INTERACTIONS"] = cf["rum"]["trackInteractions"]
os.environ["TRACE_TYPE"] = cf["rum"]["traceType"]
