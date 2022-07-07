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