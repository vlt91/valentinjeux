
import random

def jeu_devinette():
    print("Bienvenue dans le jeu de devinette !")
    print("Je pense à un nombre entre 1 et 100. Essaie de deviner lequel.")

    # L'ordinateur choisit un nombre aléatoire
    nombre_secret = random.randint(1, 100)
    
    # Initialisation du nombre de tentatives
    tentatives = 0

    while True:
        # Demander à l'utilisateur de deviner un nombre
        try:
            guess = int(input("Entrez un nombre : "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue
        
        tentatives += 1

        # Comparer la réponse avec le nombre secret
        if guess < nombre_secret:
            print("Trop petit ! Essaie encore.")
        elif guess > nombre_secret:
            print("Trop grand ! Essaie encore.")
        else:
            print(f"Bravo ! Vous avez trouvé le nombre secret {nombre_secret} en {tentatives} tentatives.")
            break

# Lancer le jeu
jeu_devinette()