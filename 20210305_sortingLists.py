even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

even.extend(odd)
print(even)
even.sort()
print(even)
even.sort(reverse=True)
print(even)

new_even = sorted(even, reverse=True)
print(new_even)

name = ["Graham",
        "John",
        "terry",
        "eric",
        "Terry",
        "michael"]
name.sort()
print(name)

name.sort(key = str.casefold)
print(name)