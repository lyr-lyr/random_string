#random_string.py

import random

str_digits = '0123456789'
str_lowercase= 'abcdefghijklmnopqrstuvwxyz'
str_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def random_string():
    #the numble of digits,lowercase and uppercase
    digits_num = random.randint(1,3)
    uppercase_num = random.randint(1,5-digits_num-1)
    lowercase_num = 5 - (digits_num + uppercase_num)

    #create a string
    string = random.sample(str_digits,digits_num) + random.sample(str_uppercase,uppercase_num) + random.sample(str_lowercase,lowercase_num)

    #shuffl
    random.shuffle(string)

    random_string = ''.join(string)

    print(random_string)



random_string()