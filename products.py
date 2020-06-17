products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q': # q = quit
		break
	price = input('請輸入商品價格: ')
	products.append([name, price])
print(products)

print(products[0][0])
print(products[1][1])

for p in products:
	print(p[0], '的價格是', p[1])

with open('products.csv', 'w') as f:
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
