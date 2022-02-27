# declare empty list for the cart
cart = []

print('\nWelcome to our shop\n') #greeting text

cartSize = input('How many items are you buying ?  ')
userChoice = input('what item do you wish to buy ?  ')

#add the item to cart
items_added = cart.append(userChoice)

# keep count of  items in cart
total_items = len(cart) 

# keep demanding for items till cart is filled
while total_items < int(cartSize) :
	userChoice = input('add another item:  ')
	cart.append(userChoice)
	total_items = total_items + 1
	
print('\n'*2) #just a negative space

lineRule = '_'*25 #for decoration
print(lineRule)

# reciept title 
print('Items Added To Cart\n' +lineRule + '\n')


show_items = 0
item_number = 1 #for enumeration
items_in_cart = len(cart)
while show_items < items_in_cart:
	print(str(item_number)+'. '+cart[show_items])
	show_items = show_items + 1
	item_number = item_number + 1
	
