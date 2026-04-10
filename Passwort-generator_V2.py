import random
import string

def create_password(length):
    password = ""
    i = 0
    while i<length:
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
        i +=1
    return password

pass20 = create_password(20)
print(pass20)