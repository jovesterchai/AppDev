name = input ('Enter yout name: ')
admin_no = input ('Enter admin number: ')
age = int (input ('Enter age: '))
gender = input ('Enter gender (Male / Female): ')
weight = float (input ('Enter weight (kg): '))
height = float (input ('Enter height (m): '))

bmi = float (weight / (height ** 2))

print ('Hello! %s' % name)
print ('Your admin no is %s and age is %s' % (admin_no, age))
print ('Your gender is %s and bmi is %.2f' % (gender, bmi))
