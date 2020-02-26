import random
#Welcome
print('Hello, what is your name?')
myName = input()
print('Hi ' + myName + ', lets play a game!')
print('Im thinking of a number between 1 & 10, you have 5 guesses. Go!')
#Guess Game
rn = random.randint(1,10)
myGuess = int(0)
guessCount =0
while myGuess != rn:
    try:
        print('Take a guess')
        myGuess = int(input())
    except ValueError:
        print("That's not a number bruh, take another guess!")
        myGuess = int(input())
    if myGuess > rn:
        print('Too high')
        guessCount +=1
        print(guessCount)
    elif myGuess < rn:
        print('Too low')
        guessCount +=1
        print(guessCount)
    if guessCount ==5:
        break
if myGuess == rn:
    print ('You Win!')
else:
    print ('You Fail!')
