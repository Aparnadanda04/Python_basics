a = 5
print(type(a))

b = 'aparna'
print(type(b))

c = 3.5
print(type(c))


c = 3 + 4j 
print("The type of c: ", type(c))
print("c is complex number: ", isinstance(3 + 4j, complex))

hello = 9
world = 'world'
print('%d' % hello)
#hw = hello + ' ' + world  # string concatenation in python
#print(hw) 

#dictionary
dict = {'fruit' : 'apple','animal' : 'monkey','age' : 20}
dict['name']='Appu'
print(dict)
print(dict['fruit'])

print('animal' in dict)
del dict['name']
print(dict.get('name','N/A'))

#loop in dict


di = {'k':'kalyan','t':'thane','p':'pune'}
for i in di:
    a = di[i]
    print('{} is in Maharashtra'.format(a))

#set
s = {'apple','banana','grapes','grapes'}
s.add('chikoo')
print(s)

#frozen set
l = {'apple','banana','grapes','grapes'}
z=frozenset(l)
print(z)
print(len(z))
print(z)
print(len(z))

# For Loop over Set data type in Python 

animals = {'cat', 'dog', 'leopard'} 
for id, animal in enumerate(animals):
    print('%d: %s' % (id + 1, animal))

    


