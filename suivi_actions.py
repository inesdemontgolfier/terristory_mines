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
poi = pd.DataFrame(raw,columns=['id', 'id_utilisateur', 'region','code_territoire', 'type_territoire', 'nom_couche', 'cochee', 'date'])

users=all_users()
datas= {"actions_cochees":actions_cochees,"analyses_territoriales":analyses_territoriales,"consultations_indicateurs":consultations_indicateurs,"poi":poi}

def moisly_connections_unique(page,date):
    sql = "SELECT COUNT(DISTINCT id_utilisateur) FROM {} WHERE date::text LIKE {}".format(page,date)
    cur.execute(sql)
    raw = cur.fetchone()
    return raw[0]

#select only the mois and the year
today=str(datetime.date.today())[0:-3]

#we chose to visiualize datas for 1 year
year=int(today[0:4])-1
mois=int(today[-2:])

def date_to_string(year,mois):
    date = "{}-{:02}".format(year,mois)
    return date


def list_mois():
    liste_mois=[]
    year=int(today[0:4])-1
    mois=int(today[-2:])
    this_mois = date_to_string(year,mois)
    liste_mois.append(this_mois)
    for mois in range (0,12):
        if mois == 12:
            year +=1
            mois = 1
        else:
            mois+=1
        liste_mois.append(str(date_to_string(year,mois)))
    return liste_mois

def connexions_mois_unique(page):
    liste_mois = list_mois()
    data_connections_unique=[]
    for mois in liste_mois:
        data_connections_unique.append(moisly_connections_unique(page,"'{}%'".format(mois)))
    plt.bar(liste_mois,data_connections_unique,1.0)
    plt.savefig('connexion_mois')
    plt.show()
    return liste_mois, data_connections_unique 

print(connexions_mois_unique('consultations.analyses_territoriales'))
def all_users():
    sql = "SELECT id FROM consultations.ip_localisation"
    cur.execute(sql)
# Fetch data line by line
    raw = cur.fetchall()
    for i in range(len(raw)) :
        raw[i]= int(raw[i][0])
    return raw

def chemin(user):
    chemin=pd.DataFrame(columns=['id_utilisateur','date','region','database'])
    i=0
    for label in datas.keys():
        data =datas[label]
        user_consultation = data[data['id_utilisateur']==user][['date','region']]
        user_consultation = user_consultation.values.tolist()
        for line in user_consultation :
            chemin.loc[i] = [user,line[0],line[1],"{}".format(label)]
            i+=1
    chemin['date']=pd.to_datetime(chemin['date'])
    chemin.sort_values(by='date',ascending=False)
    return chemin
    
#on cherche maintenant a obtenir une database avec toutes les connections de tous les utilisateurs
def chemin_all():
    chemins=pd.DataFrame(columns=['id_utilisateur','date','region','database'])
    for user in users:
        chemin_user = chemin(user)
        chemins = pd.concat([chemin_user,chemins])
    return chemins
chemins = chemin_all()
#calculer le taux de rebond sur une page

def taux_rebond():
    one_visit=0
    users_one_visit=[]
    for user in users :
        chemin_user = chemin(user)
        if len(chemin_user)==1:
            users_one_visit.append(user)
            one_visit+=1
    return one_visit/len(users),users_one_visit


def traj_une_visite():
    chemin_une_visite = []
    for user in users_one_visit:
        chemin_une_visite.append(chemins[chemins['id_utilisateur']==user]['database'])
    return chemin_une_visite

"""
Propositions d'indicateurs :
    Actions moyennes, médianes d'affilé par table
    Table la plus choisie après une table fixée
    Temps moyen passé par table
"""

#code pour trouver la page après une page donnée
#on calcule par la même occasion le temps passé par table
def next_page():
    def create_dict(): #on crée un dict avec en clé la page de provenance et en "indice" le nomnbre de fois ou une telle page à été la suivante
        dct = dict()
        time=dict()
        for data in datas.keys() :
            dct[data]=dict()
            time[data]=[]
            for data_next in datas:
                if data_next != data :
                    dct[data][data_next]=0
        return dct,time     
    dct,time = create_dict()
    for user in users:
        chemin = chemins[chemins["id_utilisateur"]==user]
        if chemin.shape[0]==0:
            continue
        page = chemin.iloc[0]["database"]
        date = chemin.iloc[0]["date"]
        for i in range(1,chemin.shape[0]):
            page_next = chemin.iloc[i]["database"]
            if page != page_next : #on detecte un changement de la page consultée
                dct[page][page_next]+=1
                date_next= chemin.iloc[i]["date"]
                time[page].append(date_next-date)
                date=date_next
                page = page_next
    return dct , time




conn.close()