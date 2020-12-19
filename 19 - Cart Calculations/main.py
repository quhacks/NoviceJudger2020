import sys

prices = {} #this is a dictionary; it's a list with labels instead of indices
cost = 0

products = sys.stdin.readline()
for i in range(int(products)):
    product, price = sys.stdin.readline().split()
    prices[product] = int(price) #sets the price of each product in the dictionary

cart = sys.stdin.readline()
for i in range(int(cart)):
    product, quantity = sys.stdin.readline().split()
    cost += prices[product] * int(quantity) #cost = price * quantity

print(cost)