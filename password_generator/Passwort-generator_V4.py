import random
import string

def generate_password(length):
    """
    Génère un mot de passe aléatoire avec les caractéristiques suivantes :
    - Longueur minimale : 8 caractères
    - Au moins 4 lettres minuscules
    - Au moins 2 lettres majuscules
    - Au moins 1 chiffre
    - Au moins 1 caractère spécial
    """
    # Vérifier que la longueur est suffisante
    if length < 8:
        raise ValueError("Le mot de passe doit contenir au moins 8 caractères")
    
    # Boucle jusqu'à ce qu'un mot de passe valide soit généré
    while True:
        # Créer une liste vide pour stocker les caractères du mot de passe
        password_chars = []

        # Ajouter obligatoirement les caractères requis
        # 4 lettres minuscules
        for _ in range(4):
            password_chars.append(random.choice(string.ascii_lowercase))

        # 2 lettres majuscules
        for _ in range(2):
            password_chars.append(random.choice(string.ascii_uppercase))

        # 1 chiffre
        password_chars.append(random.choice(string.digits))

        # 1 caractère spécial
        password_chars.append(random.choice(string.punctuation))

        # Remplir le reste du mot de passe avec des caractères aléatoires
        remaining_length = length - len(password_chars)
        all_characters = string.ascii_letters + string.digits + string.punctuation

        for _ in range(remaining_length):
            password_chars.append(random.choice(all_characters))

        # Mélanger les caractères pour éviter les motifs prévisibles
        random.shuffle(password_chars)

        # Convertir la liste en chaîne de caractères
        password = ''.join(password_chars)
        # Vérifier si le mot de passe répond aux critères
        # (cette vérification est redondante ici car nous l'avons construit selon les règles)
        lower_count = sum(1 for c in password if c.islower())
        upper_count = sum(1 for c in password if c.isupper())
        digit_count = sum(1 for c in password if c.isdigit())
        special_count = sum(1 for c in password if c in string.punctuation)
        
        # Si tous les critères sont respectés, retourner le mot de passe
        if lower_count >= 4 and upper_count >= 2 and digit_count >= 1 and special_count >= 1:
            return password

# Exemple d'utilisation
if __name__ == "__main__":
    try:
        # Demander la longueur souhaitée à l'utilisateur
        length = int(input("Entrez la longueur souhaitée pour le mot de passe (minimum 8) : "))
        pwd = generate_password(length)
        print(f"Mot de passe généré : {pwd}")
    except ValueError as e:
        print(f"Erreur : {e}")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
