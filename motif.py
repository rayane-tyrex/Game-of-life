import numpy as np

# =========================
# Dictionnaire des motifs
# =========================

MOTIFS = {

    "special": np.array([
                [1,1,1,1,1,1,1,1,1],
                [1,0,0,0,0,0,0,0,1],
                [1,0,1,1,1,1,1,0,1],
                [1,0,1,0,0,0,1,0,1],
                [1,0,1,0,1,0,1,0,1],
                [1,0,1,0,0,0,1,0,1],
                [1,0,1,1,1,1,1,0,1],
                [1,0,0,0,0,0,0,0,1],
                [1,1,1,1,1,1,1,1,1]
            ]),


    # -------- Oscillateurs --------
    "blinker": np.array([
        [1, 1, 1]
    ]),

    "toad": np.array([
        [0, 1, 1, 1],
        [1, 1, 1, 0]
    ]),

    "beacon": np.array([
        [1, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 1],
        [0, 0, 1, 1]
    ]),

    # -------- Mobiles --------
    "glider": np.array([
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1]
    ]),

    "lwss": np.array([
        [0,1,1,1,1],
        [1,0,0,0,1],
        [0,0,0,0,1],
        [1,0,0,1,0]
    ]),
}


# =========================
# Fonctions utilitaires
# =========================

def liste_motifs():
    """Retourne la liste des noms disponibles"""
    return list(MOTIFS.keys())


def motifs(nom, taille):
    """Retourne une copie du motif demandé"""
    if nom not in MOTIFS:
        grille = np.zeros((taille , taille))
        nbr_1 = (taille*taille)//5
        positions = np.random.choice(taille*taille, nbr_1, replace=False)
        lignes, colonnes = np.unravel_index(positions, (taille, taille))
        grille[lignes, colonnes] = 1
        
    else:
        return MOTIFS[nom].copy()
        
    return grille



def grille_vide(taille):
    return np.zeros((taille, taille), dtype=int)


def placer(grille, nom_motif, x, y, taille):
    """Place un motif dans la grille"""
    m = motifs(nom_motif, taille)
    h, w = m.shape
    grille[x:x+h, y:y+w] = m
    return grille

