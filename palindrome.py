# Reconnaître si une chaîne de caractères est palindrome
def is_palindrome(a):
    for i in range(len(a)//2):
        if a[i] != a[-i-1]:
            return False
    return True
# Dictionnaire associatif des caractères accentuées en langue francophone
car = {
        "à" : "a",
        "ä" : "a",
        "â" : "a",
        "ç" : "c",
        "é" : "e",
        "è" : "e",
        "ë" : "e",
        "ï" : "i",
        "ô" : "o",
        "ù" : "u",
        "ü" : "u",
        "û" : "u",
        " " : "",
        "-" : "",
        "," : "",
        "'" : "",
        "?" : "",
        "!" : "",
        "." : ""
    }
# Remplacer des caractères par d'autres
def moulinette(a):
    a = a.lower()
    for cle,valeur in car.items():
        a = a.replace(cle,valeur)
    return a
# MAIN
a = moulinette(input("Entrez une phrase : "))
if is_palindrome(a) == True:
    print("C'est un palindrome.")
else:
    print("Ce n'est pas un palindrome.")