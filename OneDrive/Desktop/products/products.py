products = []
while True:
	name = input('Please enter the name of product: ')
	if name == 'q':
		break
	price = input('Please enter the price of product (dollar): ')
	products.append([name, price])
print(products)

for p in products:
	print('The price of', p[0], 'is', p[1], 'dollars')