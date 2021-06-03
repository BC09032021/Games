# rock,paper,scissors
# import random
from random import randint

choices = ['rock', 'paper', 'scissors']


while True:
    n = input("rock or paper or scissors or exit:")
    com = choices[randint(0, 2)]

    if com == n:
        print("Tie!!")
    elif n.lower() == 'rock':
        if com == 'paper':
            print("you lose",com, "beats",n )
        else:
            print("you win  😊😊😊" ,n, "beats",com)
    elif (n.lower() == 'paper'):
        if (com == 'rock'):
            print("you win  😊😊😊" ,n, "beats",com)

        else:
            print("you lose", com, "beats", n)
    elif (n.lower() == 'scissors'):
        if (com == 'paper'):
            print("you win  😊😊😊" ,n, "beats",com)

        else:
            print("you lose", com, "beats", n)
    elif n.lower() == 'exit':
        print("It's nice playing with u!!!!")
        break;
    else:
        print("Check your spelling 🙄🙄🙄!!!")
