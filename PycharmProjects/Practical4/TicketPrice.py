age = int(input('Enter your age:'))
day = int(input('Enter the Day of the Week(In numbers):'))
price = 0
if age < 4 or age >130:
    print('Invalid Age')
else:
    if day < 6:
        membership = input('Enter your membership (C: Corporate, F: Family, N: No membership):')
        if age <16:
            if membership.lower() == 'f':
                price = 0
            else:
                price = 7.5
        elif age >= 16 and age < 65 :
                price = 10
        else:
            if membership.lower() == 'c':
                price = price *0.8
    else:
        price = 10
    print ('You have to pay $%.2f for the ticket.' % (price))












