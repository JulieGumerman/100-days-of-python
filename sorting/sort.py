number_array = [5,4,8,7,2,1,9,3,0,6]

sorted = []

for num in number_array:
    if sorted == []:
        sorted.append(num)
    elif len(sorted) == 1:
        if num > sorted[0]:
            sorted.insert(1,num)
        elif num == sorted[0]:
            sorted.insert(0,num)
        elif sorted[0] > num:
            sorted.insert(0,num)
    else:
        for num_sort in sorted:
            if num_sort > num:
                sorted.insert(sorted.index(num_sort),num)
            if num_sort.index(num_sort) == len(num_sort - 1) 


    #pull num from in array; set as variable
    #run number by each other number in sorted array
    #if smaller than num[0], put at beginning
    #if bigger than than num[0], run through nums and find which ones it squeezes between
    #if larger than last num in sorted, drop at end