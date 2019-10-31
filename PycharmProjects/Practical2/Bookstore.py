unit_price = input('Enter the unit price of the book: ')
quantity = input('Enter the quantity of the books: ')

sub_total = float(unit_price) * int(quantity)
gst = 0.07 * sub_total
total = sub_total + gst

print('Subtotal: $%.2f ' % (sub_total))
print('GST: $%.2f ' % (gst))
print('Total: $%.2f ' % (total))
