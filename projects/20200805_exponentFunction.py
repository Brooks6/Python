def cub(basic, pow):
    result = 1
    for index in range(0, pow):
        result *= basic
    return result

print(cub(2, 5))