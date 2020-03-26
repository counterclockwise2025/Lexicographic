'''
Samip Vaidh
3/31/20
Knights Tour
'''

#create a hash map for getting the number of lines and words from the input file
#dictonary to store the words/characters
words_hash = {}
#opening the file and assigning it to the read word variable and once it is finised the variable gets disposed
with open("lexi.txt", "r") as read_word:
    #looping through the file starting at the first line to take each word from the file
    for line in read_word:
        #create a variable to store the appened letters and spaces that are created by the loop
        other_line = ''
        #read each individual character of line and replace special characters with spaces into the other_line variable
        for index in range(len(line)):
            #if a '#' is found between words then the statement is broken and left off there and the other_line variable is used from that point on
            if line[index] == '#':
                break
            #if not within the series of characters and space at the end then it will add a space to the other_line variable
            if line[index].upper() not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ':
                other_line += ' '
            #if the character is a space or a letter then append to the other_line variable
            else:
                other_line += line[index]
        #create a words array with whatever other_line has store in itself and look for a 'nn' condition and split the line apart
        other_line = other_line.replace('nn', ' ').split()

        #loop through the other_line array
        for word in other_line:
            #will only keep the first 10 characters of the word
            short_word = word[:10] 
            #finds the key if the word has been seen before and adds a value of 1
            if short_word in words_hash.keys():
                words_hash[short_word] += 1
            #if the key is not found then it will assign that word as new a new key and map that to the value 1
            else:
                words_hash[short_word] = 1

#print the key and values for each word in the map
for key in words_hash.keys():
    print ('{}: {}'.format(key, words_hash[key]))

#place words into a binary tree
#create a node for the BST
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

#inseting a new node
def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

#traverse the tree in order
def in_order(root):
    if root:
        in_order(root.left)
        print(root.val)
        in_order(root.right)

