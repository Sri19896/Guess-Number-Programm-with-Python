import random
number = random.randrange(1, 50)
print(number)
while True:
    Guess = input('Guess the number  ')
    Guess = int(Guess)
    if Guess > 0:
        if Guess == number:
            print('Congratualtions ')
            break
        else:
            print('Sorry Try Again')
    else:
        print('Please  Enetr valid Number')
        continue
