#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
def biggie_size(lst):
    for i in range(0,len(lst)):
        if(lst[i] > 0):
            lst[i] = "big"
    return lst
print(biggie_size([-1, 3, 5, -5]))

#Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values.
def count_positives(lst):
    count = 0
    for val in lst:
        if( val > 0):
            count+= 1
    lst[len(lst) - 1] = count
    return lst
print(count_positives([-1,1,1,1]))

#Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
def sum_total(lst):
    sum = 0
    for val in lst:
        sum+= val
    return sum
print(sum_total([1,2,3,4]))

#Create a function that takes a list and returns the average of all the values
def avarage(lst):
    sum = 0
    for val in lst:
        sum+= val
    return sum/len(lst)
print(avarage([1,2,3,4]))

#Length - Create a function that takes a list and returns the length of the list.
def length(lst):
    return len(lst)
print(length([]))

#Minimum - Create a function that takes a list of numbers and returns the minimum value in the list.
#  If the list is empty, have the function return False.
def minimum(lst):
    if(len(lst) == 0):
        return False
    min = lst[0]
    for val in lst:
        if val < min:
            min = val
    return min
print(minimum([]))

#Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
def maximum(lst):
    if(len(lst) == 0):
        return False
    max = lst[0]
    for val in lst:
        if val > max:
            max = val
    return max
print(maximum([37,2,1,-9]))

#Ultimate Analysis - Create a function that takes a list and returns a dictionary that has 
# the sumTotal, average, minimum, maximum and length of the list.
def ultimate_analysis(lst):
    sumTotal = 0
    minimum = lst[0]
    maximum = lst[0]
    for val in lst:
        if( val > maximum):
            maximum = val
        if(val < minimum):
            minimum = val
        sumTotal+= val
    dict_lst = {
        'sumTotal': sumTotal,
        'average': sumTotal/len(lst),
        'minimum': minimum, 
        'maximum': maximum, 
        'length': len(lst)
    }
    return dict_lst
print(ultimate_analysis([37,2,1,-9]))

#Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list.
def reverse_list(lst):
    for i in range(0, (len(lst)//2)):
        temp = lst[i]
        lst[i] = lst[len(lst) - i - 1]
        lst[len(lst) - i - 1] = temp
    return lst
print(reverse_list([37,2,1,-9]))