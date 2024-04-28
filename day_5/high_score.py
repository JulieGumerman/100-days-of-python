student_scores = input().split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

high_score = 0
for n in range(0, len(student_scores)):
    if high_score < student_scores[n]:
        high_score = student_scores[n]

if high_score <= 0:
    print(f"These students have anti-student test scores. The highest score was {high_score}!")
else:
    print(f"The highest score is {high_score}")