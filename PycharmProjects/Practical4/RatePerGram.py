weight = float(input('Enter your weight:'))
postage = 0
if weight <= 20:
    postage = 0.3 * weight
elif 20 < weight <= 40:
    postage = 0.6 * weight
elif 40 < weight <= 100:
    postage = 0.9 * weight
elif weight > 100:
    postage = 1.15 * weight

print ('Your total postage charge for your parcel is:', postage)
