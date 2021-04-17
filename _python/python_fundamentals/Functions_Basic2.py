#Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number down to 0
def Countdown(num):
    list = []
    for i in range(num,-1,-1):
        list.append(i)
    return list
print(Countdown(5))

#Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
def print_and_return(num1, num2):
    print (num1)
    return num2
print(print_and_return(1,2))

# First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
def first_plus_length(li):
    return len(li) + 1
print(first_plus_length([1,2,3,4,5]))

#Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values
# Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
#  from the original list that are greater than its 2nd value. 
def values_grater_than_second(li):
    lis = []
    second = li[1]
    for x in li:
        if x > second:
            lis.append(x)
    return lis
print(values_grater_than_second([5,2,3,2,1,4]))

#his Length, That Value - Write a function that accepts two integers as parameters: size and value.
#  The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
def length_and_value(size, val):
    lis = []
    i = size
    while(i > 0):
        lis.append(val)
        i -= 1
    return lis
print(length_and_value(4,7))

