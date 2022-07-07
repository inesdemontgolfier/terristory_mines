# ce document est destiné à tester les fonctionnalités implémentées sur les équipements


# on importe les fonctions utiles que l'on va tester
from equipements_v2 import consultations_equipements, consultations_themes_equipements


#Représente la proportion des consultations de chaque catégorie d'équipement dans la région auvergne-rhone-alpes
consultations_themes_equipements(regions=['auvergne-rhone-alpes'])

#Représente la proportion des consultations de chaque équipement dans la région auvergne-rhone-alpes
consultations_equipements(regions=['auvergne-rhone-alpes'])

#Représente la proportion des consultations de chaque catégorie d'équipement dans toutes les régions répertoriées dans Terristory
consultations_themes_equipements()

#Représente la proportion des consultations de chaque équipement dans toutes les régions répertoriées dans Terristory
consultations_equipements()