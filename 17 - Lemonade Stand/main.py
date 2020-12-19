import sys

grapes = sys.stdin.readline()

if int(grapes) % 4 == 0:
    print('Greg') #Greg only wins if grapes are a multiple of four on Freddy's first turn
    print((int(grapes) // 4) * 2) #it takes two turns to reduce the number of grapes by four
else:
    print('Freddy') #otherwise, Freddy can make the grapes a multiple of four on Greg's first turn
    print(1 + (int(grapes) // 4) * 2) #it takes one turn for freddy to do that