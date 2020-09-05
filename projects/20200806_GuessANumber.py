import random
answer = random.randint(1, 100)
count = 1;
gameover = False
while not(gameover):
    guess = int(input("enter a number"))
    if guess > answer:
        print("the number is bigger than the answer")
    elif guess < answer:
        print("the number is smaller than the answer")
    else:
        print("your are right!")
        gameover = True
        continue
    count += 1
print("count: " + str(count))
