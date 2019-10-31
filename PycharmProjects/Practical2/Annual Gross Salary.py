og_salary = input ('Enter in your original annual salary: ')
og_monthly_salary =  float(og_salary) / 12
cpf = float(og_monthly_salary / 5)
net_deduction = float(cpf + 1500)
net_salary = float(og_monthly_salary - net_deduction)

print("Net monthly take-home salary: $%.2f " % net_salary)


