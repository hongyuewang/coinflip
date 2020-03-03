import random

def flip(number):
    
    number_of_heads = 0
    number_of_tails = 0
    
    for i in range(number):
        result = random.randint(0,1)

        if result == 1:
            number_of_heads += 1
        else:
            number_of_tails += 1

    print("The coin was flipped " + str(number) + " times.")
    print("It landed on heads " + str(number_of_heads) + " times.")
    print("It landed on tails " + str(number_of_tails) + " times.")

    

