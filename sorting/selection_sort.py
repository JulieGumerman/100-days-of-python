# The purpose of this function is to find the smallest item in an array.
def find_smallest(arr):
    smallest = arr[0]
    # The variable "smallest" stores the smallest value itself.
    # It starts at the beginning of the array as the default.

    smallest_index = 0

    # The variable "smallest_index" stores the index of the smallest value.
    # Just like with the variable "smallest," we're starting at the beginning of the array, hence the initial value of 0.

    for i in range(1, len(arr)):
    # This for loop checks each item in the array.
    # The "i" refers to the index of the array, starting with the first entry and ending at the last.
        if arr[i] < smallest:
            # So far, the "smallest" variable records the smallest number the "for" loop has seen so far in the array.
            # If the next number is smaller, the "smallest" variable value is overwritten by the new smallest number.
            # If the next number is NOT smaller, you move on.
            smallest = arr[i]
            smallest_index = i
    # By the time all is said and done, we'll know the smallest item in the array.
    return smallest_index

# Ok. Now that we can find the smallest number's index, let's sort this array
def selection_sort(arr):
    new_arr = [] # The variable "new_arr" stores the array in its properly sorted state
    for i in range (len(arr)):
        # We go through the array, invoking the "find_smallest" function to find the smallest element in the array

        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
            # The append method puts that smallest number at the end of the array stored as "new_arr".
            # Meanwhile, we are removing the smallest item from the old array as we find it.
            # Next time the for loop runs, it has fewer results to search through, and it can continue to find the next smallest item.
    return new_arr

my_array = [5,3,6,2,10]
print(selection_sort(my_array))

