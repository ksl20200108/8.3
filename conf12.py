# coding:utf-8
import os

env_dist = os.environ
a = env_dist.get('DB_URL')

db_url = "http://couchdb12:5984"
bootstrap_host = "192.168.118.142"
bootstrap_port = 5678
listen_port = 5678