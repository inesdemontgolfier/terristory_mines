#!/usr/bin/python3
# http://initd.org/psycopg/docs/usage.html
from symtable import Class
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

cur.execute("SELECT * from consultations.poi")
raw=cur.fetchall()
consultations_indicateurs = pd.DataFrame(raw,columns=['id', 'id_utilisateur', 'region','code_territoire', 'type_territoire', 'nom_couche', 'cochee', 'date'])

users=all_users()
datas= {"actions_cochees":actions_cochees,"analyses_territoriales":analyses_territoriales,"consultations_indicateurs":consultations_indicateurs}
def path(user):
    path=pd.DataFrame(columns=['id_utilisateur','date','region','database'])
    i=0
    for label in datas.keys():
        data =datas[label]
        user_consultation = data[data['id_utilisateur']==user][['date','region']]
        user_consultation = user_consultation.values.tolist()
        for line in user_consultation :
            path.loc[i] = [user,line[0],line[1],"{}".format(label)]
            i+=1
    path['date']=pd.to_datetime(path['date'])
    path.sort_values(by='date')
    return path
    
#on cherche maintenant a obtenir une database avec toutes les connections de tous les utilisateurs
def path_all():
    paths=pd.DataFrame(columns=['id_utilisateur','date','region','database'])
    for user in users:
        path_user = path(user)
        paths = pd.concat([path_user,paths])
    return paths
paths = path_all()
#calculer le taux de rebond sur une page

def taux_rebond():
    one_visit=0
    users_one_visit=[]
    for user in users :
        path_user = path(user)
        if len(path_user)==1:
            users_one_visit.append(user)
            one_visit+=1
    return one_visit/len(users),users_one_visit

taux, users_one_visit = taux_rebond()

def traj_one_visit():
    path_one_visit = []
    for user in users_one_visit:
        path_one_visit.append(paths[paths['id_utilisateur']==user]['database'])
    return path_one_visit
    
print(len(traj_one_visit()))


"""
Propositions d'indicateurs :
    Actions moyennes, médianes d'affilé par table
    Table la plus choisie après une table fixée
    Temps moyen passé par table
"""

def calculate_indicators(path):
    time_in_table = dict()
    next_table = dict()
    actions_in_table = dict()

    this_table = path[0]["database"]
    this_table_time = path[0]["date"]
    this_table_actions = 0

    for line in path:
        if(line["database"] != this_table):
            pass


conn.close()