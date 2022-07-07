# A détecter : indicateurs noms documentés, noms d'indicateurs proches mais pas identiques selon les régions, idem pour les thèmes.

def correction_themes(df):
    """Uniformise les noms des thèmes des indicateurs entre les régions, pour permettre une lisibilité nationale des données.
    """


    themes = {
        "Émissions de gaz à effet de serre": "Émissions de GES",
        "Logement résidentiel": "Logement",
        "Pontentiel ENR": "Potentiels ENR",
        "Socio-économie": "Économie et société",
        "Dépense énergétique" : "Facture énergétique",
        'Émissions GES': "Émissions de GES"
    }

    for ancien, nouveau in themes.items():
        #df[df["ui_theme"] == ancien]["ui_theme"] = nouveau
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
        "Émissions GES": "Émissions de GES",
        "Dépense énergétique": "Facture énergétique",
        "Émissions de GES du secteur tertiaire par salarié": "Émissions GES tertiaire / employé",
        "Émissions de GES par habitant": "Émissions GES / hab",
        "Émissions de GES du résidentiel par habitant": "Émissions GES résidentiel / hab",
        "Emissions de gaz à effet de serre": "Émissions de GES",
        "Emissions de GES": "Émissions de GES",
        "GES": "Émissions de GES",
    }

    for ancien, nouveau in indicateurs.items():
        #df[df["nom"] == ancien] = nouveau
        df.loc[df.nom == ancien, "nom"] = nouveau
    
    return df