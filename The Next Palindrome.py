"""
Problem Statement:-
A palindrome is a string that, when reversed, is equal to itself. Example of the palindrome includes:
676, 616, mom, 100001.
You have to take a number as an input from the user. You have to find the next palindrome corresponding to that
number. Your first input should be the number of test cases and then take all the cases as input from the user.

Input:
3

451
10
2133

Output:
Next palindrome for 451 is 454
Next palindrome for 10 is 11
Next palindrome for 2133 is 2222
"""


def isPalindrome(num):
    return str(num) == str(num)[::-1]


def nextPalindrome(num):
    while not isPalindrome(num):
        num += 1
    return num


if __name__ == '__main__':
    n = int(input("Enter the limit "))
    my_list = []
    for i in range(n):
        my_list.append(int(input("Enter the value that you want to find the next palindrome ")))
    for i in range(n):
        print(f"Next palindrome for {my_list[i]} is {nextPalindrome(my_list[i])}")
