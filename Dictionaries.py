
# coding: utf-8

# # Dictionaries
# - Along with lists, dictionaries are one of the most flexible built-in data types in Python.
# - If you think of lists as ordered collections of objects, you can think of dictionaries as unordered collections;
# - The chief distinction is that in dictionaries, items are sorted and fetched by key, instead of by positional offset
# - Accessed by key, not offset position
# - Unordered collections of arbitrary objects
# - Variable-length, heterogeneous, and arbitrarily nestable
# - Tables of objects references (hash tables)

# ### Define a dictionary

# In[2]:

D = {} # empty dictionary
print(type(D))
D = dict()
print(type(D))


# In[6]:

# 1) Two-item dictionary
D = {'name': 'Bob', 'age':40}
print(D)


# In[8]:

# 2) Another way
D = dict(name='Bob', age=40, address='Hel')
print(D)


# In[9]:

# 3) Another way, key and value pairs in list
D = dict([('name', 'Bob'), ('age', 40), ('address', 'Hel')])
print(D)


# In[10]:

# 4) Another way, keylists and value lists by zip
keylists = ['name', 'age', 'address']
valuelists = ['Bob', 40, 'Hel']
print(zip(keylists, valuelists))
D = dict(zip(keylists, valuelists))
print(D)


# In[11]:

# 5) Another way, using comprhensions
D = {key:value for key, value in zip(keylists, valuelists)}
print(D)


# In[17]:

# Access the items in dictionary
D['name'] = ['Bob', 'Roger']
name = D['name']
age = D['age']
print(name, age)


# In[21]:

E = {'cto': {'name': 'Bob', 'age': 40, 'address':{'weekday': 'Hel', 'weekend': 'Espoo'}}} # Nesting
# print cto age
print(E['cto']['age'])
print(E['cto']['address']['weekend'])


# ### Dictionary Methods

# In[12]:

# Find all built-in methods exist for a dictionary data-type
D = {}
dir(D)


# In[26]:

# Get all keys
D = {'name':'Bob', 'age': 40}
print(D.keys())


# In[14]:

# Get all values
print(D.values())


# In[15]:

# Get all items
print(D.items())


# In[27]:

# Copy items to new dictionary
E = D.copy()
print(D)
print(E)


# In[28]:

# Remove all items
D.clear()
print(D)
print(E)


# In[30]:

# Merge by keys
D1 = {'name':'Bob', 'age': 40}
D2 = {'work': 'IT', 'city': 'Hel', 'name':'Daad'}
D1.update(D2)
print(D1)


# In[36]:

# Fetch by key, if absent defalut (or None)
D = {'name': 'Bob', 'age': 40}
print(D.get('name', None))
print(D.get('name1')) # by default None returns if the key is absent
print(D.get('name1', 'The entered key Not exist')) # you can change the default


# In[37]:

# Remove by key, if absent default (or Error)
print(D.pop('name')) # return only value
print(D)
if D.get('name1'):
    D.pop('name1')
else:
    print('entered Key not exist')


# In[55]:

# Remove and return any (key, value) pair;
D = {'name': 'Bob', 'abc': 43, 'age': 40}
print(D.popitem())
print(D)


# In[59]:

D = {'name': 'Bob', 'age': 40}
print(D.setdefault('name')) # fetch by key if absent set default (or None)
print(D.setdefault('name1', 'Yet to assign')) # default None
print(D)
D['name1']= 'roger'
print(D)


# In[40]:

D = {'name': 'Bob', 'age': 40}
# Length: number of stored entries
print(len(D))


# In[41]:

# Adding/changing keys
D['age'] = 42
D['work'] = 'IT'
print(D)


# In[54]:

# Dictionary comprehensions
D = {x: x**2 for x in range(10)}
print(D)


# In[56]:

# Example: Movie Database
table = {'1975': 'Holy Grail',
         '1979': 'Life of Brain',
         '1983': 'The Meaning of Life'} # Key: value
print(table)


# In[57]:

# print the movies by year
for year in table:
    print(year + '\t' + table[year])


# In[58]:

# Mapping values to keys
table = {value:key for key, value in table.items()}
print(table)


# In[61]:

for title in table:
    print(title + '\t' + table[title])


# In[66]:

# What are the movies released in 1975?
print([title for (title, year) in table.items() if year == '1975'])


# ### Dictionary usage notes
# - Sequence operations don't work: Dictionaries are mappings, not sequences. Thus, no concatenation and slicing (python raises an error)
# - Assigining to new indexes adds entries
# - keys need not always be strings: Mutable objects such as lists, sets, and other dictionaries don't work as keys, but are allowed as values.

# In[67]:

# some examples: Nested dict
rec = {'name': 'Bob',
       'jobs': ['developer', 'manager'],
       'web': 'www.bobs.org/Bob',
       'home': {'state': 'Overworked', 'zip': 12345}}
print(rec)


# In[69]:

print(rec['name'])
print(rec['jobs'])
print(rec['jobs'][1])
print(rec['home']['zip'])


# In[70]:

# Why you will care: Dictionaries versus Lists
L = ['Bob', 40, ['dev', 'mgr']] # List-based record
# print name
print(L[0])
# print jobs
print(L[2])


# In[71]:

D = {'name': 'Bob', 'age': 40, 'jobs': ['dev', 'mgr']}
# print name
print(D['name'])
# print jobs
print(D['jobs'])
# Another way of defining dict which may seem even more readable to some human readers:
D = dict(name='Bob', age=40, jobs=['dev', 'mgr'])
print(D)
# remove manager job from job list
D['jobs'].remove('mgr')
print(D)


# In[ ]:



