import re

with open("lorem_ipsum.txt") as file:
    text = file.read()

text=re.sub(r'[^a-zA-Z0-9\s]+',"",text)
print(text)
cuvinte = text.split(" ")

cuvinte.sort()
print(cuvinte)
