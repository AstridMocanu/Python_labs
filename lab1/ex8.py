'''Write a function that counts how many bits with value 1 a number has.
For example for number 24, the binary format is 00011000, meaning 2 bits with value "1"'''


x=input()
x=int(x)

x=bin(x)
nr=0
for i in x[2:]:
    nr+=int(i)

print(nr)

