#!/usr/lib/python
import glob
import os
from fpdf import FPDF

## récupère le chemin courant
path=os.getcwd()

monPdf = FPDF()
monPdf.add_page()
monPdf.set_font("Arial", size=10)
monPdf.cell(200, 10, txt="Bonjour les visiteurs", ln=1, align="C")

##récupère toutes les images du dossier figure 
liste_img=glob.glob(path +'/figures/*.png')

monPdf.output("mon_fichier.pdf")
monPdf.image('index.jpeg')
monPdf.output("mon_fichier.pdf")

from equipements_v2 import consultations_equipements, consultations_themes_equipements
import suivi_actions
consultations_themes_equipements(regions=['auvergne-rhone-alpes'], titre_figure = "figures/consultation_equipements_themes_region")
consultations_equipements(regions=['auvergne-rhone-alpes'], titre_figure = "figures/consultation_equipements_region")
consultations_themes_equipements(titre_figure = "figures/consultation_equipements_themes")
consultations_equipements(titre_figure = "figures/consultation_equipements")
suivi_actions.connexions()
suivi_actions.connexions_mois(suivi_actions.analyses_territoriales,'historique des consultations pour la page analyses territorailes')
