#!/usr/lib/python
from fpdf import FPDF
monPdf = FPDF()
monPdf.add_page()
monPdf.set_font("Arial", size=10)
monPdf.cell(200, 10, txt="Bonjour les visiteurs", ln=1, align="C")
monPdf.image('index.jpeg')
monPdf.output("mon_fichier.pdf")

from equipements_v2 import consultations_equipements, consultations_themes_equipements
from suivi_actions import connexions_mois, connexions
consultations_themes_equipements(regions=['auvergne-rhone-alpes'], titre_figure = "figures/consultation_equipements_themes_region")
consultations_equipements(regions=['auvergne-rhone-alpes'], titre_figure = "figures/consultation_equipements_region")
consultations_themes_equipements(titre_figure = "figures/consultation_equipements_themes")
consultations_equipements(titre_figure = "figures/consultation_equipements")
connexions()
connexions_mois(analyses_territoriales,'historique des consultations pour la page analyses territorailes')