height = float(input('Enter you height(m):'))

min_weight = float(18.5 * height **2)
max_weight = float(22.9 * height **2)
weight = 0
print ('Your ideal weight range is %.1f - %.1f.' % (min_weight, max_weight))
