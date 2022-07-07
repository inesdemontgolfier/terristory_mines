## terristory_mines
La mission nous a été donnée par l'agence Auverge Rhones-Alpes de Terristory. Terristory est une application web qui permet aux collectivités locales de consulter différentes données afin d'entamer la transition énergétique de leur territoire

# Mission initialement prévue
Nous étions censée avoir un regard critique sur le code d'analyse d'audience déja mis en place par l'équipe Terristory Auverge Rhones-Alpes. 
Nous avons d'abord commencé par comprendre les finalités de l'application web et nous avons ensuite installé une machine virtuelle sur chacun de nos ordinateurs afin de pouvoir coder. L'équipe nous a alors demander de lire le code et d'y proposer des améliorations.
Seulement, n'ayant jamais touché à l'analyse d'audience, nous nous sommes retrouvés un peu perdu et n'avions aucun regard critique car aucun élément de comparaison. 
Nous avons donc décidé, conjointement avec Paul Roux, de nous occuper de traiter les données des utilisateurs qui consultent le site, qui sont récupérées mais pas traitées. 
Nous avons ainsi réparti le travail comme suit:
    Inès : données relatives à la consultation globale du site 
    Phil : indicateurs
    Manuela : équipements
    Cléa : consultation des pages trajectoires

# Répartition des fichiers
Chaque fichier a été codé par quelqu'un de différent

Inès:
Le fichier suivi_actions.py réalise l'analyse d'audience relatif à la consultation globale du site (taux de rebond, consultations par mois ...)

Manuela :
Le fichier irregularites.py effectue une uniformisation des noms des différents équipements entre les régions et regroupe ces équipements par catégories grâce aux thèmes trouvés sur la version en ligne de Terristory.

Le fichier equipements_v2 permet d'afficher des diagrammes circulaires représentant la proportion de consultation de chaque équipement ou catégorie d'équipements par région ou sur les toutes les régions répertoriées.



# Court mode d'emploi des fonctions 

taux_rebond : 
- ne prend pas d'arguments
- renvoie le taux de rebond, la liste des utilisateurs n'ayant consultée qu'une page

chemin_one_rebond:
- renvoie la liste des pages consultée qu'une fois (pour tenter d'expliquer la seule consultation)

consultations_indicateurs :
- renvoie les proportions 
correction_noms_equipements :
- renvoie la dataframe avec les noms des équipements uniformisés entre les régions


consultations_equipements :
- Retourne, affiche et enregistre le diagramme circulaire des fréquences de consultation des équipemments.
    Choix possible des régions.

consultations_themes_equipements :
- Retourne, affiche et enregistre le diagramme circulaire des fréquences de consultation des équipements, groupés par thème.
    Choix possible des régions.

consultation_traj_cesba :
- Retourne 



