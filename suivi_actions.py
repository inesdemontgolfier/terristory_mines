#!/usr/bin/python3
# http://initd.org/psycopg/docs/usage.html
from symtable import Class
from this import d
from typing_extensions import dataclass_transform
import psycopg2
import datetime
from matplotlib import pyplot as plt
import pandas as pd
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

"""def user_path(user):
    path=[user]
    datas= ['consultations.actions_cochees','consultations.analyses_territoriales','consultations.consultations_indicateurs']
    for data in datas: 
        sql = "SELECT  * FROM {} WHERE id_utilisateur={}".format(data, user)
        cur.execute(sql)
        raw=cur.fetchall()
        path.append(raw)
    return path
print(user_path(200))"""

#import de toutes les données pour les traiter dans pandas

cur.execute(" SELECT * from consultations.actions_cochees")
raw = cur.fetchall()
actions_cochees = pd.DataFrame(raw, columns=['id','region','listes_actions','liste_trajectoire_cible','types_actioons','date','code_territoire','type_territoire','id_utilisateur'])

cur.execute("SELECT * from consultations.analyses_territoriales")
raw = cur.fetchall()
analyses_territoriales = pd.DataFrame(raw, columns=['id','id_utilisateur','region','code_territoire','type_territoire','page','date'])

cur.execute("SELECT * from consultations.consultations_indicateurs")
raw=cur.fetchall()
consultations_indicateurs = pd.DataFrame(raw,columns=['id','provenance','region','id_indicateur','date','code_territoire','type_territoire','id_utilisateur'])

users=all_users()
datas= [actions_cochees,analyses_territoriales,consultations_indicateurs]
def path(user):
    path=pd.DataFrame(columns=['id_utilisateur','date','region','database'])
    i=0
    for data in datas:
        user_consultation = data[data['id_utilisateur']==user][['date','region']]
        user_consultation = user_consultation.values.tolist()
        for line in user_consultation :
            path.loc[i] = [user,line[0],line[1],"a"]
            i+=1
    path['date']=pd.to_datetime(path['date'])
    path.sort_values(by='date')
    return path
    
print(path(200))
conn.close()