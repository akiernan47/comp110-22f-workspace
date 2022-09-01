from random import randint

question: str = input("Ask a yes/no question... ")
response: int = 0

if response == 0:
    print("Yes, definitely")
else:
    if response == 1:
        print("Ask again later")
    else:
        print("My sources say no")