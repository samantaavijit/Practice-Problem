"""
Problem Statement:- Generate a random integer from a to b. You and your friend have to guess a number between two
numbers a and b. a and b are inputs taken from the user. Your friend is player 1 and plays first. He will have to
keep choosing the number and your program must tell whether the number is greater than the actual number or less than
the actual number. Log the number of trials it took your friend to arrive at the number. You play the same game and
then the person with minimum number of trials wins! Randomly generate a number after taking a and b as input and
don’t show that to the user.

Input:
Enter the value of a
4

Enter the value of b
13

Output:
Player1 :
Please guess the number between 4 and 13
5

Wrong guess a greater number again
8

Wrong guess a smaller number again
6

Correct you took 3 trials to guess the number

Player 2:
Correct you took 7 trials to guess the number

Player 1 wins!
"""
import random


def calculate(cAns, uAns):
    c = 0
    while True:
        c += 1
        if uAns > cAns:
            uAns = int(input("Wrong guess a smaller number again "))
        elif uAns < cAns:
            uAns = int(input("Wrong guess a greater number again "))
        elif uAns == cAns:
            print(f"Correct you took {c} trials to guess the number")
            return c


if __name__ == '__main__':
    try:
        a = int(input("Enter the value of a "))
        b = int(input("Enter the value of b "))
        if a > b:
            a = a + b
            b = a - b
            a = a - b
        print("Player1 :")
        p1 = calculate(random.randint(a, b), int(input(f"Please guess the number between {a} and {b} ")))
        print("Player2 :")
        p2 = calculate(random.randint(a, b), int(input(f"Please guess the number between {a} and {b} ")))

        if p1 > p2:
            print("Player 2 wins!")
        elif p1 < p2:
            print("Player 1 wins!")
        else:
            print("Tie")

    except ValueError:
        print("Enter valid input")
    except Exception as e:
        print(e)
