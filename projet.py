import random
def jeu_chiffre():
    chiffre_secret = random.randint(1, 10)
    tentative=3
    print("bienvenue!veuillez saisir un chiffre de votre choix")
    for tentative in range (tentative):
        try:
            choix_utilisateur= int(input ("f tentative {tentative +1}/{tentative} saisissez un chiffre: "))
        except ValueError:
            print("saisir un chiffre")
            continue
        if choix_utilisateur==chiffre_secret :
            print("bravo! vous aviez trouver")
            break
        elif choix_utilisateur < chiffre_secret:
            print("ce chiffre est inférieur au chiffre secret")
        else:
            print("ce chiffre est supérieur au chiffre secret")
        if tentative== tentative-1:
             print(f"Désolé, vous avez utilisé toutes vos tentatives. Le chiffre secret était:{chiffre_secret}.") 
jeu_chiffre()





