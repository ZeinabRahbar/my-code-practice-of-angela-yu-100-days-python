student_heights = input("Input a list of student heights:").split()
whole_height = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int( student_heights[n]) 
    whole_height +=  student_heights[n]
    
print(f"Their average height is {round(whole_height/ len(student_heights))}")

total_height = sum(student_heights)
avg = round(sum(student_heights) / len(student_heights))
print("Their average height is", avg)
