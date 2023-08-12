
# Convertisseur Nombre-Texte

Ce module Python permet de convertir des nombres entiers naturels de 0 à 999 999 999 999 en texte en français et vice versa. Le module offre les fonctionnalités suivantes :

- `convertir_en_nombre(texte: str) -> int` : Cette fonction prend une chaîne de caractères en entrée et retourne le nombre entier correspondant. Si la chaîne de caractères ne peut pas être convertie en nombre, la fonction renvoie -1.

- `convertir_en_lettre(n: int) -> str` : Cette fonction prend un nombre entier en entrée et renvoie sa représentation en texte en français.

## Exemples d'utilisation

```python
from nombre_texte import convertir_en_nombre, convertir_en_lettre

# Conversion de texte en nombre
nombre = convertir_en_nombre("deux cent quarante")
print(nombre)  # Résultat : 240

# Conversion de nombre en texte
texte = convertir_en_lettre(99999)
print(texte)  # Résultat : "quatre-vingt-dix-neuf mille neuf cent quatre-vingt-dix-neuf"
```

## Utilisation des fonctions

### `convertir_en_nombre(texte: str) -> int`

Cette fonction prend en charge la conversion de nombres en texte en utilisant des mots comme "cent", "mille", "million" et "milliard".

Si le texte d'entrée ne peut pas être converti en nombre, une exception de type `ValueError` est levée.

### `convertir_en_lettre(n: int) -> str`

Cette fonction permet de convertir des nombres en chiffres en texte en français. Elle gère les nombres jusqu'à 999 999 999 999.

Si le nombre d'entrée n'est pas un entier ou s'il dépasse la limite prise en charge, une exception de type `ValueError` est levée.

## Notes

- Ce module utilise un système de cache pour optimiser les conversions et éviter les recalculs inutiles.

- Assurez-vous d'importer le module "Cache" pour que le code fonctionne correctement.

- Le module est conçu pour traiter les nombres entiers naturels de 0 à 999 999 999 999.

## Auteur

Ce module a été développé par Léonid Gr.

N'hésitez pas à contribuer, signaler des problèmes ou améliorer le code en créant des pull requests.

---

