'''Write a functions that determine the most common letter in a string.
For example if the string is "an apple is not a tomato", then the most common character is "a" (4 times).
Only letters (A-Z or a-z) are to be considered. Casing should not be considered "A" and "a" represent the same character.'''

alfabet="a"
for i in range(1,25):
    alfabet=alfabet+chr(ord(alfabet[-1])+1)

x=input()
def counting_characters(x):
    max = 0
    count=0
    for m in map(x.lower().count, alfabet):
        count=count+1
        if m>max:
            max=m
            poz=count

    print(chr(ord("a") + poz-1))

counting_characters(x)



