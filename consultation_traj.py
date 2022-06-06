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

## AFFCIHAGE DE LA PROPORTION DE CONSULTATIONS PASSANT PAR LA PAGE SUIVI TRAJECTOIRE
def nb_consultations_traj():
    sql= "SELECT COUNT(*) FROM consultations.analyses_territoriales WHERE page='suivi_trajectoire'"
    cur.execute(sql)
    # Fetch data line by line
    raw = cur.fetchone()
    return raw[0]


def nb_consultations():
    sql= "SELECT COUNT(*) FROM consultations.analyses_territoriales "
    cur.execute(sql)
    # Fetch data line by line
    raw = cur.fetchone()
    return raw[0]

nb_consultations1= nb_consultations()
nb_consultations_traj1=nb_consultations_traj()

print(f'Il y a eu {nb_consultations1} consulations en tout dont {nb_consultations_traj1} par la page de suivi de trajectoire')

## AFFCIHAGE DE LA PROPORTION DE CONSULTATIONS PASSANT PAR LA PAGE SUIVI TRAJECTOIRE EN FONCTION DE LA DATE (il suffit de rajouter une condition dans la commande sql du code d'Inès)


conn.close()