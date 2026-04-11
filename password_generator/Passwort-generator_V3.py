import random
import string

def create_password(length):
    pass_list = ""
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation
    all = lowercase+uppercase+digits+punctuation
    i=0
    while i<4:
        pass_list += random.choice(lowercase)
        i+=1
        
    while i<6:
        pass_list += random.choice(uppercase)
        i+=1
    while i<7:
        pass_list += random.choice(digits)
        i+=1
    while i<8:
        pass_list += random.choice(punctuation)
        i+=1
    while i<length:
        pass_list += random.choice(all)
        i+=1
    
    random.shuffle(list(pass_list))
    password = "".join(pass_list)
    return password
    
if __name__ == "__main__":
    pass8 = create_password(10)
    print(pass8)