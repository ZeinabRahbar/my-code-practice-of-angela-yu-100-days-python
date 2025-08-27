student_scores = input("Input a list of student scores:").split()

print(f"max score is {max(student_scores)}!!!")

maximum = 0
for n in range(0, len(student_scores)):
    student_scores[n] = int( student_scores[n])
    if student_scores[n] > maximum:
        maximum = student_scores[n]
    
print(f"max score is {maximum}!!!")
