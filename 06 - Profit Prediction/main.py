import sys

fabric, needed, price = sys.stdin.readlines()
masks = int(fabric) // int(needed) #the operator // divides and rounds down
print(int(masks) * int(price)) #revenue = number of masks * price of mask