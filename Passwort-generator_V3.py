import random
import string

def generate_password(length=8):
    if length < 8:
        raise ValueError("La longueur minimale du mot de passe est de 8 caractères")
    
    min_required_length = 2 + 4 + 1 + 1 
    if length < min_required_length:
        raise ValueError(f"La longueur doit être d'au moins {min_required_length} caractères pour satisfaire toutes les conditions")
    
    uppercase_chars = ''.join(random.choices(string.ascii_uppercase, k=2))
    lowercase_chars = ''.join(random.choices(string.ascii_lowercase, k=4))
    digit_chars = ''.join(random.choices(string.digits, k=1))
    special_chars = ''.join(random.choices(string.punctuation, k=1))
    
    remaining_length = length - (2 + 4 + 1 + 1)
    all_chars = string.ascii_letters + string.digits + string.punctuation
    remaining_chars = ''.join(random.choices(all_chars, k=remaining_length))
    
    password_chars = uppercase_chars + lowercase_chars + digit_chars + special_chars + remaining_chars
    
    password_list = list(password_chars)
    random.shuffle(password_list)
    
    password = ''.join(password_list)
    
    return password

if __name__ == "__main__":
    try:
        pwd = generate_password(8)
        print(f"Mot de passe généré: {pwd}")
    except ValueError as e:
        print(f"Erreur: {e}")