products = []
while True:
	name = input('Please enter the name of product: ')
	if name == 'q':
		break
	price = input('Please enter the price of product: ')
	products.append([name, price])
print(products)