# Normal method
squares = []

for i in range(1, 6):
    squares.append(i * i)

print(squares)


# List comprehension method
numbers = [i * i for i in range(1, 6)]

print(numbers)


# Even numbers
even_numbers = [i for i in range(1, 11) if i % 2 == 0]

print(even_numbers)