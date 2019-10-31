try:
    weight = float(input('Enter your weight(kg):'))
    height = float(input('Enter you height(m):'))

    bmi = float(weight / height ** 2)
    clas = ''
    if bmi >= 27.5:
        clas = 'obesity'
    elif 23 <= bmi < 27.5:
        clas = 'overweight'
    elif 18.5 <= bmi < 23:
        clas = 'normal weight'
    else:
        clas = 'underweight'
    print('your BMI is %.2f and you are %s.' % (bmi, clas))
except ValueError:
    print('Your value is invalid.')
