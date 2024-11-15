import math

def binary_search(list, item):
    low = 0
    high = len(list)-1

    # variables "low" and "high" mark the ends of the array being searched
    # the number searched for is HIGHER array[low] and lower than array[high]
    # as we target the MIDDLE INDEX of the array, the low index and high index start to shift

    while low <= high:
        mid = math.floor((low+high)/2) #this is that MIDDLE INDEX
        #Please note: mid is the INDEX, not the number being searched for (in this case, the variable "item"
        guess = list[mid] # in other words, is the item at the middle index equal to the item being looked for?
        if guess == item:
            return mid # game over: you landed on the number being searched for. Lucky you. #returns the index
        if guess > item:
            high = mid - 1 # ARRAY[mid] was higher than the item you are looking for
            #changes "high" to the LOWER HALF of the array in question
        if guess < item:
            low = mid + 1 #ARRAY[mid] was LOWER than the item you are looking for
            #changes "low" to the HIGHER HALF of the array in question
    return None #you went through the entire array and the number is not there

my_list = [1,3,5,7,9]

print(binary_search(my_list, 3))