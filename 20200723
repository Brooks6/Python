#function
def sayHi(name):#def is a mark word means that you want to use function
  print("Hello " + name )

sayHi("Mike") 

#return statement
def cube(num):
  return num*num*num

cube(3)

#if statement
is_male = True
is_tall = True

if is_male or is_tall:#"and" also could be used
  print("balabala")
elif is_male and not(is_tall)
  print("balabala")
else:
  print("balabala")
  
#if comparisions
def maxNum(num1, num2, num3)
  if num1 >= num2 and num1 >= num3
    return num1
  elif num2 >= num1 and num2 >= num3
    return num2
  else
    return num3
  
 print(maxNum(1, 2, 3))

#building a better calculator
'''
input num1, op("+", "-", "*", "/"), num2
and then use if statement to deal with these two numbers
'''

#dictionaries
monthConversions = {
  "Jan": "January",# 1: "January"
  "Feb": "February",
  "Mar": "March"
}

print(monthConversions["Feb"])
print(monthConversions.get("Dec", "Not a vaild key"))

#while loops
i = 1
while i <= 10:#def, if and while, both of them use colon replace open curly brace
  print(i)
  i +=1
  
print("Done with loop")

#building a guess game
secret_word = "Brooks"
guess = ""
guess_count = 0
guess_of_guesses = False

while guess != secret_word and not(out_of_guesses):
  if guess_count < guess_limit
    guess = input("Please try to guess the creator's name")
    guess_count += 1
  else:
    out_of_guesses = True
    
if out_of_guesses:
  print("you lose")
else
  print("you win")
  
#for loops
for letter in "Brooks":#for every letter inside "Brooks", I want to do sth.
  print(letter)
'''
outcome below:
B
r
o
o
k
s
'''
friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
  print(name)
for index in range(3,10):#outcome:3~9
  print(index)
  
#exponent function
def raise_to_power(base_num, pow_num):
  result = 1
  for index in range(pow_num)
    result = result * base_num
  return result

print(raise_to_power(3, 4))

#2D lists & neste loops
number_grid = [
  [1, 2, 3]
  [4, 5, 6]
  [7, 8, 9]
  [0]
]

print(number_grid[0][0])
for row in number_grid:
  for colon in row:
    print(colon)
    
#build a basic translator
def translate(phrase):
  translation = ""
  for letter in phrase:
    if letter in "aeiouAEIOU":
      translation = translation + "g"
    else:
      translation = translation + letter
  return translation

print(translate(input("Enter a phrase")))

#comments
#single line
'''
mutiple lines
'''
"""
mutiple lines
"""

#try except
try:
  value = 10 / 0  
  number = int(input("enter a number:"))
  print(number)
except ValueError:#specified issues
  print("invalid input")
except ZeroDivisionError as err:
  print(err)
