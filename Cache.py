"""Module pour créer du cache"""
import json
import constantes
import os

class Cache(dict):
    def __init__(self, taille:int = 100, nom: str = "cache"):
        self.taille = taille
        self.nom = nom
        self.chemin = os.path.join(constantes.CUR_DIR , f"{self.nom}.json")
        self.initialisation()

    def initialisation(self):
        if os.path.exists(self.chemin):
            with open(self.chemin, "r") as f:
                dictionnaire_temp = json.load(f).copy()
                for cle, valeur in dictionnaire_temp.items():
                    self.ajouter(cle, valeur)
               
    def supprimer_premiere_element(self):
        self.pop(list(self.keys())[0])
        self.ecriture()

    def ajouter(self, cle:int|str, valeur:int|str)->None:
        if len(self)<self.taille:
            if str(cle) in self.keys():
                self.pop(str(cle))
            self[cle]=valeur
            self.ecriture()
        else:
            self.supprimer_premiere_element()
            self[cle]=valeur
            self.ecriture()

    def vider(self):
        self.clear()
        self.ecriture()

    def ecriture(self):
        with open(self.chemin, "w") as f:
            json.dump(self, f, indent=4)

if __name__ == '__main__':
    dic = Cache(5,"cache")
    dic.ajouter(0, "léonid")


    print(dic)
