import random

def get_num_randomly():
    random_number = random.randint(0,9)
    return random_number

print("== WELCOME TO THE GAME==")
chance = 0
while 1:
    choice = input("do you want to play (y/n):")
    if 'y' in choice.lower():
        print("Generate random nuber between 0 to 9")
        random_number = get_num_randomly()
        while 1:
            chance += 1
            user_num = int(input("enter a number between 0 to 9:\t"))
            if user_num > 9 or user_num < 0:
                print("Invalid input")
            else:
                if user_num == random_number:
                    print("congrats you got the number in {0} chances".format(chances))
                    chances = 0
                    break
                elif user_num > random_number:
                    if abs(user_num - random_number) <= 4:
                        print("close but not correct, try lower number")
                    else:
                        print("not even close, try another")
                
                elif user_num < random_number:
                    if abs(user_num - random_number) >= 4:
                        print("close but not correct, try higher")
                    else:
                        print("not even close, try another")
    elif 'n' in choice.lower():
        print("Exiting...")
        break
    else:
        print("Invalid input...")