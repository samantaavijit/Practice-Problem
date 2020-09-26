"""
Create By - Avijit Samanta
Date - 26/09/2020

Problem Statement:- Avijit das is a fraud by nature. Avijit Samanta wrote a python function to print a multiplication
table of a given number and put one of the values (randomly generated) as wrong.

Avijit Samanta did this to fool his classmates and make them commit a mistake in a test. You cannot tolerate this!

So you decided to use your python skills to counter Avijit’s actions by writing a python program that validates
Avijit’s multiplication table.

Your function should be able to find out the wrong values in Avijit’s table and expose Avijit Samanta as a fraud.

Note: Avijit’s function returns a list of numbers like this

Avijit Samanta’s Function Input:
avijitMultiplication(6)

Avijit’s function returns this output:
[6, 12, 18, 26, …., 60]

You have to write a function isCorrect(table, number) and return the index where avijit’s function is wrong and print
it to the screen! If the table is correct, your function returns None
"""
import random


def avijitMultiplication(number):
    wrong = random.randint(0, 9)
    table = [number * i for i in range(1, 11)]
    table[wrong] = table[wrong] + random.randint(0, 10)
    return table


def isCorrect(table, number):
    for i in range(1, 11):
        if table[i - 1] != i * number:
            return i - 1
    return None


if __name__ == '__main__':
    n = int(input("Enter the number "))
    myTable = avijitMultiplication(n)
    print(f"My Table is {myTable}")
    wrongIndex = isCorrect(myTable, n)

    print(f"Wrong index is {wrongIndex}")
