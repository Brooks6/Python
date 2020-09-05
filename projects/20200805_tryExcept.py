try:
  #value = 10 / 0
  number = int(input("enter a number:"))
  print(number)
except ValueError:#specified issues
  print("invalid input")
except ZeroDivisionError as err:
  print(err)