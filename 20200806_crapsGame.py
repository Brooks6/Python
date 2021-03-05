import random

money = 1000
while money > 0:
    goon = False
    print("your total moeny : %d \n" % money)
    while True:
        bet = int(input("please bet: \n"))
        if 0 < bet <= 1000:
            break
        else:
            print("illegal amount, please bet again")
            bet = int(input("please bet"))
    first = random.randint(1, 6) + random.randint(1, 6)
    print("the number of first dice is: %d" % first)
    if first == 7 or first == 11:
        print("you win!")
        money += bet
    elif first == 2 or first == 3 or first == 12:
        print("you lose")
        money -= bet
    else:
        goon = True
    while goon:
        goon = False
        second = random.randint(1, 6) + random.randint(1, 6)
        print("the number of dice is: %d" % second)
        if second == 7:
            print("you lose")
            money -= bet
        elif second == first:
            print("you win")
            money += bet
        else:
            goon = True

print("gameover!")
