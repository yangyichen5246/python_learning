import random
secretNumber = random.randint(1,20)
print('i am thinking of a number between 1 and 20.')

for guessesTaken in range(1,7):
    print('take a guess ,请在下方输入一个数字:')
    guess = int(input())



    if guess < secretNumber:
        print('your guess is too low')
    elif guess > secretNumber:
        print('your guess is too high')
    else:
        break
if guess == secretNumber:
   print("good job your guess is in " + str(guessesTaken)+" guess!")
else:
   print('nope the number i was thinking was' + str(secretNumber))

