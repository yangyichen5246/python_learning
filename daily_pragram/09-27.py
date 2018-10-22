import random
secretNumber = random.randint(1,20)
print('来，咋们玩一个游戏，猜一个1-20间的数值.')

for guessesTaken in range(1,8):
    print('游戏开始,请在下方输入一个数字:')
    guess = int(input())



    if guess < secretNumber:
        print('你猜的太小了')
    elif guess > secretNumber:
        print('你猜的太大了')
    else:
        break
if guess == secretNumber:
   print('bingo，我猜的数值就是' + str(secretNumber))
   print("非常棒，猜对了 只用了" + str(guessesTaken) + "次")
else:
   print('错了其实我猜的数值是' + str(secretNumber))

