#!/usr/bin/env python
# Copyright: (c) OpenSpug Organization. https://github.com/openspug/spug
# Copyright: (c) <spug.dev@gmail.com>
# Released under the AGPL-3.0 License.
"""Django's command-line utility for administrative tasks."""
import os
import sys
from ddtrace import tracer
import logging

os.environ["DD_SERVICE"] = "Python-spug"    # 设置服务名
os.environ["DD_ENV"] = "Testing"          # 设置环境名
os.environ["DD_VERSION"] = "V1.1"         # 设置版本号
os.environ["DD_LOGS_INJECTION"] = "true"  # 开启log注入
os.environ["DD_REMOTE_CONFIGURATION_ENABLED"] = "true"  # 开启log注入
os.environ["DD_AGENT_HOST"] = "47.106.191.26"  #datakit host
os.environ["DD_AGENT_PORT"] = "9529"  #datakit port

print(os.environ["DD_SERVICE"],)
print(os.environ["DD_AGENT_HOST"],)
print(os.environ["DD_AGENT_PORT"],)


FORMAT = ('%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] '
          '[dd.service=%(dd.service)s dd.env=%(dd.env)s dd.version=%(dd.version)s dd.trace_id=%(dd.trace_id)s dd.span_id=%(dd.span_id)s] '
          '- %(message)s')
logging.basicConfig(level=logging.info, format=FORMAT)

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spug.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        )
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
