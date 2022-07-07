#!/usr/bin/python3
# http://initd.org/psycopg/docs/usage.html
#from this import d
from typing_extensions import dataclass_transform
import psycopg2
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from datetime import timedelta

from irregularites import correction_themes, correction_noms

HOST = "localhost"
USER = "postgres"
PASSWORD = "postgres"
DATABASE = "postgres"
# Open connection
conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
# Open a cursor to send SQL commands
cur = conn.cursor()

sql = """SELECT id_indicateur, date, id_utilisateur, provenance
FROM consultations.consultations_indicateurs
ORDER BY date ASC;
"""
cur.execute(sql)
raw = cur.fetchall()
conn.close()

df = pd.DataFrame(raw, columns=["id_indicateur", "date", "id_utilisateur","provenance"])

temps_consultations = []


t0 = df["date"][0]
print(t0)
temps_unique = []

for i in df.index:
    durée = (df["date"][i] - t0).total_seconds()
    if durée > 300:
        nouvelle_consultation = True
    else:
        temps_unique.append(durée)

    try :
        nouvelle_consultation = (df["id_utilisateur"][i] != df["id_utilisateur"][i + 1] or df["id_indicateur"][i] != df["id_indicateur"][i+1])
    except:
        nouvelle_consultation = False
    if nouvelle_consultation:
        if len(temps_unique) > 10:
            temps_consultations.append(temps_unique)
        temps_unique = []
        t0 = df["date"][i + 1]


h=0
for consultation in temps_consultations:
    h += 1
    plt.scatter(consultation, [h]*len(consultation), marker='+')
plt.xlabel("Temps à partir du premier enregistrement (s)")
plt.ylabel("Requêtes différentes")
plt.yticks(ticks=[], labels=[])
plt.title('Enregistrements des consultations (utilisateur, indicateur unique, à moins de 5 minutes)')
plt.show()


moustache = [len(consultation) for consultation in temps_consultations]
plt.boxplot(moustache)
plt.show()