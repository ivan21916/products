import os

# check and read file
products = []
if os.path.isfile('products.csv'):
	print('file found')
	with open('products.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if 'item,price' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
else:
	print('can not found the file')

# let user input the items and price
while True:
	name = input('Please enter the name of product(enter \'q\' to quit): ')
	if name == 'q':
		break
	price = input('Please enter the price of product (dollar): ')
	products.append([name, price])
print(products)

#print all items and price
for p in products:
	print('The price of', p[0], 'is', p[1], 'dollars')

#export file as csv
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('item,price\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')