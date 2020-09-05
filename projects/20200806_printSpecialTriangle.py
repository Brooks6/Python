'''
    *
   ***
  *****
 *******
*********
'''
result = ""
space = " "
star = "*"
x = 0
y = 0
for row in range(1, 6):
    space_times = 5 - row
    star_times = 2 * row - 1
    while x < space_times:
        result += space
        x += 1
    while y < star_times:
        result += star
        y += 1
    print(result)
    x = 0
    y = 0
    result = ""
'''
    for i in range(row):
        for _ in range(row - i - 1):
            print(' ', end='')
        for _ in range(2 * i + 1):
            print('*', end='')
        print()
'''