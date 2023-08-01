#!/bin/bash
# Copyright: (c) OpenSpug Organization. https://github.com/openspug/spug
# Copyright: (c) <spug.dev@gmail.com>
# Released under the AGPL-3.0 License.
# start worker service
cd /data/spug/spug_api/

python3 manage.py updatedb
python3 manage.py user add -u admin -p admin -s -n admin

exec ddtrace-run python3 manage.py runserver
