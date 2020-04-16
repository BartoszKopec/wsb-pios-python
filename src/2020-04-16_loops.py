import random

randomNumber = random.randint(1, 10)
answer=-1
i=0
print('Random number from 1 to 10 was drawn. Guess this number.')

while True:
    try:
        i+=1
        answer = int(input('What is your answer? '))
        if answer == randomNumber:
            break
        elif answer < randomNumber:
            print('Your answer is lower than drawn number.')
        else:
            print('Your answer is greater than drawn number.')

    except ValueError:
        print("No numbers provided")
print('Congratulations. It took ', i ,'attempts to guess the number.')