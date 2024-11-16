number_array = [5,4,8,7,2,1,9,3,0,6]

sorted = []

for i in range(len(number_array)):
    if sorted == []:
        sorted.append(number_array.pop(0))
    if sorted != []:
        

print(sorted)
print(number_array)
    #pull num from in array; set as variable
    #run number by each other number in sorted array
    #if smaller than num[0], put at beginning
    #if bigger than than num[0], run through nums and find which ones it squeezes between
    #if larger than last num in sorted, drop at end