#!/usr/bin/python3
# http://initd.org/psycopg/docs/usage.html
from this import d
from typing_extensions import dataclass_transform
import psycopg2
from matplotlib import pyplot as plt
import numpy as np
HOST = "localhost"
USER = "postgres"
PASSWORD = "postgres"
DATABASE = "postgres"
# Open connection
conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
# Open a cursor to send SQL commands
cur = conn.cursor()

def noms_indicateurs():
    conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
    cur = conn.cursor()
    
    sql = "SELECT id, nom FROM meta.indicateur"
    cur.execute(sql)
    noms = dict(cur.fetchall())
    conn.close()
    return noms

def fréquences_indic(noms=None):
    conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
    cur = conn.cursor()
    
    sql = "SELECT consultations_indicateurs.id_indicateur, COUNT(*) FROM consultations.consultations_indicateurs GROUP BY consultations_indicateurs.id_indicateur;"
    cur.execute(sql)
    data = dict(cur.fetchall())
    conn.close()

    #Normalisation
    nb_consultations = sum(consultation for indicateur, consultation in data.items())
    for indicateur, consultation in data.items():
        data[indicateur] = consultation/nb_consultations
        
    #Légendage des indicateurs
    if noms != None:
        data_lengendée = {'inconnu': 0.}
        for indicateur, fréquence in data.items():
            if indicateur in noms:
                data_lengendée[noms[indicateur]] = fréquence
            else:
                data_lengendée['inconnu'] += fréquence
            """
            try:
                indicateur = noms[indicateur]
            except:
                print(f"L'indicateur {indicateur} n'est pas légendé.")
                indicateur = "Inconnu"
            break"""
        return data_lengendée
    return data

def fréquences_indic_majoritaires(data, p):
    """Renvoie les indicateurs consultés à plus de 100*p pourcents.
    Crée une catégorie "autres" pour ceux dont la fréquence de consultation est inférieure à p.
    Plote les données.
    """
    print(data)
    fréquences = [0]
    légende = ['autres']  
    for indicateur, fréquence in data.items():
        if fréquence < p:
            fréquences[0] += fréquence
        else:
            fréquences.append(fréquence)
            légende.append(indicateur)

    plt.title(f"Consultations des indicateurs (pour une fréquence supérieure à {p})")
    plt.pie(fréquences, labels=légende, labeldistance=1., rotatelabels=True)
    plt.show()

    return [légende, fréquences]

fréquences_indic_majoritaires(fréquences_indic(noms_indicateurs()), 0.05)

# Attention, y'a un très gros biais : deux indicateur identiques mais dans 2 régions différentes n'ont pas le même identifiant.
# Ici, c'est vraiment un camembert de base, où on ne regroupe pas ensemble les indicateurs identiques de plusieurs régions différentes.
# Problème résolu dans la v2, où on sommera sur les noms, non pas sur les id.