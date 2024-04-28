student_scores = input().split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

high_score = 0
for score in student_scores:
    if high_score < score:
        high_score = score

if high_score <= 0:
    print(f"These students have anti-student test scores. The highest score was {high_score}!")
else:
    print(f"The highest score is {high_score}")