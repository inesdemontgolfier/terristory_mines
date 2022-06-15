#!/usr/bin/python3
# http://initd.org/psycopg/docs/usage.html
from symtable import Class
from this import d
from typing_extensions import dataclass_transform
import psycopg2
import datetime
from matplotlib import pyplot as plt
HOST = "localhost"
USER = "postgres"
PASSWORD = "postgres"
DATABASE = "postgres"
# Open connection
conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
# Open a cursor to send SQL commands
cur = conn.cursor()

def all_users():
    sql = "SELECT id FROM consultations.ip_localisation"
    cur.execute(sql)
# Fetch data line by line
    raw = cur.fetchall()
    for i in range(len(raw)) :
        raw[i]= int(raw[i][0])
    return raw

def user_path(user):
    path=[]
    datas= ['consultations.actions_cochees','consultations.analyses_territoriales','consultations.consultations_indicateurs']
    for data in datas: 
        sql = "SELECT  * FROM {} WHERE id_utilisateur={}".format(data, user)
        cur.execute(sql)
        raw=cur.fetchall()
        path.append(raw)
    return path
print(user_path(200))
conn.close()