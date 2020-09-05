result = ""
phrase = input("enter a sentence")
for letter in phrase:
    if letter in "aeiouAEIOU":
        result += 'g'
    else:
        result += letter

print(result)