# list
li=[4,'Abhi','Appu',5.5]
print(li)
print(li[2])
print(li[2:])
print(li[::-1])
li.append(6)
print(li)
li.pop()
print(li)
li.insert(2,7)
print(li)

l=[1,2,3,4,5,6]
s=[]
for i in l:
   s.append(i**2)
   print(s)

nums = [0, 1, 2, 3, 4]
squares = []
for x in nums:
    squares.append(x ** 2)
    print(squares)

nums = [0, 1, 2, 3, 4]
even_squares = [x ** 2 for x in nums if x % 2 == 0]
print(even_squares)

tupl = (1, "python", "programming", "spark", 4+5)
print(tupl)
print(tupl[3])

integer = - 200
print('Absolute value is: ', abs(integer))

floating = - 30.67
print('Absolute value is: ', abs(floating))

#all
k = [3, 6, 9, 12]
print(all(k))

k = [0, False]
print(all(k))

k = []
print(all(k))


test1 = [0] 
print(test1, 'is', bool(test1))

test1 = None
print(test1, 'is', bool(test1))

string = "hello python"
array = bytes(string, 'utf-8')
print(array)


code_str = 'x = 5\ny = 10 \nprint("sum", x + y)'
code = compile(code_str, 'sum_py', 'exec')
print(type(code))
exec(code) 

I = [0, False]
print(any(I))

normalText = "Python is the most popular programming language in 2022"
print(ascii(normalText))


string = "python is a high level programming language"
arr = bytearray(string, 'utf-8')
print(arr)

# float format 

print(format(126, "f"))

print(format(125,"b"))


txt1 = "The name of the person is {} , his age is {} ".format("John", 35)
print(txt1)

def calculateAddition(n):
    return n + n

numbers = (1, 5)
result = map(calculateAddition, numbers)
print(result) 
numbersAddition = set(result)
print(numbersAddition)


result = enumerate([1, 2, 3])
print(result)
print(list(result))

result = dict() 
result2 = dict(a = 1, b = 2,c = 3)

print(result)
print(result2)

def filterdata(x): 
    if x < 5:
        return x
        
result = filter(filterdata, (1, 2, 2))

print(list(result))

result = hash(20) # input value 
result1 = hash(22.6) #floating value

print(result)
print(result1)

result1 = slice(5)
result2 = slice(0,5,3) # returns the slice object

print(result1)
print(result2)


str = "pythonisamazing"
asortedlist = sorted(str)
print(asortedlist)

import math as m
a=int(input("enter a number:"))
q=int(m.sqrt(a))
print(q)

Tuple1 = ('n', 'o', 'h', 't', 'y', 'p')
print(list(reversed(Tuple1)))




Range = range(5, 12)
print(list(reversed(Range)))


def calc(x,y):
   if x>y:
    return x
   else:
    return y

num1=int(input("enter a number"))
num2=int(input("enter another number"))
ans=calc(num1,num2)
print(ans)

def number(x):
  if x%2==0:
    return ("even number")
ans=number(8)
print(ans)

def fib(n):   # write a fibonacci series upto n numbers 
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
        print()

fib(2000)  

def isPalindrome(s):
    x = list(s)
    y = []
    y.extend(x)
    x.reverse()
    if (x == y):
        return True
    return False


 # driver code block 
 

s = "malayalam"
a = "python"
val = isPalindrome(s)
val1 = isPalindrome(a)

if val:
    print("Yes, the string is palindrome")
else: 
    print("No, the given input string is not a palindrome") 

    