
def cotisation():
    try:

        jour_cotise=(input("avez vous cotiser aujourd'hui? (oui/non)")).strip().lower()
        if jour_cotise == "oui":
            som = float(input("ancienne somme:"))
            somco = float(input("Entrer la somme cotisée:"))

            somme =som+somco

            print(f"la nouvelle somme est: {somme}")
        elif jour_cotise=="non":
            som=float(input("ancienne somme"))
            print(f"votre somme reste: {som}")
        else :
            print("Erreur de saisi")
    except ValueError:
        print("Erreur : Veuillez entrer des nombres valides pour les sommes.")

cotisation()

