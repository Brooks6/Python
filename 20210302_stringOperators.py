today = "Friday"
print("day" in today)
print("fri" in today)

print("there are {0} days in {1}, {2}".format(31, "Jan", "Mar"))

for i in range(1, 13):
    print("{0:2} squared is {1:<4} and cubed is {2:^4}".format(i, i ** 2, i **3))
