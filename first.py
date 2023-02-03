a = 10
print (a)

a = 10 
print("The type of a: ", type(a))

b = 40.4 
print("The type of b: ", type(b))

c = 3 + 4j 
print("The type of c: ", type(c))
print("c is complex number: ", isinstance(3 + 4j, complex))

# string operations 

str = "Hello this is Python programming"
print(str)
hello = 'hello'
print(len(hello))
world = 'world'
hw = hello + ' ' + world  # string concatenation in python
print(hw) 

# apply string formatting with sprintf style 

hw12 = '%s %s %d' % (hello, world, 12)
print(hw12)

# Python lists slicing operation

nums = list(range(5))   #range is a built-in function which creates a list of integers 
print(nums)
print(nums[2:4])        # Get a slice from the index position of 2 to 4


 #assign a new sublist to a slice 

nums=[0,1,2,3,4]
nums[2:4] = [8,9]
print(nums)