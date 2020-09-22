"""
Problem Statement:- You visited a restaurant called CodeWithHarry, and the food items in that restaurant are
sorted, based on their amount of calories. You have to reserve this list of food items containing calories.
You have to use the following three methods to reserve a list:

Inbuilt method of python
List name [::-1] slicing trick
Swapping the first element with the last one and second element with second last one and so on like,
[6 7 8 34 5] -> [5 34 8 7 6]

Input:
Take a list as an input from the user
[5, 4, 1]

Output:
[1, 4, 5]
[1, 4, 5]
[1, 4, 5]

All three methods give the same results!
"""

if __name__ == '__main__':
    try:
        my_list = []
        size = int(input("Enter the size of list "))
        for i in range(size):
            my_list.append(int(input("Enter the value ")))

        print(f"Original list is {my_list}")
        reverse1 = my_list.copy()
        reverse2 = my_list[::-1]
        reverse3 = my_list.copy()
        reverse4 = my_list[:]
        reverse1.reverse()
        print(f"Reverse using reverse() {reverse1}")
        print(f"Reverse using [::-1] {reverse2}")

        i = 0
        j = size - 1
        while i < j:
            temp = reverse3[i]
            reverse3[i] = reverse3[j]
            reverse3[j] = temp
            i += 1
            j -= 1
        print(f"Reverse using Two pointer algorithm(while) {reverse3}")
        for i in range(len(reverse4) // 2):
            reverse4[i], reverse4[len(reverse4) - i - 1] = reverse4[len(reverse4) - i - 1], reverse4[i]

        print(f"Reverse using for loop {reverse4}")
        if reverse1 == reverse2 and reverse2 == reverse3 and reverse3 == reverse4:
            print("All methods give the same results!")
    except ValueError:
        print("Please enter valid input")
    except Exception as e:
        print(e)
