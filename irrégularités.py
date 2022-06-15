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
        #print(df[df["ui_theme"] == ancien])
        df[df["ui_theme"] == ancien] = nouveau
        #print(df["ui_theme" == ancien])
    
    return df

def correction_noms(df):
    """Uniformise les noms des indicateurs entre les régions, pour permettre une lisibilité nationale des données.
    """

    indicateurs = {
    }

    for ancien, nouveau in indicateurs.items():
        df["nom" == ancien] = nouveau
    
    return df