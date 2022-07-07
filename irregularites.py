def correction_dates(df, type_de_donnée):
    df["masque"]=np.nan
    id = df.iloc[0, df.columns.get_loc("id_utilisateur")]
    ind = df.iloc[0, df.columns.get_loc(type_de_donnée)]
    date = df.iloc[0, df.columns.get_loc("date")]
    for i in df.index :
        if df.iloc[i, df.columns.get_loc("id_utilisateur")]!= id and df.iloc[i, df.columns.get_loc(type_de_donnée)]!= ind :
            ind = df.iloc[i, df.columns.get_loc(type_de_donnée)]
            id = df.iloc[i, df.columns.get_loc("id_utilisateur")]
            date = df.iloc[i, df.columns.get_loc("date")]
            df.iloc[i, df.columns.get_loc("masque")] = True
        else :
            delta_temps = -(date - df.iloc[i, df.columns.get_loc("date")]).total_seconds()
            if delta_temps > 300 :
                df.iloc[i, df.columns.get_loc("masque")] = True
                ind = df.iloc[i, df.columns.get_loc(type_de_donnée)]
                id = df.iloc[i, df.columns.get_loc("id_utilisateur")]
                date = df.iloc[i, df.columns.get_loc("date")]
            else :
                df.iloc[i, df.columns.get_loc("masque")] = False
    return df[df.masque==True]

# Première partie : irrégularités sur les indicateurs

# A détecter : indicateurs noms documentés, noms d'indicateurs proches mais pas identiques selon les régions, idem pour les thèmes.

def correction_themes(df):
    """Uniformise les noms des thèmes des indicateurs entre les régions, pour permettre une lisibilité nationale des données.
    """


    themes = {
        "Émissions de gaz à effet de serre": "Émissions de GES",
        "Logement résidentiel": "Logement",
        "Pontentiel ENR": "Potentiels ENR",
        "Socio-économie": "Économie et société",
        "Dépense énergétique" : "Facture énergétique"
    }

    for ancien, nouveau in themes.items():
        
        df.loc[df.ui_theme == ancien, "ui_theme"] = nouveau
        
        
    
    return df

def correction_noms(df):
    """Uniformise les noms des indicateurs entre les régions, pour permettre une lisibilité nationale des données.
    """

    indicateurs = {
        "Part Enr/Consommation d'énergie": "Part Enr / Consommation d'énergie",
        "Taux de pauvreté 2015": "Taux de pauvreté",
        "Part de ménages en précarité énergétique logement": "Taux de précarité énergétique",
        "Médiane du niveau de vie par epci 2016": "Médiane du niveau de vie",
        "Dépense énergétique du tertiaire par salarié": "Facture énergétique tertiaire / employé",
        "Dépense énergétique par habitant": "Facture énergétique / hab",
        "Dépense énergétique du résidentiel par habitant": "Facture énergétique résidentiel / hab",
        "Production d'énergie renouvelable (2016)": "Prodution ENR",
        "Émissions de GES": "Émissions GES",
        "Dépense énergétique": "Facture énergétique",
        "Émissions de GES du secteur tertiaire par salarié": "Émissions GES tertiaire / employé",
        "Émissions de GES par habitant": "Émissions GES / hab",
        "Émissions de GES du résidentiel par habitant": "Émissions GES résidentiel / hab",
        "Emissions de gaz à effet de serre": "Émissions GES",
        "Emissions de GES": "Émissions GES",
        "GES": "Émissions GES",
    }

    for ancien, nouveau in indicateurs.items():
        df.loc[df.nom == ancien, "nom"] = nouveau
    
    return df





# Deuxième partie : irrégularités sur les équipements

# A détecter : équipements noms documentés, noms d'équipements proches mais pas identiques selon les régions, création de thèmes.

import numpy as np

def correction_noms_equipements(df):
    """Uniformise les noms des équipements entre les régions, pour permettre une lisibilité nationale des données.
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