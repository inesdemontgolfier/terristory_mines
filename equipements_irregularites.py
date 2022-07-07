# A détecter : équipements noms documentés, noms d'équipements proches mais pas identiques selon les régions, création de thèmes.
import numpy as np

def correction_noms_equipements(df):
    """Uniformise les noms des indicateurs entre les régions, pour permettre une lisibilité nationale des données.
    """

    equipements = {"Installations GnV": "Installations GnV et bio-GnV",
        "Unité de compostage": "Unités de compostage",
        "Ressourceries" : "Recycleries",
        "Centrales éoliennes" : "Installations et parcs éoliens terrestres",
        "Parcs éoliens terrestres" : "Installations et parcs éoliens terrestres",
        "Installations hydroélectrique" : "Installations hydroélectriques",
        "Centrales hydroliques" : "Installations hydroélectriques",
        "Centrales photovoltaïques" : "Installations solaires photovoltaïques",
        "Unités de méthanisation" : "Installations de méthanisation",
        "Installation de méthanisation" : "Installations de méthanisation"
        }

    for ancien, nouveau in equipements.items():
        df.loc[df.nom_couche == ancien, "nom_couche"] = nouveau
        #df["nom_couche" == ancien] = nouveau
    
    return df





Carburants_alternatifs = ["Bornes de recharge de véhicules électriques", "Bornes hydrogène", "Installations GnV et bio-GnV"]
Déchets = ["Centres de tri", "Déchèteries", "Installation de stockage de déchets non dangereux", "Unités de compostage", "Recycleries", "Unités de valorisation énergétique des déchets"]
Infrastructures = ["Réseaux de chaleur"]
Installations = ["Bornes hydrogène", "Géothermie"]
Installations_EnR = ["Chaufferies", "Unité d’incinération des ordures ménagères", "Installations et parcs éoliens terrestres", "Installations hydroélectriques", "Installations solaires photovoltaïques", "Unités de cogénération", "Installations de méthanisation"]

def themes_equipements(df):
    """Création d'une colonne de thèmes ou de catégories d'équipements.
    """

    df["theme"] = np.nan
    for elt in Carburants_alternatifs:
        df.loc[df.nom_couche == elt, "theme"] = "Carburants_alternatifs"
    for elt in Déchets:
        df.loc[df.nom_couche == elt, "theme"] = "Déchets"
    for elt in Infrastructures:
        df.loc[df.nom_couche == elt, "theme"] = "Infrastructures"
    for elt in Installations:
        df.loc[df.nom_couche == elt, "theme"] = "Installations"
    for elt in Installations_EnR:
        df.loc[df.nom_couche == elt, "theme"] = "Installations_EnR"
    return(df)