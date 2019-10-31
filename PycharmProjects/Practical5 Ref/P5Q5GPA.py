final_gpa=0
total_credit=0
for i in range(1,6):
    credit=float(input("Enter the credit for Module %s:"%i))
    gpa=float(input("Enter the GPA for Module %s:"%i))
    final_gpa+=credit*gpa
    total_credit+=credit
print("Your cumulative GPA for 5 modules are ",final_gpa/total_credit)
