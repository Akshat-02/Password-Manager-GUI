import string
import random


def password_generator():

    #Using string module to generate specific characters
    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = list(string.punctuation)

    #Specifiyng the max and min characters in password
    count_letters = random.randint(12, 14)        
    count_numbers = random.randint(6, 8)
    count_symbols = random.randint(6, 8)

    password_list = []

    #Appending random letters to the password list
    for i in range(count_letters):
        password_list.append(random.choice(letters))


    #Appending random numbers to the password list
    for i in range(count_numbers):
        password_list.append(random.choice(numbers))


    #Appending random symbols to the password list
    for i in range(count_symbols):
        password_list.append(random.choice(symbols))

    
    #Shuffling the elements of generated password list 
    random.shuffle(password_list)

    #Converting password list to a string
    password_generated = "".join(password_list)

    return password_generated

