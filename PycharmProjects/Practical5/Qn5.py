gpa = 0
total_grade_point = 0
total_credit = 0
for i in range(1, 6):
    credit = int(input("Enter the credit for Module: " + str(i) + ": "))
    module_gpa = float(input("Enter your GPA for Module: " + str(i) + ": "))
    grade_point = credit * module_gpa
    total_grade_point += grade_point
    total_credit += credit
gpa = total_credit / total_grade_point
print("Your cumulative GPA for 5 modules are", gpa)
