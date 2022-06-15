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
"""
def monthly_connections(date):
    sql = "SELECT COUNT(*) FROM consultations.poi WHERE date::text LIKE {}".format(date)
    cur.execute(sql)
# Fetch data line by line
    raw = cur.fetchone()
    return raw[0]

months=[]

#select only the month and the year
today=str(datetime.date.today())[0:-3]

#we chose to visiualize datas for 1 year
year=int(today[0:4])-1
month=int(today[-2:])

def date_to_string(year,month):
    date = "{}-{:02}".format(year,month)
    return date

this_month = date_to_string(year,month)

months.append(this_month)
for i in range (0,12):
    if month == 12:
        year +=1
        month = 1
    else:
        month+=1
    months.append(str(date_to_string(year,month)))

data_connections=[]
for month in months:
    try :
        data_connections.append(monthly_connections("'{}%'".format(month)))
    except :
        data_connections.append(0)

conn.close()
"""




#Camembert des catégories

def nb_carburants():
    sql = "SELECT  COUNT(*) FROM consultations.poi WHERE nom_couche  IN ('Bornes de recharge de véhicules électriques', 'Bornes hydrogène', 'Installations GnV/bio-GnV')"
    cur.execute(sql)
    raw = cur.fetchone()
    return raw[0]
#178

carburants = nb_carburants()
print(carburants)

def nb_infrastructures():
    sql = "SELECT  COUNT(*) FROM consultations.poi WHERE nom_couche  = 'Réseaux de chaleur'"
    cur.execute(sql)
    raw = cur.fetchone()
    return raw[0]
#45
infrastructures = nb_infrastructures()
print(infrastructures)

def nb_installationsEnr():
    sql = "SELECT  COUNT(*) FROM consultations.poi WHERE nom_couche  IN ('Installations géothermiques', 'Unités de méthanisation')"
    cur.execute(sql)
    raw = cur.fetchone()
    return raw[0]
#40
installationsEnr = nb_installationsEnr()
print(installationsEnr)

def nb_déchets():
    sql = "SELECT  COUNT(*) FROM consultations.poi WHERE nom_couche  IN ('Centres de tri', 'Déchèteries', 'Installations de stockage des déchets non dangereux', 'Plateformes de compostage', 'Recycleries', 'Unités de valorisation énergétique des déchets')"
    cur.execute(sql)
    raw = cur.fetchone()
    return raw[0]
#214
déchets = nb_déchets()
print(déchets)

plt.figure(figsize = (8, 8))
x = [carburants, infrastructures, installationsEnr, déchets]
plt.pie(x, labels = ['Carburants', 'Infrastructures', 'InstallationsEnr', 'Déchets'], normalize = True)
plt.legend()
plt.show()


#Equipements un par un

def nb_bornes_elec():
    sql = "SELECT  COUNT(*) FROM consultations.poi WHERE nom_couche  = 'Bornes de recharge de véhicules électriques'"
    cur.execute(sql)
    raw = cur.fetchone()
    return raw[0]

bornes_elec = nb_bornes_elec()


def nb_bornes_hydro():
    sql = "SELECT  COUNT(*) FROM consultations.poi WHERE nom_couche  = 'Bornes hydrogène'"
    cur.execute(sql)
    raw = cur.fetchone()
    return raw[0]

bornes_hydro = nb_bornes_hydro()


def nb_install_bio():
    sql = "SELECT  COUNT(*) FROM consultations.poi WHERE nom_couche  = 'Installations GnV/bio-GnV'"
    cur.execute(sql)
    raw = cur.fetchone()
    return raw[0]

install_bio = nb_install_bio()


def nb_centres_tri():
    sql = "SELECT  COUNT(*) FROM consultations.poi WHERE nom_couche  = 'Centres de tri'"
    cur.execute(sql)
    raw = cur.fetchone()
    return raw[0]

centres_tri = nb_centres_tri()


def nb_déchèteries():
    sql = "SELECT  COUNT(*) FROM consultations.poi WHERE nom_couche  = 'Déchèteries'"
    cur.execute(sql)
    raw = cur.fetchone()
    return raw[0]

déchèteries = nb_déchèteries()


def nb_install_déchets_non_danger():
    sql = "SELECT  COUNT(*) FROM consultations.poi WHERE nom_couche  = 'Installations de stockage des déchets non dangereux'"
    cur.execute(sql)
    raw = cur.fetchone()
    return raw[0]

install_déchets_non_dangerchèteries = nb_install_déchets_non_danger()


def nb_pateformes_compostage():
    sql = "SELECT  COUNT(*) FROM consultations.poi WHERE nom_couche  = 'Plateformes de compostage'"
    cur.execute(sql)
    raw = cur.fetchone()
    return raw[0]

pateformes_compostage = nb_pateformes_compostage()


def nb_recycleries():
    sql = "SELECT  COUNT(*) FROM consultations.poi WHERE nom_couche  = 'Recycleries'"
    cur.execute(sql)
    raw = cur.fetchone()
    return raw[0]

recycleries = nb_recycleries()


def nb_unité_valorisation():
    sql = "SELECT  COUNT(*) FROM consultations.poi WHERE nom_couche  = 'Unités de valorisation énergétique des déchets'"
    cur.execute(sql)
    raw = cur.fetchone()
    return raw[0]

unité_valorisation = nb_unité_valorisation()


def nb_réseaux_chaleur():
    sql = "SELECT  COUNT(*) FROM consultations.poi WHERE nom_couche  = 'Réseaux de chaleur'"
    cur.execute(sql)
    raw = cur.fetchone()
    return raw[0]

réseaux_chaleur = nb_réseaux_chaleur()


def nb_install_géoth():
    sql = "SELECT  COUNT(*) FROM consultations.poi WHERE nom_couche  = 'Installations géothermiques'"
    cur.execute(sql)
    raw = cur.fetchone()
    return raw[0]

install_géoth = nb_install_géoth()


def nb_unités_méthanisation():
    sql = "SELECT  COUNT(*) FROM consultations.poi WHERE nom_couche  = 'Unités de méthanisation'"
    cur.execute(sql)
    raw = cur.fetchone()
    return raw[0]

unités_méthanisation = nb_unités_méthanisation()


plt.figure(figsize = (8, 8))
x = [bornes_elec, infrastructures, install_bio, centres_tri, déchèteries, install_déchets_non_dangerchèteries, pateformes_compostage, recycleries, unité_valorisation, réseaux_chaleur, install_géoth, unités_méthanisation]
plt.pie(x, labels = ['Bornes de recharge de véhicules électriques', 'Bornes hydrogène', 'Installations GnV/bio-GnV', 'Centres de tri', 'Déchèteries', 'Installations de stockage des déchets non dangereux', 'Plateformes de compostage', 'Recycleries', 'Unités de valorisation énergétique des déchets', 'Réseaux de chaleur', 'Installations géothermiques', 'Unités de méthanisation'], normalize = True)
plt.legend()
plt.show()