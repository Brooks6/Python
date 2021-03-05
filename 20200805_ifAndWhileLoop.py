num = 6
guessNum = 0
guessCount = 0
guessLimit = 3
gg = False

while int(guessNum) != num and not(gg):
    if guessCount < guessLimit:
        guessNum = input("guess a number")
        guessCount += 1
    else:
        gg = True

if gg:
    print("you lose")
else:
    print("you win")