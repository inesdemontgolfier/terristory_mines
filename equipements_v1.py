# ce fichier contient une ancienne version de réccupération de données grâce à des requêtes SQL
# ceci est un exemple de code non optimisé pour voir l'évolution de notre code
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


# Représentation des catégories d'équipement sous la forme d'un diagramme circulaire en fonction de la fréquence d'appel de la catégorie

def nb_carburants():
    sql = "SELECT  COUNT(*) FROM consultations.poi WHERE nom_couche  IN ('Bornes de recharge de véhicules électriques', 'Bornes hydrogène', 'Installations GnV/bio-GnV')"
    cur.execute(sql)
    raw = cur.fetchone()
    return raw[0]

carburants = nb_carburants()
print(carburants)


def nb_infrastructures():
    sql = "SELECT  COUNT(*) FROM consultations.poi WHERE nom_couche  = 'Réseaux de chaleur'"
    cur.execute(sql)
    raw = cur.fetchone()
    return raw[0]

infrastructures = nb_infrastructures()
print(infrastructures)


def nb_installationsEnr():
    sql = "SELECT  COUNT(*) FROM consultations.poi WHERE nom_couche  IN ('Installations géothermiques', 'Unités de méthanisation')"
    cur.execute(sql)
    raw = cur.fetchone()
    return raw[0]

installationsEnr = nb_installationsEnr()
print(installationsEnr)


def nb_déchets():
    sql = "SELECT  COUNT(*) FROM consultations.poi WHERE nom_couche  IN ('Centres de tri', 'Déchèteries', 'Installations de stockage des déchets non dangereux', 'Plateformes de compostage', 'Recycleries', 'Unités de valorisation énergétique des déchets')"
    cur.execute(sql)
    raw = cur.fetchone()
    return raw[0]

déchets = nb_déchets()
print(déchets)


# affichage
plt.figure(figsize = (8, 8))
x = [carburants, infrastructures, installationsEnr, déchets]
plt.pie(x, labels = ['Carburants', 'Infrastructures', 'InstallationsEnr', 'Déchets'], normalize = True)
plt.legend()
plt.show()



# Représentation de chaque équipement sous la forme d'un diagramme circulaire en fonction de la fréquence d'appel de l'équipement

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

# affichage
plt.figure(figsize = (8, 8))
x = [bornes_elec, infrastructures, install_bio, centres_tri, déchèteries, install_déchets_non_dangerchèteries, pateformes_compostage, recycleries, unité_valorisation, réseaux_chaleur, install_géoth, unités_méthanisation]
plt.pie(x, labels = ['Bornes de recharge de véhicules électriques', 'Bornes hydrogène', 'Installations GnV/bio-GnV', 'Centres de tri', 'Déchèteries', 'Installations de stockage des déchets non dangereux', 'Plateformes de compostage', 'Recycleries', 'Unités de valorisation énergétique des déchets', 'Réseaux de chaleur', 'Installations géothermiques', 'Unités de méthanisation'], normalize = True)
plt.legend()
plt.show()