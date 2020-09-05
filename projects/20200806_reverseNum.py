num = int(input("enter a number:\n"))
def get_digits(aNum):
    count = 0
    result = int(aNum)
    while result >= 1:
        result = int(result / 10)
        count += 1
    return count
#print(get_digits(num))

reversed_num = 0

for index in range(1, get_digits(num) + 1):
    reversed_num += int(num / (10 ** (get_digits(num) - index))) % 10 * (10 ** (index - 1))
print(reversed_num)

'''
num = int(input('num = '))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)
'''