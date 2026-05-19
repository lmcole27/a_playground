
def func(a, b=[]):
    b.append(a)
    return b

print(func(1))
print(func(2))
print(func(3))

a = 1
b = 2
a, b = b, a
print(a, b) # Output: 2 1

a, b = 3, 1
print( a, b)


print(True + True + True) # Output: 3
print(False + False + False) # Output: 0
print(True + False + True) # Output: 2

print("hello"[-1] + "world"[1]) # Output: "od" 
#remember positive indexing starts at 0, negative indexing starts at -1 

print(list(range(5, -1, -1)))

print("{2}, {1}, {0}".format('a', 'b', 'c'))    # Output: "c, b, a" 

print(len(set([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])))

x = {'a': 1, 'b': 2}
y = dict(x)
y['c'] = 3
print(x)

print("".join([chr(ord(c) + 1) for c in "hello"]))

def multiply(a, b):
    return a * b

print(multiply('5', 3))

print(sum(map(int, "123")))

x =list(map(int, "123")) 
print(sum(x))

x = [1, 2, 3] 
print(x[::-1]) # Slicing [start:stop:step] with step -1 reverses the list
# when start is blank starts at the end 
# when stop is blank it stops at the beginning

print(x[1::-1])    

print(round(5.5), round(6.5))
# In Python 3, the round() function rounds to the nearest even number 
# when the value is exactly halfway between two integers.

import itertools
print(list(itertools.permutations([1, 2, 3], 2)))

print(eval('2 + 3 * 4'))