#!/usr/bin/python3
# http://initd.org/psycopg/docs/usage.html
#from this import d
from typing_extensions import dataclass_transform
import psycopg2
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# on importe le fichier de modifications et de normalisation des données
from irregularites import correction_noms_equipements, themes_equipements

HOST = "localhost"
USER = "postgres"
PASSWORD = "postgres"
DATABASE = "postgres"
# Open connection
conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
# Open a cursor to send SQL commands
cur = conn.cursor()

sql = """SELECT consultations.poi.Id,
consultations.poi.Id_utilisateur,
consultations.poi.region,
consultations.poi.nom_couche,
consultations.poi.date
FROM consultations.poi;"""
cur.execute(sql)
raw = cur.fetchall()
conn.close()

df = pd.DataFrame(raw, columns=["Id", "Id_utilisateur", "region", "nom_couche", "date"])

df = correction_noms_equipements(df)
df = themes_equipements(df)


#Rappel des catégories
Carburants_alternatifs = ["Bornes de recharge de véhicules électriques", "Bornes hydrogène", "Installations GnV et bio-GnV"]
Déchets = ["Centres de tri", "Déchèteries", "Installation de stockage de déchets non dangereux", "Unités de compostage", "Recycleries", "Unités de valorisation énergétique des déchets"]
Infrastructures = ["Réseaux de chaleur"]
Installations = ["Bornes hydrogène", "Géothermie"]
Installations_EnR = ["Chaufferies", "Unité d’incinération des ordures ménagères", "Installations et parcs éoliens terrestres", "Installations hydroélectriques", "Installations solaires photovoltaïques", "Unités de cogénération", "Installations de méthanisation"]



def fréquences_equipements_majoritaires(data, p, regions, theme, titre_figure = "figures/titre par défaut.png"):
    """Renvoie les equipements consultés à plus de 100*p pourcents.
    Crée une catégorie "autres" pour ceux dont la fréquence de consultation est inférieure à p.
    Plote les données et enregistre le diagramme dans le dossier figures.
    """

    fréquences = [0]
    légende = ['Autres']
  
    for equipement, fréquence in data.items():
        if fréquence < p:
            fréquences[0] += fréquence
        else:
            fréquences.append(fréquence)
            légende.append(equipement)
    if theme:
        plt.title(f"""
        Consultations des thèmes d'équipements
        (région(s) : {', '.join((str(region) for region in regions))})
        """)
    else:
        plt.title(f"""
        Consultations des équipements
        (région(s) : {', '.join((str(region) for region in regions))})
        """)
    plt.pie(fréquences, labels=légende, autopct='%.1f%%')
    plt.savefig(titre_figure, bbox_inches = "tight")
    plt.show()

    return [légende, fréquences]

def consultations_equipements(p=0.02, themes=df.theme.unique(), regions=df.region.unique(), titre_figure = "figures/titre par défaut.png"):
    """Retourne et affiche le camembert des fréquences de consultation des équipemments.
    Choix possible des thèmes et des régions.
    """

    data = df[df["theme"].isin(themes) & df["region"].isin(regions)]
    data_freq = dict(data["nom_couche"].value_counts(normalize=True))
    
    return fréquences_equipements_majoritaires(data_freq, p, regions, False, titre_figure)

def consultations_themes_equipements(p=0.01, regions=df.region.unique(), titre_figure = "figures/titre par défaut.png"):
    """Retourne et affiche le camembert des fréquences de consultation des indicateurs, groupés par thème.
    Choix possible des régions.
    """

    data = df[df["region"].isin(regions)]
    data_freq = dict(data["theme"].value_counts(normalize=True))
    return fréquences_equipements_majoritaires(data_freq, p, regions, True, titre_figure)
