"""Module qui converti les nombre entier naturel de 0 à 999999999999"""
import math
import os
import subprocess
from Cache import Cache

DICTIONNAIRE_NOMBRES = {
    "zéro":0,
    "un":1,
    "deux":2,
    "trois":3,
    "quatre":4,
    "cinq":5,
    "six":6,
    "sept":7,
    "huit":8,
    "neuf":9,
    "dix":10,
    "onze":11,
    "douze":12,
    "treize":13,
    "quatorze":14,
    "quinze":15,
    "seize":16,
    "vingt":20,
    "trente":30,
    "quarante":40,
    "cinquante":50,
    "soixante":60,
    "soixante-dix":70,
    "soixante-onze":71,
    "soixante-douze":72,
    "soixante-treize":73,
    "soixante-quatorze":74,
    "soixante-seize":76,
    "quatre-vingt":80,
    "quatre-vingt-dix":90,
    "quatre-vingt-onze":91,
    "quatre-vingt-douze":92,
    "quatre-vingt-treize":93,
    "quatre-vingt-quatorze":94,
    "quatre-vingt-quinze":95,
    "quatre-vingt-seize":96
}
DICTIONNAIRE_MOTS_SPECIAUX = {
    "cent":100,
    "mille":1000,
    "million":1000000,
    "milliard":1000000000
}
DICTIONNAIRE_NOMBRES_INVERSE = {valeur:cle for cle, valeur in DICTIONNAIRE_NOMBRES.items()}
CACHE_NOMBRE_EN_TEXTE = Cache(1000,"number-to-texte")
CACHE_TEXTE_EN_NOMBRE = {valeur : cle for cle, valeur in CACHE_NOMBRE_EN_TEXTE.items()}


def convertir_en_nombre(texte:str)->int:
    """Fonction qui converti les chaînes de caractères en nombre entier

    Args:
        texte (str): Le chaîne à convertir

    Raises:
        ValueError: Si l'argument texte n'est pas une chaine de caractère ou vide

    Returns:
        int: La chaîne de caractère converti en entier
    """
    nombre_total = 0
    nombre_partiel = 0

    if not isinstance(texte, str) or not texte.strip() or texte.isnumeric():
        raise ValueError("Vous devez entrer une chaine de caractère!")
    try:
        return int(CACHE_TEXTE_EN_NOMBRE[texte])
    except KeyError:
        mots = texte.lower().split()
        #Verifie si tout les mots sont dans les dictionnaires
        verification = all([lettre in DICTIONNAIRE_NOMBRES.keys() or lettre in DICTIONNAIRE_MOTS_SPECIAUX.keys() for lettre in mots])
        
        if verification:
            for lettre in mots:
                if lettre in DICTIONNAIRE_NOMBRES.keys():
                    nombre_partiel +=DICTIONNAIRE_NOMBRES[lettre]
                elif lettre in DICTIONNAIRE_MOTS_SPECIAUX.keys():
                    if nombre_partiel:
                        nombre_partiel *= DICTIONNAIRE_MOTS_SPECIAUX[lettre]
                    else:
                        nombre_partiel += DICTIONNAIRE_MOTS_SPECIAUX[lettre]
                    if lettre in ["mille", "million", "milliard"]:
                        nombre_total += nombre_partiel
                        nombre_partiel = 0
            nombre_total += nombre_partiel
            CACHE_NOMBRE_EN_TEXTE.ajouter(nombre_total,texte)
            return nombre_total
        
        else:
            raise ValueError("Veuillez entrer une valeur correct")
        

def decomposer(mot:str)->list[str]:
    """Fonction qui décompose un nombre à trois chiffres.
    exemple: 350 -> [300,50], 247 -> [200, 40, 7]

    Args:
        mot (str): Le nombre à decomposer

    Returns:
        list[str]: Liste du chaîne de caractère à décomposer en chîne de caractère
    """
    if int(mot) == 0:
        return []
    temp = []
    compteur = len(mot)-1
    for i in range(len(mot)):
        if int(mot[-2:]) in DICTIONNAIRE_NOMBRES_INVERSE.keys() and compteur==len(mot)-2:
            temp.append(str(mot[-2:]))
            break
        temp.append(mot[i]+"0"*(compteur))
        compteur-=1
    return temp


def convertir_en_lettre(n:int)->str:
    """Fonction qui converti les nombres en lettre français

    Args:
        n (int): Le nombre à convertir en lettre français

    Returns:
        str: Le nombre converti
    """
    if not isinstance(n,int) and not str(n).isnumeric():
        raise ValueError("Vous devez entrez un entier seulement")
    elif len(str(n))>12:
        raise ValueError("Votre nombre est trop grand")
    try:
        return CACHE_NOMBRE_EN_TEXTE[str(n)]
    except KeyError:
        mots = str(n)
        l = []
        lettre = []
        nombre_itterations = math.ceil(len(mots)/3)
        for _ in range(nombre_itterations):
            l.append(mots[-3:])
            mots = mots[:-3]
        i=nombre_itterations
        for mot in l[::-1]:
            if len(mot)<=2 and int(mot) in DICTIONNAIRE_NOMBRES_INVERSE.keys():
                if i==2 and int(mot)==1:
                    pass
                else:
                    lettre.append(DICTIONNAIRE_NOMBRES_INVERSE[int(mot)])
            else:
                try:
                    lettre.append(CACHE_NOMBRE_EN_TEXTE[mot])
                except KeyError:
                    decomposition = decomposer(mot)
                    if len(decomposition)==0:
                            i -=1
                            continue
                    for nombre in decomposition:
                        
                        if int(nombre) == 0:
                            continue
                        elif len(nombre)==3:
                            if(int(nombre[0])==1):
                                pass
                            else:
                                lettre.append(DICTIONNAIRE_NOMBRES_INVERSE[int(nombre[0])])
                            lettre.append("cent")
                        else:
                            lettre.append(DICTIONNAIRE_NOMBRES_INVERSE[int(nombre)])
            if i==2:
                lettre.append("mille")     
            elif i==3:
                lettre.append("million")     
            elif i==4:
                lettre.append("milliard")  
            i-=1
        
        texte = " ".join(lettre)
        CACHE_NOMBRE_EN_TEXTE.ajouter(n,texte)
        return texte

if __name__ == '__main__':
    def menu():
        subprocess.run("clear")
        print("Bienvenu dans Word To Number")
        print("Selectionner une option:")
        print("""
        1. Changer texte en chiffre.\n
        2. Changer chiffre en texte.\n
        3. Quitter.
              """)

        choix = int(input("Votre choix: "))
        if isinstance(choix, int):
            if choix == 1:
                subprocess.run("clear")
                print("Texte en chiffre\n")
                n = input("Entrez le texte: ")
                try:
                    print(f"{n} en nombre égale à {convertir_en_nombre(n)}")
                except ValueError as e:
                    print(e)
                input("Appuyez sur entrer pour continuer...")
                menu()
            if choix == 2:
                subprocess.run("clear")
                print("Chiffre en texte\n")
                n = input("Entrez le chiffre: ")
                try:
                    print(f"{n} en nombre égale à {convertir_en_lettre(n)}")
                except ValueError as e:
                    print(e)
                input("Appuyez sur entrer pour continuer...")
                menu()
            if choix == 3:
                os.close(0)
    menu()