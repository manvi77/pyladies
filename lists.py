
# coding: utf-8

# # Lists
# - Flexible ordered collection object type
# - Mutable objects (can be changed in place)
# 

# In[6]:

s = ''
a = 'welcome'
print(a[4])
print(type(a))
b = 10
print(type(b))


# In[7]:

# Define an empty list
L = []
# How to know the data type of an item?
print(type(L))

L = list()
print(type(L))


# In[8]:

# List with four items:
# Can you tell datatypes of items in the list?
L = [123, 'abc', 1.23, {}]

# print some elements
print(L[0])

# print the length of list
print(len(L))

# print fourth element
print(L[3]) # Index start from 0

# print last element 
print(L[len(L) - 1])

# print the last element with out using len
print(L[-1])


# In[9]:

# Nested sublists
L = ['Bob', 40.0, ['dev', 'mgr']]
print(L)


# In[12]:

# How to a list from a given string?
s = 'pyladies'

L = list(s)
print(L)
# tell the length of string

# Strings in python are immutable: we can not change a string
# How can we change string using lists?
L[0] = 'i'
print(L)
s = ''.join(L)
print(s)


# In[18]:

# Make a list of 'n' numbers
n = 10
L = list(range(0,n)) # Do you know how the range works?
print(L)


# In[22]:

# Slice the list from an index 'i' to an index 'j'
i = 2
j = 5
a = L[i:j] # 'j' is exclusive

# what will be the datatype of 'a'
print(a, type(a))
# what happens when index 'j' exceeds the length of the list?
j = 12
print(L[i:j]) # https://stackoverflow.com/questions/9490058/why-substring-slicing-index-out-of-range-works-in-python
# print(L[j]) # IndexError


# In[25]:

# Concatenate
L1 = ['A', 'B', 'C']
L2 = [1, 2, 3]
L3 = L1 + L2
print(L3)

# Repeat elements in L3 by 2 times
L4 = L3 * 4
print(L3)
print(L4)


# In[26]:

# Iteration: Iterate through all elements in list
for x in L4:
    print(x)


# In[28]:

# List datatype has many in-built methods which makes our life a bit simpler
# How to know all the in-built methods exist for the list datatype
dir(L)

# Most of these methods are intutive to guess

# L.append()
# L.count()
# L.extend()
# L.index()
# L.insert()
# L.pop()
# L.remove()
# L.reverse()
# L.sort()

# How to add a new element to a given existing list
L = [1, 2, 3]

# add element 4 to the list L
L.append(4)
# 1, 2, 3, 4

# we can extend the list by another list 
L1 = [1, 2, 3]
L2 = ['a'] * 4 # ['a', 'a', 'a', 'a']

L1.extend(L2)
print(L1) # [1, 2, 3, 'a', 'a', 'a', 'a']
# L1 = L1 + L2 

# What is the difference between append and extend
L1 = [1, 2, 3]
L2 = ['a'] * 4
L1.append(L2)
print(L1)

# Try to understand what other methods does on the list
L = [1, 1, 2, 3, 3, 4]
print(L.count(2)) # count how many times the given element exist in list
print(L.count(1)) # count the element exist in list 


# In[34]:

# Exercises
# 1) Define a list of numbers from 1 to 5?
L = list(range(1, 5)) 
# or 
L = [1, 2, 3, 4, 5]

# 2) Find the length of list?
print(len(L))

# 3) Concatenate multiple lists?
L1 = [1, 2, 3]
L2 = [4, 5, 6]
L3 = L1 + L2
print(L3)
# or
# L1.extend(L2)
print(L1.extend(L2))
print(L1)
# 4) Repeat the lists?
L1 = [1]*4


# In[54]:

#  List comprehensions and map
res = []
for c in 'SPAM':
    res.append(c*4)

# List comprehension equivalent
res = [c * 4 for c in 'SPAM']

L = [x**2 for x in range(5)]
print(L)

# Map a function across a sequence
# apply absolute function on every elemenet in list
list(map(abs, [-2, -1, 0, 1, 2]))

# find unicode value of each character in a string
list(map(ord, 'spam'))


# In[ ]:

## Indexing
L = ['spam', 'Spam', 'SPAM!']
print(L[2]) # Offsets start at zero

# Negative: count from the right
print(L[-2])

## Slicing
# Slicing fetches sections
print(L[1:])

## Matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # 3 x 3 two-dimensional list-based array
print(matrx[1]) # one index, you get an entire row
print(matrix[1][1]) # two, you get an item within the row
matrix[2][0] # Guess??


# In[ ]:

## Changing Lists in Place
L = ['spam', 'Spam', 'SPAM!']
# change index 1 to 'eggs'
L[1] = 'eggs' # Index assignment
print(L)

# Slice assignment: delete + insert
L[0:2] = ['eat', 'more']
print(L)

L = [1, 2, 3]

# Replacement + insert
L[1:2] = [4, 5] # replacing one element with two elements
print(L)

# Insertion (replace nothing)
L[1:1] = [6, 7]
print(L)

# Deletion (insert nothing)
L[1:2] = []
print(L)

L = [1]
# Insert all at :0, an empty slice at front
L[:0] = [2, 3, 4]
print(L)
# Insert all at len(L):, an empty slice at end
L[len(L):] = [5, 6, 7]
print(L)
# Insert all at end, named method
L.extend([8, 9, 10])
print(L)


# In[57]:

# List method calls
L = ['eat', 'more', 'SPAM!']
L.append('please') # Append method call: add item at end
print(L)

# Unlike '+' concatenation, append doesn't have to generate new objects, so it's usually faster than '+' too.

# Sort list items
L.sort() # 
print(L) # ('S' < 'e')

# Sort with mixed case
L = ['abc', 'ABD', 'aBe']
L.sort() 
print(L) # by default it sorts by captial letters

# sort by lower case 
L.sort(key=str.lower, reverse=True) # Change sort order
print(L)

# Sorting built-in
sorted(L, key=str.lower, reverse=True)

# Pretransform items: different
sorted([x.lower() for x in L], reverse=True)


# In[61]:

# Other common list methods
L = [1, 2]
L.extend([3, 4, 5]) # Add many items at end (like in-place '+')
print(L)

# Delete and return last item (by default: -1)
L.pop() # 5
print(L)

# In-place reversal method
L.reverse()
print(L)
# Reversal built-in with a result (iterator)
list(reversed(L))


# In[ ]:

L = []
# Push onto stack, LIFO (Last In First Out)
L.append(1)
print(L)
L.append(2)
print(L)

# Pop off stack
L.pop() # 2
print(L)


# In[ ]:

L = ['spam', 'eggs', 'ham']
# Index of an object (search/find)
L.index('eggs') # 1
# Insert at position
L.insert(1, 'toast')
print(L)
# Delete by value
L.remove('eggs')
print(L)
# Delete by position
L.pop(1) # 'toast'
print(L)
# Number of occurences
L.count('spam') # 1


# In[62]:

L = ['spam', 'eggs', 'ham', 'toast']
# Delete one item
del L[0]
print(L)
# Delete an entire section
del L[1:] # same as L[1:] = []
print(L)

