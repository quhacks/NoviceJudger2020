import sys

a, b = sys.stdin.readline().split()

for i in range(int(a), int(b)): #includes a but not b
    number = ''
    if i % 3 == 0: #the operator % is modulo (or remainder)
        number += 'Quack'
    if i % 5 == 0: #if the remainder is 0, it is divisible
        number += 'Hack'
    if number == '': #if number wasn't divisble by either
        number = i
    print(number)
