import sys

height, width = sys.stdin.readline().split()
matrix = sys.stdin.readlines()
rows = cols = 0 #number of empty rows and columns

#counts all of the empty rows
for row in matrix:
    if '1' not in row: #a row is empty if there are no 1's
        rows += 1

#iterating over columns is a little harder
for col in range(int(width)):
    empty = True #first, we assume it's empty
    for row in matrix: #then we loop over every row
        if row[col] == '1': #if there's a 1, the column isn't empty
            empty = False #we can stop searching now 
            break
    
    if empty: #if we found no 1's, then it's an empty column
        cols += 1

print(max(rows, cols)) #a fabric can fix 1 empty row and 1 empty column simultaneously