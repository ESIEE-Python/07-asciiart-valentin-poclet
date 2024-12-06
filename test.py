def artcode_i(s):
    """Encode une chaîne de caractères en utilisant un algorithme itératif."""
    if not s:  # Cas où la chaîne est vide
        return []
    
    Ox = 1  # Compteur d'occurrences
    L = []  # Résultat
    n = len(s)         
    
    for k in range(1, n):
        if s[k] == s[k - 1]:
            Ox += 1
        else:
            L.append((s[k - 1], Ox))  # Ajouter le groupe encodé
            Ox = 1  # Réinitialiser le compteur
    # Ajouter le dernier groupe
    L.append((s[-1], Ox))
    
    return L

def artcode_r(s):
    """Encode une chaîne de caractères en utilisant un algorithme récursif."""
    if not s:  # Cas de base : chaîne vide
        return []
    
    Ox = 1  # Compteur d'occurrences
    n = len(s)
    
    # Trouver le nombre d'occurrences du premier caractère
    while Ox < n and s[Ox] == s[0]:
        Ox += 1
    
    # Récursivité : traiter le reste de la chaîne
    return [(s[0], Ox)] + artcode_r(s[Ox:])

def main():
    print("Test itératif : ", artcode_i('MMMMaaacXolloMM'))
    print("Test récursif : ", artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
