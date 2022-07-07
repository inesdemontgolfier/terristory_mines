#!/usr/bin/python3
# http://initd.org/psycopg/docs/usage.html
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
def moisly_connections_double(date):
    sql = "SELECT COUNT(*) FROM consultations.analyses_territoriales WHERE date::text LIKE {}".format(date)
    cur.execute(sql)
# Fetch data line by line
    raw = cur.fetchone()
    return raw[0]

def moisly_connections_unique(date):
    sql = "SELECT COUNT(DISTINCT id_utilisateur) FROM consultations.analyses_territoriales WHERE date::text LIKE {}".format(date)
    cur.execute(sql)
# Fetch data line by line
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


def liste_mois():
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

def connexions_mois_doublons():
    liste_mois = liste_mois()
    data_connections_double=[]
    for mois in liste_mois:
        try :
            data_connections_double.append(moisly_connections_double("'{}%'".format(mois)))
        except :
            data_connections_double.append(0)
    plt.bar(liste_mois,data_connections_double,1.0)
    plt.savefig('connexion_mois_double')
    plt.show()
    return liste_mois, data_connections_double

def connexions_mois_unique():
    liste_mois = liste_mois()
    data_connections_unique=[]
    for mois in liste_mois:
        try :
            data_connections_unique.append(moisly_connections_unique("'{}%'".format(mois)))
        except :
            data_connections_unique.append(0)
    plt.bar(liste_mois,data_connections_unique,1.0)
    plt.savefig('connexion_mois_unique')
    plt.show()
    return liste_mois, data_connections_unique 

connexions_mois_doublons()
connexions_mois_unique()

conn.close()