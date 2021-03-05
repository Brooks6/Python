x = int(input('x = '))
y = int(input('y = '))


def get_min(x, y):
    if x < y:
        return x
    else:
        return y

def get_max(x, y):
    if x > y:
        return x
    else:
        return y

# GCD
for index in range(get_min(x, y) + 1, 0, -1):
    if x % index == 0 and y % index == 0:
        print("LCM = " + str(index))
        break

#LCM
for index2 in range(1, get_max(x, y) + 1):
    if (index2 * get_min(x, y)) % get_max(x, y) == 0:
        print("GCD = " + str(index2 * get_min(x, y)))
        break