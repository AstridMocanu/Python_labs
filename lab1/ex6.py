'''Write a function that validates if a number is a palindrome.'''

x=input()
y=x[-1::-1]
if x == y :
    print("Palindrom")
else:
    print("Nu e Palidrom")