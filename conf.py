# coding:utf-8
import os

env_dist = os.environ
db_url1 = "http://couchdb"
db_url1 += env_dist.get('DB_URL')
db_url1 += ":5984"

db_url = db_url1    # "http://couchdb1:5984"
bootstrap_host = "192.168.118.131"
bootstrap_port = 5678
listen_port = 5678
