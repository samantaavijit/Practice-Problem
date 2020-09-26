"""
Create By - Avijit Samanta
Date - 26/09/2020

Problem Statement:- Its result day at school and not everyone is happy. You decided to make your friends laugh by
jumbling their names to come up with some funny names.

Your program should take the number of names and the names separated by space as input. Output should be funny names
in the same order.

Input:
Enter number of friends:
3

Enter the name of your 3 friends:
Rohan Das
Shubham Agarwal
Ritesh Arora

Output:
Ritesh Das
Shubham Arora
Rohan Agarwal
"""
import random


def getFirstLastName(nameList):
    flName = [item.split(" ") for item in nameList]
    newName = []
    for item in flName:
        if len(item) > 2:
            item[1] = item[1] + " " + item[2]
            del item[2]
        newName.append(item)
    return newName


def changeName(nameList):
    for item in nameList:
        index = random.randint(0, len(nameList) - 1)
        nn = nameList[index]
        item[1] = nn[1]
        print(item)


if __name__ == '__main__':
    myName = ["Avijit Samanta", "Antik Mondal", "Ramij Ahamed Mistry"]
    changeName(getFirstLastName(myName))

