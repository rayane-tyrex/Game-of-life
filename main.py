import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import motif
import time


def voisin(tab, i, j):
    rows , column = tab.shape
    S = 0

    for di in (-1, 0, 1):
        for dj in (-1,0,1):
            if di == 0 and dj == 0:
                continue

            else:
                ni = (i+di) % rows
                nj = (j+dj) % column

            S += tab[ni, nj]

    return S
print("Motifs diponibles")
for m in motif.liste_motifs():
    print("--", m, "--")


def main_pg(taille, motif_choisi ):

    grille = motif.grille_vide(taille)
    m = motif.motifs(motif_choisi, taille)
    x = taille//2 - m.shape[0]//2
    y = taille//2 - m.shape[1]//2
    
    tab = motif.placer(grille, motif_choisi, x, y, taille)



    original_tab = tab.copy()

    plt.ion()

    cp = 0
    population = []
  

    couleur = ListedColormap(['black', 'white'])

    fig, axes = plt.subplots(1,3, figsize=(18,9))

    img0 = axes[0].imshow(original_tab, cmap=ListedColormap(['blue','white']), vmin=0, vmax=1)
    axes[0].set_title(f"Population initiale: {np.sum(grille)}")

    img1 = axes[1].imshow(tab, cmap=couleur, vmin=0, vmax=1, interpolation='nearest')
    title1 = axes[1].set_title("generation 0")

    

   
    while plt.fignum_exists(fig.number):
        tableau = tab
        nouvelle = tab.copy()
        
        for i in range(taille):
            for j in range(taille):
                nbr_voisin_vivant = voisin(tab, i, j)
                if nouvelle[i,j] == 1:
                    if nbr_voisin_vivant < 2 or nbr_voisin_vivant > 3:
                        nouvelle[i,j] = 0

                    else:
                        nouvelle[i,j] = 1

                else:
                    if nbr_voisin_vivant == 3:
                        nouvelle[i,j] = 1

        if np.array_equal(tableau, nouvelle):
            nbr_cellule = np.sum(tableau)
            title1.set_text(f"Simulation terminé \n Generation {cp} \n Population {nbr_cellule}")
    

        else:
            nbr_cellule = np.sum(nouvelle)
            cp +=1
            tab = nouvelle
            population.append(nbr_cellule)
            
            img1.set_data(tab)
            title1.set_text(f"Simulation en cours \n Generation {cp} \n Population {nbr_cellule}")
            img2 = axes[2].plot(population)
            title2 = axes[2].set_title("Evolution de la population au fil des generation")
            plt.xlabel("nbr de generation")
            plt.ylabel("Population")
            
            
            
            plt.pause(0.5)
    

main_pg(taille=int(input("Entrez la taille: ")), motif_choisi= input("choix du motif: "))