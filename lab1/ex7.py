'''Write a function that extract a number from a text
 (for example if the text is "An apple is 123 USD", this function will return 123)'''

x= input()
y=x.split()

for i in range(0,len(y)):
    if y[i].isnumeric():
        print(y[i])
