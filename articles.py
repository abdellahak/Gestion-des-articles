from tabulate import tabulate
import datetime

Articles = [
    {'idArt': 1, 'nom': "chemise", 'prix': 250},
    {'idArt': 2, 'nom': "robe", 'prix': 100},
    {'idArt': 3, 'nom': "cravate", 'prix': 50},
    {'idArt': 4, 'nom': "botte", 'prix': 300},
]
Clients = [
    {'idClt': 1, 'nom': "Alami", 'tel': "0639762987", 'email': "alami321@gmail.com"},
    {'idClt': 2, 'nom': "Ali", 'tel': "0634672367", 'email': "alami321@gmail.com"},
    {'idClt': 3, 'nom': "Muslih", 'tel': "0632476437", 'email': "muslih@gmail.com"},
    {'idClt': 4, 'nom': "Moosa", 'tel': "0634762387", 'email': "moosa10112001@gmail.com"},
    {'idClt': 5, 'nom': "Samir", 'tel': "0623987525", 'email': "samir1999@gmail.com"},
    {'idClt': 6, 'nom': "Asil", 'tel': "06236823763", 'email': "asil666@gmail.com"},
]

Ventes = [
    {'idVente': 1, 'idClt': 1, 'date': '13/2/2022', 'articles': [{'idArt': 1, 'quantité': 1},
                                                                 {'idArt': 2, 'quantité': 2}, ]},
    {'idVente': 2, 'idClt': 3, 'date': '13/9/2022', 'articles': [{'idArt': 4, 'quantité': 2},
                                                                 {'idArt': 3, 'quantité': 4}, ]},
    {'idVente': 3, 'idClt': 1, 'date': '20/9/2022', 'articles': [{'idArt': 1, 'quantité': 2},
                                                                 {'idArt': 1, 'quantité': 1},
                                                                 {'idArt': 4, 'quantité': 2}, ]},
]


# ============Fonction pour afficher les table============
def affiche(l):
    data = []
    temp = []
    heading = []
    for key, value in l[0].items():
        heading.append(key)
    for i in l:
        for key, value in i.items():
            temp.append(value)
        data.append(temp.copy())
        temp.clear()
    print(tabulate(data, headers=heading, tablefmt="rounded_outline"))


def menu():
    while True:
        print(" " * 70, "╭──────────────────────────╮")
        print(" " * 70, "│           MENU           │")
        print(" " * 70, "├──────────────────────────┤")
        print(" " * 70, "│       1 - Article        │")
        print(" " * 70, "│       2 - Client         │")
        print(" " * 70, "│       3 - Vente          │")
        print(" " * 70, "│       4 - Quitter        │")
        print(" " * 70, "╰──────────────────────────╯\n")
        while True:
            x = input("choisir votre choix dans le menu precendent: ")
            x = x.strip()
            if x == "1" or x == "2" or x == "3" or x == "4":
                x = int(x)
                break
            print("─" * 100)
            print("Choix invalide, tapez une chiox valide")
            print("─" * 100)
        if x == 1:
            article()
        elif x == 2:
            client()
        elif x == 3:
            vente()
        elif x == 4:
            bye()
            exit()


###########################################################ARTICLE#####################################################
def article():
    while True:
        print(" " * 70, "╭──────────────────────────╮")
        print(" " * 70, "│          ARTICLE         │")
        print(" " * 70, "├──────────────────────────┤")
        print(" " * 70, "│       1 - Lister         │")
        print(" " * 70, "│       2 - Ajouter        │")
        print(" " * 70, "│       3 - Recherche      │")
        print(" " * 70, "│       4 - Quitter        │")
        print(" " * 70, "╰──────────────────────────╯\n")
        while True:
            n = input("choisir votre choix dans le menu precendent: ")
            n = n.strip()
            if n == "1" or n == "2" or n == "3" or n == "4":
                n = int(n)
                break
            print("─" * 100)
            print("Choix invalide, tapez une chiox valide")
            print("─" * 100)
        # ============Afficher la liste des clients============
        if n == 1:
            print("ٍٍٍٍٍٍVoici la liste des clients :")
            affiche(Articles)
        # ============Ajouter un nouveau Article============
        elif n == 2:
            s = '[§@_!#$%^&*()<>?/\\|}{~^]'
            while True:
                c = 0
                nom = input("Entrez le nom d'article: ")
                for i in nom:
                    if i in s:
                        c += 1
                if c > 0:
                    print("─" * 100)
                    print("Le nom doit être composée des lettres")
                    print("─" * 100)
                elif c == 0:
                    break
            while True:
                prix = input("Entrez le prix d'article: ")
                prix = prix.strip()
                if prix.isdecimal():
                    prix = int(prix)
                    break
                print("─" * 100)
                print("Prix invalide, Entrez un prix décimal")
                print("─" * 100)
            new = {"idArt": len(Articles) + 1,
                   "nom": nom,
                   "prix": prix}
            print(new)
            Articles.append(new.copy())
            print("─" * 100)
            print("ٍٍٍٍٍٍVoici la liste des articles:")
            affiche(Articles)
            print("─" * 100)
            print("L'article a été ajouté avec succès")
            print("─" * 100)
        # ============Rechercher un article============
        elif n == 3:
            r = input("Entrez le nom d'article que vous recherchez: ")
            j = 0
            for i in Articles:
                if r.lower() in i['nom'].lower():
                    print("─" * 100)
                    for key, value in i.items():
                        print(f"== {key}{(12 - len(key)) * " "}:  {value}")
                    print("─" * 100)
                    j += 1
            if j == 0:
                print("─" * 100)
                print("Aucun article avec ce nom")
                print("─" * 100)
        elif n == 4:
            break


###########################################################ARTICLE#####################################################

def client():
    while True:
        print(" " * 70, "╭──────────────────────────╮")
        print(" " * 70, "│          CLIENT          │")
        print(" " * 70, "├──────────────────────────┤")
        print(" " * 70, "│       1 - Lister         │")
        print(" " * 70, "│       2 - Ajouter        │")
        print(" " * 70, "│       3 - Recherche      │")
        print(" " * 70, "│       4 - Quitter        │")
        print(" " * 70, "╰──────────────────────────╯\n")
        while True:
            n = input("choisir votre choix dans le menu precendent: ")
            n = n.strip()
            if n == "1" or n == "2" or n == "3" or n == "4":
                n = int(n)
                break
            print("─" * 100)
            print("Choix invalide, tapez une chiox valide")
            print("─" * 100)
        # ============Afficher la liste des clients============
        if n == 1:
            print("ٍٍٍٍٍٍVoici la liste des clients :")
            affiche(Clients)
        # ============Ajouter un nouveau Client============
        elif n == 2:
            s = '[§@_!#$%^&*()<>?/\\|}{~^]1234567890-°+='
            while True:
                c = 0
                nom = input("Entrez le nom de client: ")
                for i in nom:
                    if i in s:
                        c += 1
                if c > 0 or len(nom) < 2:
                    print("─" * 100)
                    print("nom invalide, Entrez un nom correct")
                    print("─" * 100)
                elif c == 0 and len(nom) > 1:
                    break
            while True:
                tel = input("Entrez le numéro de téléphone: ")
                tel = tel.strip()
                if tel.isdecimal() and len(tel) == 10 and (
                        tel.startswith("06") or tel.startswith("07") or tel.startswith("05")):
                    break
                print("─" * 100)
                print("Vous devez entrer un numéro de téléphone à 10 chiffres commençant par 06, 07 ou 05")
                print("─" * 100)
            while True:
                email = input("Entrez l'adresse e-mail: ")
                email = email.strip()
                if "@" in email and "." in email and len(email) > 2:
                    break
                print("─" * 100)
                print("E-mail incorrect, entrez un e-mail valide")
                print("─" * 100)
            new = {"idClt": len(Clients) + 1,
                   "nom": nom,
                   "tel": tel,
                   "email": email}
            print(new)
            Clients.append(new.copy())
            print("─" * 100)
            print("ٍٍٍٍٍٍVoici la liste des clientes:")
            affiche(Clients)
            print("─" * 100)
            print("Le client a été ajouté avec succès")
            print("─" * 100)
            # ============Rechercher une adherent============
        elif n == 3:
            r = input("Entrez le nom ou telephone de client: ")
            j = 0
            for i in Clients:
                if r.lower() in i['nom'].lower() or r in i['tel']:
                    print("─" * 100)
                    for key, value in i.items():
                        print(f"== {key}{(12 - len(key)) * " "}:  {value}")
                    print("─" * 100)
                    j += 1
            if j == 0:
                print("─" * 100)
                print("Aucun client avec ce nom ou telephone")
                print("─" * 100)
        # ============Quitter============
        elif n == 4:
            break


###########################################################VENTE#####################################################

def vente():
    global somme, produit, idvente, nomClt, dateVente, idClt, idArt, quantite
    while True:
        print(" " * 70, "╭──────────────────────────╮")
        print(" " * 70, "│           VENTE          │")
        print(" " * 70, "├──────────────────────────┤")
        print(" " * 70, "│       1 - Lister         │")
        print(" " * 70, "│       2 - Détail         │")
        print(" " * 70, "│       3 - Ajouter        │")
        print(" " * 70, "│       4 - Quitter        │")
        print(" " * 70, "╰──────────────────────────╯\n")
        while True:
            n = input("choisir votre choix dans le menu precendent: ")
            n = n.strip()
            if n == "1" or n == "2" or n == "3" or n == "4":
                n = int(n)
                break
            print("─" * 100)
            print("Choix invalide, tapez une chiox valide")
            print("─" * 100)
        # ============Afficher la liste des clients============
        if n == 1:
            print("ٍٍٍٍٍٍVoici la liste des ventes :")
            data = []
            temp = []
            heading = ['idVente', 'idClt', 'Nom du client', 'Date d\'achat', 'Nombre d\'achats']
            for i in Ventes:
                for key, value in i.items():
                    if key == 'articles':
                        # Sans répétition
                        # temp.append(len(value))
                        nmbr = 0
                        for i in value:
                            nmbr += i['quantité']
                        temp.append(nmbr)
                    elif key == 'date':
                        for k in Clients:
                            if k["idClt"] == i["idClt"]:
                                temp.append(k["nom"])
                        temp.append(value)
                    else:
                        temp.append(value)
                data.append(temp.copy())
                temp.clear()
            print(tabulate(data, headers=heading, tablefmt="rounded_outline"))

        # ============Afficher les détails de vente============
        elif n == 2:
            print("─" * 100)
            print("ٍٍٍٍٍٍVoici la liste des ventes :")
            data = []
            temp = []
            heading = ['idVente', 'idClt', 'Nom du client', 'Date d\'achat', 'Nombre d\'achats']
            for i in Ventes:
                for key, value in i.items():
                    if key == 'articles':
                        # Sans répétition
                        # temp.append(len(value))
                        nmbr = 0
                        for i in value:
                            nmbr += i['quantité']
                        temp.append(nmbr)
                    elif key == 'date':
                        for k in Clients:
                            if k["idClt"] == i["idClt"]:
                                temp.append(k["nom"])
                        temp.append(value)
                    else:
                        temp.append(value)
                data.append(temp.copy())
                temp.clear()
            print(tabulate(data, headers=heading, tablefmt="rounded_outline"))
            cont = True
            while cont:
                while True:
                    idvente = input("Entrez l'id du vente dont vous souhaitez afficher les détails: ")
                    if idvente.isdecimal():
                        idvente = int(idvente)
                        break
                    print("─" * 100)
                    print("l'id doit être composé uniquement de chiffres")
                    print("─" * 100)
                for i in Ventes:
                    if i['idVente'] == idvente:
                        cont = False
                if cont:
                    print("─" * 100)
                    print("l'id saisi est introuvable, Veuiller saisi une id correcte")
                    print("─" * 100)
                else:
                    break
            print("─" * 100, "\n")
            for i in Ventes:
                for j in Clients:
                    if i["idClt"] == j["idClt"]:
                        nomClt = j["nom"]
                        dateVente = i["date"]
            print("=" * 61)
            print(f"ٍٍٍٍٍٍٍVoici les détails des achats de {nomClt} en date du {dateVente} :\n")
            data = []
            temp = []
            heading = ['idArt', 'nom d\'article', 'prix d\'article', 'quantité']
            for i in Ventes:
                if i['idVente'] == idvente:
                    somme = 0
                    for j in i['articles']:
                        for key, value in j.items():
                            if key == "quantité":
                                for t in Articles:
                                    if t["idArt"] == j["idArt"]:
                                        temp.append(t["nom"])
                                        temp.append(t["prix"])
                                        produit = t["prix"] * j["quantité"]
                                somme += produit
                            temp.append(value)
                        data.append(temp.copy())
                        temp.clear()
            print(f"id Vente : {idvente}")
            print("Client:", nomClt, " " * (61 - len(nomClt) - len(dateVente) - 16), "Date:", dateVente)
            print(tabulate(data, headers=heading, tablefmt="rounded_outline"))
            print("Le prix d'achat total est :", " " * (32 - len(str(somme))), somme)
            print("=" * 61)
        # ============Ajouter un nouveau Vente============
        elif n == 3:
            # choisir le client
            while True:
                print("─" * 100)
                print("ٍٍٍٍٍٍVoici la liste des clients :")
                affiche(Clients)
                condition = input("Êtes-vous inscrit? Écrivez \"oui\" ou \"non\": ")
                if condition.lower() == "oui":
                    print("ٍٍٍٍٍٍVoici la liste des clients :")
                    affiche(Clients)
                    cont = True
                    while cont:
                        while True:
                            idClt = input("Veuillez taper votre id qui apparaît dans la liste ci-dessus: ")
                            if idClt.isdecimal():
                                idClt = int(idClt)
                                break
                            print("─" * 100)
                            print("l'id doit être composé uniquement de chiffres positifs")
                            print("─" * 100)
                        for i in Clients:
                            if i['idClt'] == idClt:
                                cont = False
                        if cont:
                            print("─" * 100)
                            print("l'id saisi est introuvable, Veuiller saisi une id correcte")
                            print("─" * 100)
                        else:
                            break
                    break
                elif condition.lower() == "non":
                    s = '[§@_!#$%^&*()<>?/\\|}{~^]1234567890-°+=\"'
                    while True:
                        c = 0
                        nom = input("Entrez le nom de client: ")
                        for i in nom:
                            if i in s:
                                c += 1
                        if c > 0 or len(nom) < 2:
                            print("─" * 100)
                            print("nom invalide, Entrez un nom correct")
                            print("─" * 100)
                        elif c == 0 and len(nom) > 1:
                            break
                    while True:
                        tel = input("Entrez le numéro de téléphone: ")
                        tel = tel.strip()
                        if tel.isdecimal() and len(tel) == 10 and (
                                tel.startswith("06") or tel.startswith("07") or tel.startswith("05")):
                            break
                        print("─" * 100)
                        print("Vous devez entrer un numéro de téléphone à 10 chiffres commençant par 06, 07 ou 05")
                        print("─" * 100)
                    while True:
                        email = input("Entrez l'adresse e-mail: ")
                        email = email.strip()
                        if "@" in email and "." in email and len(email) > 2:
                            break
                        print("─" * 100)
                        print("E-mail incorrect, entrez un e-mail valide")
                        print("─" * 100)
                    idClt = len(Clients) + 1
                    new = {"idClt": idClt,
                           "nom": nom,
                           "tel": tel,
                           "email": email}
                    print(new)
                    Clients.append(new.copy())
                    print("─" * 100)
                    print("ٍٍٍٍٍٍVoici la liste des clientes:")
                    affiche(Clients)
                    print("─" * 100)
                    print("Le client a été ajouté avec succès")
                    print("─" * 100)
                    break
                else:
                    print("─" * 100)
                    print("choix invalide, tapez une chiox valide.")
                    print("─" * 100)
            print("ٍٍٍٍٍٍVoici la liste des articles :")
            affiche(Articles)

            # choisir l'article
            artachete = []
            while True:
                cont = True
                while cont:
                    while True:
                        idArt = input("Écrivez l'id d'article que vous souhaitez acheter: ")
                        idArt = idArt.strip()
                        if idArt.isdecimal():
                            idArt = int(idArt)
                            break
                        print("─" * 100)
                        print("l'id doit être composé uniquement de chiffres positifs")
                        print("─" * 100)
                    for i in Articles:
                        try:
                            if i['idArt'] == idArt:
                                cont = False
                        except:
                            continue
                    if cont:
                        print("─" * 100)
                        print("l'id saisi est introuvable, Veuiller saisi une id correcte")
                        print("─" * 100)
                    else:
                        while True:
                            quantite = input("Combien voulez-vous acheter de cet article: ")
                            quantite = quantite.strip()
                            if quantite.isdecimal():
                                quantite = int(quantite)
                                if quantite >= 1:
                                    break
                            print("─" * 100)
                            print("choix invalide, vuillez taper une choix valide")
                            print("─" * 100)
                        break
                artachete.append({'idArt': idArt, 'quantité': quantite})
                while True:
                    tocontinue = input("Voulez-vous ajouter un autre articl? Écrivez \"oui\" ou \"non\": ")
                    tocontinue = tocontinue.strip()
                    if tocontinue.lower() == "oui" or tocontinue.lower() == "non":
                        break
                    print("─" * 100)
                    print("choix invalide, vuillez taper une choix valide")
                    print("─" * 100)
                if tocontinue.lower() == "non":
                    break
            idvente = len(Ventes) + 1
            date = datetime.datetime.today().strftime('%d/%m/%Y')
            vente_temp = {'idVente': idvente, 'idClt': idClt, 'date': date, 'articles': artachete}
            # noinspection PyTypeChecker
            Ventes.append(vente_temp)
            print("─" * 100)
            print("L'operation a réussi")
            print("─" * 100)
            print("Voici votre recu : ")
            # aficher le recu
            for i in Clients:
                if i['idClt'] == idClt:
                    nomClt = i['nom']
            data = []
            temp = []
            heading = ['idArt', 'nom d\'article', 'prix d\'article', 'quantité']
            for i in Ventes:
                if i['idVente'] == idvente:
                    somme = 0
                    for j in i['articles']:
                        for key, value in j.items():
                            if key == "quantité":
                                for t in Articles:
                                    if t["idArt"] == j["idArt"]:
                                        temp.append(t["nom"])
                                        temp.append(t["prix"])
                                        produit = t["prix"] * j["quantité"]
                                somme += produit
                            temp.append(value)
                        data.append(temp.copy())
                        temp.clear()
            print(f"id Vente : {idvente}")
            print("Client:", nomClt, " " * (61 - len(nomClt) - len(date) - 16), "Date:", date)
            print(tabulate(data, headers=heading, tablefmt="rounded_outline"))
            print("Le prix d'achat total est :", " " * (32 - len(str(somme))), somme)
            print("=" * 61)
        # ============Quitter============
        elif n == 4:
            break


def title():
    print(" " * 15,
          " ██████╗ ███████╗███████╗████████╗██╗ ██████╗ ███╗   ██╗    ██████╗ ███████╗███████╗    ██╗   ██╗███████╗███╗   ██╗████████╗███████╗███████╗")
    print(" " * 15,
          "██╔════╝ ██╔════╝██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║    ██╔══██╗██╔════╝██╔════╝    ██║   ██║██╔════╝████╗  ██║╚══██╔══╝██╔════╝██╔════╝")
    print(" " * 15,
          "██║  ███╗█████╗  ███████╗   ██║   ██║██║   ██║██╔██╗ ██║    ██║  ██║█████╗  ███████╗    ██║   ██║█████╗  ██╔██╗ ██║   ██║   █████╗  ███████╗")
    print(" " * 15,
          "██║   ██║██╔══╝  ╚════██║   ██║   ██║██║   ██║██║╚██╗██║    ██║  ██║██╔══╝  ╚════██║    ╚██╗ ██╔╝██╔══╝  ██║╚██╗██║   ██║   ██╔══╝  ╚════██║")
    print(" " * 15,
          "╚██████╔╝███████╗███████║   ██║   ██║╚██████╔╝██║ ╚████║    ██████╔╝███████╗███████║     ╚████╔╝ ███████╗██║ ╚████║   ██║   ███████╗███████║")
    print(" " * 15,
          " ╚═════╝ ╚══════╝╚══════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝    ╚═════╝ ╚══════╝╚══════╝      ╚═══╝  ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚══════╝")

def bye():
    print(" " * 64, "             ▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄   ")
    print(" " * 64, "             █▒▒░░░░░░░░░▒▒█   ")
    print(" " * 64, "              █░░█░░░░░█░░█    ")
    print(" " * 64, "           ▄▄  █░░░▀█▀░░░█  ▄▄ ")
    print(" " * 64, "          █░░█ ▀▄░░░░░░░▄▀ █░░█")
    print(" " * 64, "█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
    print(" " * 64, "█░░                                   ░░█")
    print(" " * 64, "█░░             AU REVOIR             ░░█")
    print(" " * 64, "█░░                                   ░░█")
    print(" " * 64, "█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")


title()
menu()
