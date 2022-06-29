#!/usr/bin/python3
# http://initd.org/psycopg/docs/usage.html
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

# def provenance():
#     raws=['carto','tableaux_de_bord']
#     nb_provenance=[]
#     for name in raws :
#         sql = "SELECT count(*) FROM consultations.consultations_indicateurs WHERE consultations.consultations_indicateurs.provenance={}".format(name)
#         cur.execute(sql)
#         # Fetch data line by line
#         raw = cur.fetchone()
#         nb_provenance.append(raw)
#     return raw[0]

# print(provenance())

def provenance_tot():
    sql = "SELECT DISTINCT count(*) FROM consultations.consultations_indicateurs"
    cur.execute(sql)
    # Fetch data line by line
    raw = cur.fetchone()
    return raw[0]

def provenance_carto():
    
    sql = "SELECT DISTINCT count(*) FROM consultations.consultations_indicateurs WHERE consultations.consultations_indicateurs.provenance='carto'"
    cur.execute(sql)
    # Fetch data line by line
    raw = cur.fetchone()
    return raw[0]


def provenance_tdb():
    
    sql = "SELECT DISTINCT count(*) FROM consultations.consultations_indicateurs WHERE consultations.consultations_indicateurs.provenance='tableaux_de_bord'"
    cur.execute(sql)
    # Fetch data line by line
    raw = cur.fetchone()
    return raw[0]

def provenance_filtre():
    sql="SELECT DISTINCT count(*) FROM consultations.consultations_indicateurs WHERE consultations.consultations_indicateurs.provenance LIKE 'filtre%'"
    cur.execute(sql)
    # Fetch data line by line
    raw = cur.fetchone()
    return raw[0]

nb_autre=provenance_tot()-provenance_tdb()-provenance_carto()-provenance_filtre()
plt.figure(figsize = (8, 8))
x=[provenance_carto(),provenance_filtre(),provenance_tdb(),nb_autre]
plt.pie(x, labels=['carto','filtre','tableaux de bord', 'autre'])
plt.title('Provenance de la consultation indicateur ')
plt.show()

conn.close()
