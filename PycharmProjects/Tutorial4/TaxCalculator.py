income = int(input('Enter your income:'))
status = input('Enter your marital status:(S/M)')
tax = 0
if status == 'M':
    if income > 64000:
        tax = 6400 + (income -64000) * 0.25
    else:
        tax = income * 0.1
else:
    if income > 32000:
        tax = 3200 + (income - 32000) * 0.25
    else:
        tax = income * 0.1
print ('Your taxable income is:', tax)
