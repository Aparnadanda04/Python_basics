def isPalindrome(s):
    x = list(s)
  
    y= reversed(x)
    if (x == y):
        return True
    else:
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

    