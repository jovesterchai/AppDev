total_s = int(input('Enter time in seconds: '))
hr = total_s // 3600
x = total_s % 3600
min = x // 60
s = x % 60

#7384 seconds is 2 hours 3 minutes and 4 seconds
print('%i seconds is %i hours, %i minutes and %i seconds' % (total_s, hr, min, s))
