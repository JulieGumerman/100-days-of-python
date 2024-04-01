# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
average = 0
length = 0
for n in student_heights:
    average += n
    length += 1

print("average", average/length)