import os

def read_file(filename):
	products = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			if 'item,price' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	return products

# let user input the items and price
def user_input(products):
	while True:
		name = input('Please enter the name of product(enter \'q\' to quit): ')
		if name == 'q':
			break
		price = input('Please enter the price of product (dollar): ')
		products.append([name, price])
	print(products)
	return products

#print all items and price
def print_products(products):
	for p in products:
		print('The price of', p[0], 'is', p[1], 'dollars')

#export file as csv
def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f:
		f.write('item,price\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename): # check and read file
		print('file found')
		products = read_file(filename)
	else:
		print('can not found the file')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()