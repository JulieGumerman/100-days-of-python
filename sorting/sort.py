number_array = [5,4,8,7,2,1,9,3,0,6]

sorted = []

for num in number_array:
    if sorted == []:
        sorted.append(num)
    if sorted != []:
        for num_sort in sorted:
            print(num)
            sorted.insert(0,num)
            print(sorted)
    #         if num_sort > num or num_sort == num:
    #             sorted.insert(sorted.index(num_sort),num)
    #         if sorted.index(num_sort) == (len(number_array)-1):
    #             sorted.insert(len(sorted), num)

print(sorted)
    #pull num from in array; set as variable
    #run number by each other number in sorted array
    #if smaller than num[0], put at beginning
    #if bigger than than num[0], run through nums and find which ones it squeezes between
    #if larger than last num in sorted, drop at end