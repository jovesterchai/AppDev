current_price = float(input('Enter current price for ABC Corporation (S$): '))
cost = 0.4 * 2000
comission_cost = 0.03 * cost

selling = current_price * 2000
comission_selling = 0.02 * selling

total = comission_cost + comission_selling

profit = selling - cost - total

print('You paid total comission of (S$): %.2f' %total)
print('You have made a profit of (S%): ', profit)
