import random
import string

loop01 = 50 > 1
loop02 = 4 > 1

print("How many passwords would you like to print: ", end = '')
number = int(input())

index = 0

while loop01 == True:

    alphabets = list(string.ascii_lowercase)
    capital_alphabets = list(string.ascii_uppercase)
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    special_characters = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", "|", "/", ":", ";", ",", "'", ".", "?"]

    selection = []

    selection.append(random.choice(alphabets))
    selection.append(random.choice(alphabets))
    selection.append(random.choice(alphabets))
    selection.append(random.choice(capital_alphabets))
    selection.append(random.choice(capital_alphabets))
    selection.append(random.choice(numbers))
    selection.append(random.choice(numbers))
    selection.append(random.choice(numbers))
    selection.append(random.choice(special_characters))
    selection.append(random.choice(special_characters))

    c_11 = random.randint(0,2)
    c_12 = random.randint(0,2)
    c_13 = random.randint(0,2)
    c_21 = random.randint(3,4)
    c_22 = random.randint(3,4)
    c_31 = random.randint(5,7)
    c_32 = random.randint(5,7)
    c_33 = random.randint(5,7)
    c_41 = random.randint(8,9)
    c_42 = random.randint(8,9)

    positions = [
        c_11, c_12, c_13, c_21, c_22, c_31, c_32, c_33, c_41, c_42 
    ]

    password = random.shuffle(positions)

    if loop02 == True:
        print(selection[positions[0]]+selection[positions[1]]+selection[positions[2]]+selection[positions[3]]+selection[positions[4]]+selection[positions[5]]+selection[positions[6]]+selection[positions[7]]+selection[positions[8]]+selection[positions[9]])
        index = index + 1
    if index == number:
        loop01 = False