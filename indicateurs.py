# ZTTENTION CODE OBSOLETE, VOIR A LA FIN.

#!/usr/bin/python3
# http://initd.org/psycopg/docs/usage.html
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
    """
    Récupère dans la base de données les informations nécessaires pour construire un dictionnaire, avec pour clef l'id des indicateurs et pour valeur, le nom.
    """
    conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
    cur = conn.cursor()
    
    sql = "SELECT id, nom FROM meta.indicateur;"
    cur.execute(sql)
    noms = dict(cur.fetchall())
    conn.close()
    return noms

def fréquences_indic(noms=None):
    """
    Récupère les fréquences des indicateurs consultés.7
    Légende les indicateurs à partir de leur id, si on fournit à la fonction le dictionnaire `noms` (qui peut être obtenu classiquement avec `noms_indicateurs`).
    """
    conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
    cur = conn.cursor()
    
    sql = """SELECT consultations_indicateurs.id_indicateur, COUNT(*)/CAST((SELECT COUNT(*) FROM consultations.consultations_indicateurs) AS DECIMAL(7,2))
    FROM consultations.consultations_indicateurs
    GROUP BY consultations_indicateurs.id_indicateur;"""
    cur.execute(sql)
    data = dict(cur.fetchall()) # Dictionnaire des fréquences
    conn.close()
        
    #Légendage des indicateurs
    if noms != None:
        data_lengendée = {'inconnu': 0.}
        for indicateur, fréquence in data.items():
            if indicateur in noms:
                data_lengendée[noms[indicateur]] = float(fréquence)
            else:
                data_lengendée['inconnu'] += float(fréquence)
                # Certains indicateurs ne sont pas suivis dans la table meta.indicateur. On les nomme donc 'inconnu'.
        return data_lengendée
    return data

def fréquences_indic_majoritaires(data, p):
    """Renvoie les indicateurs consultés à plus de 100*p pourcents.
    Crée une catégorie "autres" pour ceux dont la fréquence de consultation est inférieure à p.
    Plote les données.
    Enregistre la figure pour un éventuel export pdf.
    """
    fréquences = [0.]
    légende = ['autres']  
    for indicateur, fréquence in data.items():
        if fréquence < p:
            fréquences[0] += fréquence
        else:
            fréquences.append(fréquence)
            légende.append(indicateur)

    plt.title(f"Consultations des indicateurs (pour une fréquence supérieure à {p})")
    plt.pie(fréquences, labels=légende, labeldistance=1., rotatelabels=True, radius=0.5, textprops={'fontsize': 5})
    plt.savefig(f"figures/consultation_indicateurs_v0_p_{p}.png", dpi=400.)
    plt.show()
    return [légende, fréquences]

fréquences_indic_majoritaires(fréquences_indic(noms_indicateurs()), 0.01)

# Attention, il y a ici un très gros biais : deux indicateur identiques mais dans 2 régions différentes n'ont pas le même identifiant. Ils seront représentés par 2 secteurs différents dans le camembert.
# Ici, c'est vraiment un camembert de base, où on ne regroupe pas ensemble les indicateurs identiques de plusieurs régions différentes.
# Aucune analyse au niveau national ne peut être tirée
# Cela explique la très grosse proportion de "Autres"
# Problème résolu dans la v2, où on sommera sur les noms, non pas sur les id.