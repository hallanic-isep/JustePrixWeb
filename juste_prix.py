import random


def verif(essai,cible):
    if essai < 1 or essai > 10:
        print("Erreur, il faut saisir une valeur entre 1 et 10...")
        return "continuer"

    if cible == essai:
        print("Bravo !!!")
        return "bravo"
    elif cible < essai:
        print("Trop élevé...")
    else:
        print("Trop peu")
    return "continuer"


def juste_prix():
    print("Trouver le prix de l'objet X..")
    cible = random.randint(1,10)
    #print(f"cible={cible}")

    for i in range(5):

        # Récupération de la proposition du joueur
        try:
            nv_essai = int(input("Votre proposition entre 1 et 10 : "))
        except ValueError:
            print("Erreur: Il faut saisir un entier...")
            continue

        if verif(nv_essai,cible) == "bravo":
            break

    print("Fin du jeu...")

if __name__ == "__main__":
    juste_prix()