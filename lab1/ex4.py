"""Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores."""

A="A"
for i in range(1,26):
    A=A+chr(ord(A[-1])+1)

print(A)

y=input()

x=""

for c in y:
    if c in A:
        x=x+"_"
    x = x + c.lower()

x=x[1:]

print(x)