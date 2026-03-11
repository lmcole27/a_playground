from functools import reduce


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter Even Numbers
evens = filter(lambda x: x % 2 == 0, numbers)

# Square the Even Numbers
squares = map(lambda x: x ** 2, evens)

# Reduce to Sum
total = reduce(lambda x, y: x + y, squares)

print(total)  # Output: 220

numbers = [1, 2, 3, 4, 5, 6]

# One-liner expressing the entire transformation
total = sum([n**2 for n in numbers if n % 2 == 0])

print(total) # Output: 56
