# coding:utf-8
import os

env_dist = os.environ
a = env_dist.get('DB_URL')

db_url = "http://couchdb19:5984"
bootstrap_host = "192.168.118.149"
bootstrap_port = 5678
listen_port = 5678