"""Write a script that calculates how many vowels are in a string."""

def counting_vowels(x):
    nr = 0
    for m in map(x.lower().count, "aeiou"):
        nr = nr + m
        print(m)


    print(nr)


x=input()
counting_vowels(x)
"""
map(func,vec) = [func(x) for x in vec] 
 
"""