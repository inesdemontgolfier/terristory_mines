#!/usr/bin/python3
# http://initd.org/psycopg/docs/usage.html
#from this import d
#from turtle import shape
from typing_extensions import dataclass_transform
import psycopg2
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

from irrégularités import correction_themes, correction_noms

HOST = "localhost"
USER = "postgres"
PASSWORD = "postgres"
DATABASE = "postgres"
# Open connection
conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
# Open a cursor to send SQL commands
cur = conn.cursor()

sql = """SELECT consultations.consultations_indicateurs.id_indicateur,
meta.indicateur.nom,
meta.indicateur.ui_theme,
consultations.consultations_indicateurs.date,
consultations.consultations_indicateurs.region,
consultations.consultations_indicateurs.provenance
FROM consultations.consultations_indicateurs
LEFT JOIN meta.indicateur ON consultations.consultations_indicateurs.id_indicateur = meta.indicateur.id;"""
cur.execute(sql)
raw = cur.fetchall()


sql1="SELECT * FROM consultations.consultations_indicateurs WHERE consultations.consultations_indicateurs.provenance NOT LIKE 'tableaux_de_bord'"
cur.execute(sql1)
raw1 = cur.fetchall()

conn.close()

df = pd.DataFrame(raw, columns=["id_indicateur", "nom", "ui_theme", "date", "region", "provenance"])

df = correction_themes(df)
df = correction_noms(df)

print(df)


def fréquences_indic_majoritaires(data, p, regions, titre_fichier="figures/titre_par_defaut.png"):
    """Renvoie les indicateurs consultés à plus de 100*p pourcents.
    Crée une catégorie "autres" pour ceux dont la fréquence de consultation est inférieure à p.
    Plote les données.
    """

    fréquences = [0]
    légende = ['Autres']
  
    for indicateur, fréquence in data.items():
        if fréquence < p:
            fréquences[0] += fréquence
        else:
            fréquences.append(fréquence)
            légende.append(indicateur)
    
    plt.pie(fréquences, labels=légende, autopct='%.1f%%')
    plt.savefig(titre_fichier)
    plt.show()
    

    return [légende, fréquences]

def consultations_indicateurs(p=0.02, themes=df.ui_theme.unique(), regions=df.region.unique(), provenances=df.provenance.unique()):
    """Retourne et affiche le camembert des fréquences de consultation des indicateurs.
    Choix possible des thèmes, des régions et des provenances.
    """

    data = df[df["ui_theme"].isin(themes) & df["region"].isin(regions)& df["provenance"].isin(provenances)]
    data_freq = dict(data["nom"].value_counts(normalize=True))
    
    return fréquences_indic_majoritaires(data_freq, p, regions)

def consultations_themes(p=0.01, regions=df.region.unique(), provenances=df.provenance.unique()):
    """Retourne et affiche le camembert des fréquences de consultation des indicateurs, groupés par thème.
    Choix possible des régions et des provenances.
    """

    data = df[df["region"].isin(regions)& df["provenance"].isin(provenances)]
    data_freq = dict(data["ui_theme"].value_counts(normalize=True))
    
    return fréquences_indic_majoritaires(data_freq, p, regions, titre_fichier="figures/consultations_indicateurs.png")

consultations_themes(regions=['nouvelle-aquitaine'])

## si on veut exclure la provenance tableaux de bord car elle biaise les proportions
liste=[]
for i in range(df.shape[0]):
    if df.provenance[i]!="tableaux_de_bord":
        liste.append(i)


df_new=df.drop(liste)

print(df.shape)
print(df_new.shape)

def consultations_themes_sans_tbd(p=0.01, regions=df_new.region.unique(), provenances=df_new.provenance.unique()):
    """Retourne et affiche le camembert des fréquences de consultation des indicateurs, groupés par thème.
    Choix possible des régions et des provenances.
    """

    data = df_new[df_new["region"].isin(regions)& df_new["provenance"].isin(provenances)]
    data_freq = dict(data["ui_theme"].value_counts(normalize=True))
    
    return fréquences_indic_majoritaires(data_freq, p, regions, titre_fichier="figures/consultations_indicateurs_sans_tbd.png")


consultations_themes_sans_tbd(regions=['nouvelle-aquitaine'])
