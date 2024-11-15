#the purpose of this function is to find the smallest item in an array
def find_smallest(arr):
    smallest = arr[0]
    #the variable "smallest" stores the smallest value itself
    # it starts at the beginning of the array as the default

    smallest_index = 0

    #the variable "smallest_index" stores the index of the smallest value
    #just like with "smallest," we're starting at the beginning of the array, hence the initial value of 0

    for i in range(1, len(arr)):
    # this for loop checks each item in the array
    # "i" refers to the index of the array, starting with the first entry and ending at the last
        if arr[i] < smallest:
            #so far, the "smallest" variable records the smallest number the "for" loop has seen so far in the array
            #if the next number is smaller, the "smallest" variable value is overwritten by the new smallest number
            #if the next number is NOT smaller, you move on
            smallest = arr[i]
            smallest_index = i
    #by the time all is said and done, we'll know the smallest item in the array
    return smallest_index


    
