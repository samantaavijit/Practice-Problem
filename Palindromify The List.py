"""Problem Statement:- You are given a list that contains some numbers. You have to print a list of next palindromes
only if the number is greater than 10; otherwise, you will print that number.

Input:
[1, 6, 87, 43]

Output:
[1, 6, 88, 44]
"""


def is_palindrome(num):
    return str(num) == str(num)[::-1]


def next_palindrome(num):
    while not is_palindrome(num):
        num += 1
    return num


def palindrome_list(p_list):
    res_l = []
    for item in p_list:
        if item > 10:
            res_l.append(next_palindrome(item))
        else:
            res_l.append(item)
    return res_l


if __name__ == '__main__':
    n = int(input("Enter the limit "))
    my_list = []
    for i in range(n):
        my_list.append(int(input("Enter value ")))
    print(palindrome_list(my_list))
    print(f"One Line Execution {[item if item < 10 else next_palindrome(item) for item in my_list]}")
