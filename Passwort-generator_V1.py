import random
import string

tous_les_caracteres = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

i=0
password = ""

while i<14:
    password += random.choice(tous_les_caracteres)
    i += 1
    
print(password)
