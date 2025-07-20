import string

password = input("Entrez votre mot de passe : ")

upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
special_char = any([1 if c in string.punctuation else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])

characters = [upper_case, lower_case, special_char, digits]

length = len(password)

score = 0

try:
    with open("password_strength.txt", "r") as file:
        common = file.read().splitlines()
except FileNotFoundError:
    common = []

if password in common:
    print("Le mot de passe est trop commun. Votre score est 0/7")
    exit()

if length >= 8:
    score += 1
if length >= 12:
    score += 1
if length >= 16:
    score += 1
if length >= 20:
    score += 1

if sum(characters) >= 1:
    score += 1
if sum(characters) >= 2:
    score += 1
if sum(characters) >= 3:
    score += 1

print(f"Votre mot de passe contient {sum(characters)} types de caractères différents.")

if score < 4:
    print(f"Votre mot de passe est faible. Votre score est {score}/7")
elif score == 4:
    print(f"Votre mot de passe est moyen. Votre score est {score}/7")
elif score == 5:
    print(f"Votre mot de passe est fort. Votre score est {score}/7")
elif score == 6 or score == 7:
    print(f"Votre mot de passe est très fort. Votre score est {score}/7")






