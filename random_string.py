#random_string.py

import random

str_digits = '0123456789'
str_lowercase= 'abcdefghijklmnopqrstuvwxyz'
str_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
str_all = str_digits +  str_lowercase + str_uppercase

def random_string():
    
    string = random.sample(str_all,5)

    random_string = ''.join(string)

    print(random_string)



random_string()
