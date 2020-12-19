import sys

words = sys.stdin.readline().split()

for i in range(len(words)): #loop over the sentence's words
    
    for j in range(len(words[i])): #loop over the word's characters
        if words[i][j] in 'aeiou': #checks if vowel
            break #stops the loop, preserving the value of j
    
    suffix = words[i][:j] or 'w' #gets the first j characters (or 'w' if j is 0)
    remainder = words[i][j:] #gets the characters after j
    words[i] = remainder + suffix + 'ack' #modifies the word
    
print(' '.join(words)) #prints the words separated by a space